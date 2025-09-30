from typing import Dict, List, Optional, Any
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from fastapi_amis.amis.components import App, Page, PageSchema
from fastapi_amis.core.logger import logger, LogConfig
from .router import AmisViewRouter


class AmisSite:
    """
    AmisSite 管理站点类
    
    统一管理多个 AmisViewRouter，负责：
    1. 处理所有路由器的视图和页面
    2. 设置路由并挂载到 FastAPI 应用
    3. 提供统一的导航和页面渲染
    """

    def __init__(
            self,
            title: str = "FastAPI Amis Admin",
            logo: str = "https://suda.cdn.bcebos.com/images%2F2021-01%2Fdiamond.svg",
            mount_path: str = "/",
            intercept_fastapi_logs: bool = True,
    ) -> None:
        """
        初始化 AmisSite 实例
        
        Args:
            title: 站点标题，显示在页面顶部
            logo: 站点Logo URL，显示在页面顶部
            mount_path: 挂载路径，默认为根路径 "/"
            intercept_fastapi_logs: 是否接管 FastAPI/Uvicorn 的日志到 loguru，默认 True
        """
        self.title = title
        self.logo = logo
        self.mount_path = mount_path.rstrip('/') or "/"
        self._api_router = APIRouter()
        self._page_routers: Dict[str, AmisViewRouter] = {}  # router_id -> router
        self._app_routers: Dict[str, AmisViewRouter] = {}   # router_id -> router
        self._router_names: Dict[str, str] = {}  # router_id -> name (for display)
        
        # 接管 FastAPI/Uvicorn 日志
        if intercept_fastapi_logs:
            LogConfig.intercept_logging()

    def _setup_route(self) -> None:
        """
        设置所有路由器的路由
        
        遍历所有已注册的路由器，为每个视图创建对应的路由端点，
        并收集应用路由器的页面用于构建主页导航。
        """
        self._api_router = APIRouter()
        app_pages = []
        
        # 为所有路由器设置路由
        for routers in [self._page_routers, self._app_routers]:
            for router in routers.values():
                for view in router.views_dict.values():
                    page_schema = view.page_schema_config
                    if not page_schema:
                        continue
                    
                    logger.info(f"注册路由: {page_schema.url}")
                    
                    # 注册页面路由
                    self._register_page_route(page_schema)
                    
                    # 收集应用页面
                    if router.type == "app":
                        app_pages.append(page_schema)
        
        # 设置应用主页
        if app_pages:
            self._register_app_route(app_pages)
    
    def _register_page_route(self, page_schema: PageSchema) -> None:
        """
        注册单个页面路由
        
        Args:
            page_schema: 页面配置对象，包含URL和页面内容
        """
        @self._api_router.get(page_schema.url, response_class=HTMLResponse)
        async def _(current_page_schema=page_schema) -> HTMLResponse:
            try:
                page_body = current_page_schema.as_page_body()
                if not page_body:
                    return HTMLResponse(content="<h1>Page not available</h1>")
                
                content = page_body.render() if hasattr(page_body, 'render') else Page(body=page_body).render()
                return HTMLResponse(content=content)
            except Exception as e:
                logger.error(f"页面渲染失败: {e}")
                return HTMLResponse(content="<h1>Page rendering error</h1>")
    
    def _register_app_route(self, app_pages: List[PageSchema]) -> None:
        """
        注册应用主页路由
        
        Args:
            app_pages: 应用页面配置列表，用于构建主页导航
        """
        @self._api_router.get(self.mount_path, response_class=HTMLResponse)
        async def _() -> HTMLResponse:
            try:
                app_config = App(
                    brandName=self.title,
                    logo=self.logo,
                    pages=[PageSchema(children=app_pages)]
                )
                return HTMLResponse(content=app_config.render())
            except Exception as e:
                logger.error(f"应用渲染失败: {e}")
                return HTMLResponse(content="<h1>App rendering error</h1>")

    def add_router(self, router: AmisViewRouter) -> str:
        """
        注册 AmisViewRouter 到站点
        
        Args:
            router: 要注册的 AmisViewRouter 实例
            
        Returns:
            str: 注册的路由器ID
            
        Note:
            每个路由器都有唯一的ID，即使名称相同也能正确注册
        """
        router_id = router.id
        self._router_names[router_id] = router.name
        
        target_routers = self._page_routers if router.type == "page" else self._app_routers
        target_routers[router_id] = router
        
        self._setup_route()
        logger.info(f"注册路由器: {router.name} (ID: {router_id[:8]}...)")
        return router_id

    def get_router(self, identifier: str) -> Optional[AmisViewRouter]:
        """
        获取指定名称或ID的路由器
        
        Args:
            identifier: 路由器的名称或ID
            
        Returns:
            Optional[AmisViewRouter]: 找到的路由器实例，如果未找到则返回None
            
        Note:
            优先按ID查找，如果未找到则按名称查找
        """
        # 按ID查找
        for routers in [self._page_routers, self._app_routers]:
            if identifier in routers:
                return routers[identifier]
        
        # 按名称查找
        for routers in [self._page_routers, self._app_routers]:
            for router in routers.values():
                if router.name == identifier:
                    return router
        
        return None

    @property
    def routers(self) -> List[str]:
        """
        获取所有已注册的路由器名称
        
        Returns:
            List[str]: 路由器名称列表
        """
        return list(self._router_names.values())

    @property
    def pages(self) -> List[PageSchema]:
        """
        获取所有页面配置
        
        Returns:
            List[PageSchema]: 所有路由器中的页面配置列表
        """
        return [
            page for routers in [self._page_routers, self._app_routers]
            for router in routers.values()
            for page in router.pages_list
        ]

    @property
    def views(self) -> Dict[str, Any]:
        """
        获取所有视图信息
        
        Returns:
            Dict[str, Any]: 以路由器名称为键的视图字典
        """
        return {
            router.name: router.views_dict
            for routers in [self._page_routers, self._app_routers]
            for router in routers.values()
        }

    def mount_to_app(self, app: FastAPI) -> None:
        """
        将主路由器挂载到 FastAPI 应用
        
        Args:
            app: FastAPI 应用实例
            
        Note:
            如果启用了 intercept_fastapi_logs，请在 uvicorn.run 时设置 log_config=None
            
        Examples:
            >>> import uvicorn
            >>> site = AmisSite(intercept_fastapi_logs=True)
            >>> site.mount_to_app(app)
            >>> uvicorn.run(app, log_config=None)  # 禁用 uvicorn 默认日志
        """
        app.include_router(self._api_router)

    @property
    def page_views(self) -> Dict[str, Any]:
        """
        获取所有页面路由器中的视图
        
        Returns:
            Dict[str, Any]: 以路由器名称为键的页面视图字典
        """
        return {router.name: router.views_dict for router in self._page_routers.values()}

    @property
    def app_views(self) -> Dict[str, Any]:
        """
        获取所有应用路由器中的视图
        
        Returns:
            Dict[str, Any]: 以路由器名称为键的应用视图字典
        """
        return {router.name: router.views_dict for router in self._app_routers.values()}

    def get_view_by_key(self, view_key: str) -> Optional[Dict[str, Any]]:
        """
        根据视图键获取视图信息
        
        Args:
            view_key: 视图的键名
            
        Returns:
            Optional[Dict[str, Any]]: 包含视图信息的字典，如果未找到则返回None
        """
        for routers in [self._page_routers, self._app_routers]:
            for router in routers.values():
                if view_key in router.views_dict:
                    return {view_key: router.views_dict[view_key]}
        return None

    @property
    def site_info(self) -> Dict[str, Any]:
        """
        获取站点信息
        
        Returns:
            Dict[str, Any]: 包含站点详细信息的字典，包括：
                - title: 站点标题
                - logo: 站点Logo URL
                - mount_path: 挂载路径
                - routers_count: 路由器总数
                - total_pages: 总页面数
                - page_views_count: 页面路由器数量
                - app_views_count: 应用路由器数量
                - routers: 所有路由器的详细信息列表
        """
        all_routers = [*self._page_routers.values(), *self._app_routers.values()]
        return {
            "title": self.title,
            "logo": self.logo,
            "mount_path": self.mount_path,
            "routers_count": len(all_routers),
            "total_pages": len(self.pages),
            "page_views_count": len(self._page_routers),
            "app_views_count": len(self._app_routers),
            "routers": [router.router_info for router in all_routers]
        }
