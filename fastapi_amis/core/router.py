from typing import Dict, List, Literal, Type, Any, Optional, Callable, Union
from fastapi_amis.amis.components import PageSchema
from fastapi_amis.core.views import AmisView


class AmisViewRouter:
    """
    AmisView 路由器
    
    专注于收集和管理 AmisView，不处理路由挂载
    类似于一个视图收集器，由上层组件负责路由处理
    """

    def __init__(
            self, name: str = "default",
            type: Literal['app', 'page'] = 'app'
    ):
        self.name = name
        self.type = type
        self.views: Dict[str, AmisView] = {}
        self.pages: List[PageSchema] = []

    def register(self, view_class: Optional[Type[AmisView]] = None) -> Union[Callable, Type[AmisView]]:
        """
        注册 AmisView 的装饰器
        
        Args:
            view_class: 可选的视图类，如果提供则直接注册
            
        Returns:
            装饰器函数或已注册的类
        """

        def decorator(cls: Type[AmisView]) -> Type[AmisView]:
            try:
                view = cls()
                view_name = cls.__name__
                self.views[view_name] = view

                # 收集页面配置，但不处理路由
                page_schema = view.get_page_schema()
                if page_schema:
                    # 添加到页面列表
                    self.pages.append(page_schema)
                else:
                    raise ValueError(f"视图 {cls.__name__} 没有有效的页面配置")

                return cls
            except Exception as e:
                raise ValueError(f"注册视图 {cls.__name__} 失败: {str(e)}")

        return decorator if view_class is None else decorator(view_class)

    def add_view(self, view: AmisView, name: Optional[str] = None) -> str:
        """
        直接添加视图实例
        
        Args:
            view: 视图实例
            name: 可选的名称，如果不提供则使用类名
            
        Returns:
            注册的名称
        """
        view_name = name or view.__class__.__name__
        self.views[view_name] = view

        page_schema = view.get_page_schema()
        if page_schema:
            self.pages.append(page_schema)

        return view_name

    def remove_view(self, name: str) -> bool:
        """
        移除视图
        
        Args:
            name: 视图名称
            
        Returns:
            是否成功移除
        """
        if name in self.views:
            view = self.views.pop(name)
            # 同时从页面列表中移除
            page_schema = view.get_page_schema()
            if page_schema and page_schema in self.pages:
                self.pages.remove(page_schema)
            return True
        return False

    def get_view(self, name: str) -> Optional[AmisView]:
        """获取指定名称的视图"""
        return self.views.get(name)

    def list_views(self) -> List[str]:
        """列出所有已注册的视图名称"""
        return list(self.views.keys())

    def get_views(self) -> Dict[str, AmisView]:
        """获取所有视图的副本"""
        return self.views.copy()

    def get_pages(self) -> List[PageSchema]:
        """获取所有页面配置"""
        return self.pages.copy()

    def clear(self) -> None:
        """清空所有注册的视图"""
        self.views.clear()
        self.pages.clear()

    def get_router_info(self) -> Dict[str, Any]:
        """获取路由器信息"""
        return {
            "name": self.name,
            "type": self.type,
            "views_count": len(self.views),
            "pages_count": len(self.pages),
            "views": list(self.views.keys()),
            "pages": [page.url for page in self.pages]
        }
