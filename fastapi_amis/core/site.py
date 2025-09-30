import logging
from typing import Dict, List, Optional, Any
from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse
from fastapi_amis.amis.components import App, Page, PageSchema
from .router import AmisViewRouter

logger = logging.getLogger(__name__)


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
            root_path: str = "/",
    ) -> None:
        self.title = title
        self.logo = logo
        self.root_path = root_path.rstrip('/') or "/"
        self._api_router = APIRouter()
        self._page_routers:  Dict[str, AmisViewRouter] = {}
        self._app_routers:  Dict[str, AmisViewRouter] = {}

    def _setup_route(self) -> None:
        """设置路由"""
        app_pages = []
        # 为页面路由器设置路由
        for _, router in self._page_routers.items():
            for _, view in router.get_views().items():
                page_schema = view.get_page_schema()
                if not page_schema:
                    continue
                
                logger.info(f"注册页面路由: {page_schema.url}")
                
                @self._api_router.get(page_schema.url, response_class=HTMLResponse)
                async def _() -> HTMLResponse:
                    try:
                        page_body = page_schema.as_page_body()
                        if page_body:
                            if hasattr(page_body, 'render'):
                                return HTMLResponse(content=page_body.render())
                            else:
                                return HTMLResponse(content=Page(body=page_body).render())
                        return HTMLResponse(content="<h1>Page not available</h1>")
                    except Exception as e:
                        logger.error(f"页面渲染失败: {e}")
                        return HTMLResponse(content="<h1>Page rendering error</h1>")
        
        # 为应用路由器设置路由
        for _, router in self._app_routers.items():
            for _, view in router.get_views().items():
                page_schema = view.get_page_schema()
                if not page_schema:
                    continue
                
                logger.info(f"注册应用路由: {page_schema.url}")
                app_pages.append(view.get_page_schema())
                
        if app_pages:
            @self._api_router.get(self.root_path, response_class=HTMLResponse)
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
            router: AmisViewRouter 实例
        Returns:
            注册的名称
        """
        router_name = router.name
        if router.type == "page":
            self._page_routers[router_name] = router
        else:
            self._app_routers[router_name] = router
        
        # 设置路由
        self._setup_route()
        
        return router_name

    def get_router(self, name: str) -> Optional[AmisViewRouter]:
        """获取指定名称的路由器"""
        if name in self._page_routers:
            return self._page_routers[name]
        elif name in self._app_routers:
            return self._app_routers[name]
        return None

    def list_routers(self) -> List[str]:
        """列出所有已注册的路由器名称"""
        return list(self._page_routers.keys()) + list(self._app_routers.keys())

    def get_all_pages(self) -> List[PageSchema]:
        """获取所有页面配置"""
        all_pages = []
        for router in self._page_routers.values():
            all_pages.extend(router.get_pages())
        for router in self._app_routers.values():
            all_pages.extend(router.get_pages())
        return all_pages

    def get_all_views(self) -> Dict[str, Any]:
        """获取所有视图信息"""
        all_views = {}
        for router_name, router in self._page_routers.items():
            all_views[router_name] = router.get_views()
        for router_name, router in self._app_routers.items():
            all_views[router_name] = router.get_views()
        return all_views

    def mount_to_app(self, app: FastAPI, prefix: str = "/admin") -> None:
        """将主路由器挂载到 FastAPI 应用"""
        app.include_router(self._api_router, prefix=prefix)

    def get_page_views(self) -> Dict[str, Any]:
        """获取所有页面视图"""
        return {name: router.get_views() for name, router in self._page_routers.items()}

    def get_app_views(self) -> Dict[str, Any]:
        """获取所有应用视图"""
        return {name: router.get_views() for name, router in self._app_routers.items()}

    def get_view_by_key(self, view_key: str) -> Optional[Dict[str, Any]]:
        """根据视图键获取视图信息"""
        # 在页面路由器中查找
        for router in self._page_routers.values():
            views = router.get_views()
            if view_key in views:
                return {view_key: views[view_key]}
        
        # 在应用路由器中查找
        for router in self._app_routers.values():
            views = router.get_views()
            if view_key in views:
                return {view_key: views[view_key]}
        return None

    def get_site_info(self) -> Dict[str, Any]:
        """获取站点信息"""
        all_routers = list(self._page_routers.values()) + list(self._app_routers.values())
        return {
            "title": self.title,
            "logo": self.logo,
            "root_path": self.root_path,
            "routers_count": len(all_routers),
            "total_pages": len(self.get_all_pages()),
            "page_views_count": len(self._page_routers),
            "app_views_count": len(self._app_routers),
            "routers": [router.get_router_info() for router in all_routers]
        }
