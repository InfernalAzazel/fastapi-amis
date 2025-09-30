from typing import Optional
from fastapi_amis.amis.components import Page
from fastapi_amis.core.views import AmisView


class LinkAdminView(AmisView):
    """链接管理员类，用于创建跳转链接"""

    link: Optional[str] = None

    def __init__(self):
        super().__init__()
        if self.link:
            self.page = self._create_link_page()

    def _create_link_page(self) -> Page:
        """创建链接页面"""
        return Page(
            title=self.page_schema or "链接页面",
            body={
                "type": "container",
                "body": [
                    {
                        "type": "tpl",
                        "tpl": f"<p>正在跳转到: <a href='{self.link}' target='_blank'>{self.link}</a></p>"
                    },
                    {
                        "type": "button",
                        "label": "打开链接",
                        "level": "primary",
                        "actionType": "url",
                        "url": self.link,
                        "blank": True
                    }
                ]
            }
        )


class IframeAdminView(AmisView):
    """内嵌页面管理员类，用于创建内嵌页面"""

    src: Optional[str] = None

    def __init__(self):
        super().__init__()
        if self.src:
            self.page = self._create_iframe_page()

    def _create_iframe_page(self) -> Page:
        """创建内嵌页面"""
        return Page(
            title=self.page_schema or "内嵌页面",
            body={
                "type": "iframe",
                "src": self.src,
                "width": "100%",
                "height": "600px"
            }
        )