import re
from typing import Optional
from fastapi_amis.amis.components import PageSchema, Page


class AmisView:
    """
    AmisView 基类
    
    用于定义 Amis 页面视图的基础类，提供页面配置和URL生成功能。
    子类需要定义 page_schema 和 page 属性来创建具体的页面。
    """

    page_schema: Optional[str] = None  # 页面标题/标签
    page: Optional[Page] = None        # 页面内容配置
    url: Optional[str] = None          # 页面URL路径
    icon: str = "fa fa-file"          # 页面图标
    
    @property
    def page_schema_config(self) -> Optional[PageSchema]:
        """
        获取页面配置对象
        
        Returns:
            Optional[PageSchema]: 页面配置对象，如果 page_schema 或 page 未定义则返回 None
            
        Note:
            如果 url 未定义，会自动基于类名生成 URL
        """
        if not self.page_schema or not self.page:
            return None

        if not self.url:
            self.url = self._generate_url()

        return PageSchema(
            label=self.page_schema,
            icon=self.icon,
            url=self.url,
            schema=self.page
        )

    def _generate_url(self) -> str:
        """
        基于类名生成URL路径
        
        将驼峰命名的类名转换为下划线命名，并添加斜杠前缀
        
        Returns:
            str: 生成的URL路径，例如：UserListView -> /user_list_view
            
        Example:
            class UserListView(AmisView):  # 生成 URL: /user_list_view
            class SystemInfo(AmisView):    # 生成 URL: /system_info
        """
        class_name = self.__class__.__name__
        snake_case = re.sub('([A-Z])', r'_\1', class_name).lower().lstrip('_')
        return f"/{snake_case}"