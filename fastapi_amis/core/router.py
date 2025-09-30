from typing import Dict, List, Literal, Type, Any, Optional, Callable, Union
import uuid
from fastapi_amis.amis.components import PageSchema
from fastapi_amis.core.views import AmisView


class AmisViewRouter:
    """
    AmisView 路由器
    
    专注于收集和管理 AmisView，不处理路由挂载
    类似于一个视图收集器，由上层组件负责路由处理
    """

    def __init__(
            self, 
            name: str = "default",
            type: Literal['app', 'page'] = 'app', # noqa
            id: Optional[str] = None # noqa
    ):
        """
        初始化 AmisViewRouter 实例
        
        Args:
            name: 路由器名称，用于标识和显示
            type: 路由器类型，'app' 表示应用路由器，'page' 表示页面路由器
            id: 路由器唯一ID，如果不提供则自动生成UUID
        """
        self.name = name
        self.type = type
        self.id = id or str(uuid.uuid4())
        self.views: Dict[str, AmisView] = {}  # 视图名称 -> 视图实例
        self.pages: List[PageSchema] = []     # 页面配置列表

    def register(self, view_class: Optional[Type[AmisView]] = None) -> Union[Callable, Type[AmisView]]:
        """
        注册 AmisView 的装饰器方法
        
        Args:
            view_class: 可选的视图类，如果提供则直接注册，否则返回装饰器函数
            
        Returns:
            Union[Callable, Type[AmisView]]: 装饰器函数或已注册的类
            
        Example:
            @router.register
            class MyView(AmisView):
                # 视图定义
                pass
                
            # 或者直接注册
            router.register(MyView)
        """

        def decorator(cls: Type[AmisView]) -> Type[AmisView]:
            try:
                view = cls()
                view_name = cls.__name__
                self.views[view_name] = view

                # 收集页面配置
                page_schema = view.page_schema_config
                if page_schema:
                    self.pages.append(page_schema)
                else:
                    raise ValueError(f"视图 {cls.__name__} 没有有效的页面配置")

                return cls
            except Exception as e:
                raise ValueError(f"注册视图 {cls.__name__} 失败: {str(e)}")

        return decorator if view_class is None else decorator(view_class)


    @property
    def views_dict(self) -> Dict[str, AmisView]:
        """
        获取所有视图的副本
        
        Returns:
            Dict[str, AmisView]: 视图名称到视图实例的字典副本
        """
        return self.views.copy()

    @property
    def pages_list(self) -> List[PageSchema]:
        """
        获取所有页面配置
        
        Returns:
            List[PageSchema]: 页面配置列表的副本
        """
        return self.pages.copy()

    def clear(self) -> None:
        """
        清空所有注册的视图和页面配置
        
        移除所有已注册的视图实例和页面配置，重置路由器状态
        """
        self.views.clear()
        self.pages.clear()

    @property
    def router_info(self) -> Dict[str, Any]:
        """
        获取路由器的详细信息
        
        Returns:
            Dict[str, Any]: 包含路由器详细信息的字典，包括：
                - name: 路由器名称
                - type: 路由器类型
                - router_id: 路由器唯一ID
                - views_count: 视图数量
                - pages_count: 页面数量
                - views: 视图名称列表
                - pages: 页面URL列表
        """
        return {
            "name": self.name,
            "type": self.type,
            "router_id": self.id,
            "views_count": len(self.views),
            "pages_count": len(self.pages),
            "views": list(self.views.keys()),
            "pages": [page.url for page in self.pages]
        }
