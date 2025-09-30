import re
from typing import Optional
from fastapi_amis.amis.components import PageSchema, Page


class AmisView:
    """页面管理员基类"""

    page_schema: Optional[str] = None
    page: Optional[Page] = None
    url: Optional[str] = None
    icon: str = "fa fa-file"

    def get_page_schema(self) -> Optional[PageSchema]:
        """获取页面配置"""
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
        """生成基于类名的URL"""
        class_name = self.__class__.__name__
        snake_case = re.sub('([A-Z])', r'_\1', class_name).lower().lstrip('_')
        return f"/{snake_case}"

    async def get_page(self) -> Optional[Page]:
        """获取页面实例，支持动态生成"""
        return self.page