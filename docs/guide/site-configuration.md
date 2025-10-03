# 站点配置

`AmisSite` 提供了丰富的配置选项，让你可以自定义管理后台的外观和行为。

## 基础配置

### 创建站点

```python
from fastapi_amis.core.site import AmisSite

site = AmisSite(
    title="我的管理后台",
    logo="https://example.com/logo.png"
)
```

### 常用参数

```python
site = AmisSite(
    title="管理后台",              # 站点标题
    logo="https://...",           # Logo URL
    favicon="https://...",        # 网站图标
    description="系统描述",        # 站点描述
    theme="cxd"                   # 主题名称
)
```

## 主题配置

Amis 提供了多个内置主题：

```python
# 默认主题
site = AmisSite(theme="cxd")

# 暗黑主题
site = AmisSite(theme="dark")

# 移动端主题
site = AmisSite(theme="antd")
```

### 自定义主题色

```python
site = AmisSite(
    title="管理后台",
    theme={
        "className": "my-theme",
        "colors": {
            "primary": "#007bff",
            "success": "#28a745",
            "warning": "#ffc107",
            "danger": "#dc3545",
            "info": "#17a2b8"
        }
    }
)
```

## 导航配置

### 侧边栏导航

```python
# 添加路由器到站点
user_router = AmisViewRouter(
    name="用户管理",
    icon="fa fa-users"
)
site.add_router(user_router)

system_router = AmisViewRouter(
    name="系统设置",
    icon="fa fa-cog"
)
site.add_router(system_router)
```

### 导航位置

```python
site = AmisSite(
    title="管理后台",
    asideResizor=True,        # 允许调整侧边栏大小
    asideSticky=True,         # 侧边栏固定
    asideMinified=False,      # 默认是否收起侧边栏
)
```

### 顶部导航

```python
site = AmisSite(
    title="管理后台",
    header={
        "title": "管理后台",
        "logo": "https://...",
        "body": [
            {
                "type": "tpl",
                "tpl": '<div class="ml-auto">用户：Admin</div>'
            }
        ]
    }
)
```

## 页面布局

### 布局模式

```python
# 侧边栏布局（默认）
site = AmisSite(layout="aside")

# 顶部导航布局
site = AmisSite(layout="header")

# 混合布局
site = AmisSite(layout="auto")
```

### 内容区域

```python
site = AmisSite(
    title="管理后台",
    body={
        "type": "page",
        "className": "custom-page",
        "body": [
            # 页面内容
        ]
    }
)
```

## 挂载配置

### 挂载到 FastAPI

```python
from fastapi import FastAPI

app = FastAPI()

# 默认挂载到根路径
site.mount_to_app(app)

# 挂载到指定路径
site.mount_to_app(app, prefix="/admin")
```

### 多站点挂载

```python
# 前台站点
frontend_site = AmisSite(title="前台系统")
frontend_site.mount_to_app(app, prefix="/")

# 后台站点
admin_site = AmisSite(title="后台管理")
admin_site.mount_to_app(app, prefix="/admin")
```

## 高级配置

### 自定义页面模板

FastAPI Amis 使用 Jinja2 模板，你可以自定义模板：

```python
site = AmisSite(
    title="管理后台",
    template_path="/path/to/templates",  # 自定义模板目录
    template_name="my_template.html"     # 自定义模板文件
)
```

### API 前缀

```python
site = AmisSite(
    title="管理后台",
    api_prefix="/api/v1"  # API 路径前缀
)
```

### 静态资源

```python
site = AmisSite(
    title="管理后台",
    static_path="/static",      # 静态文件路径
    static_url="/static"        # 静态文件 URL
)
```

## 国际化

### 设置语言

```python
site = AmisSite(
    title="管理后台",
    locale="zh-CN"  # 中文
    # locale="en-US"  # 英文
)
```

### 自定义翻译

```python
site = AmisSite(
    title="管理后台",
    locale="zh-CN",
    translations={
        "zh-CN": {
            "save": "保存",
            "cancel": "取消",
            "confirm": "确定"
        }
    }
)
```

## 权限配置

### 全局权限检查

```python
from fastapi import Depends

def check_auth(request: Request):
    """全局权限检查"""
    if not request.state.user:
        raise HTTPException(status_code=401)

site = AmisSite(
    title="管理后台",
    dependencies=[Depends(check_auth)]
)
```

### 路由级权限

```python
def require_admin():
    def dependency(request: Request):
        if not request.state.user.is_admin:
            raise HTTPException(status_code=403)
    return Depends(dependency)

admin_router = AmisViewRouter(
    name="管理员",
    dependencies=[require_admin()]
)
```

## 完整配置示例

```python
from fastapi import FastAPI, Depends
from fastapi_amis.core.site import AmisSite
from fastapi_amis.core.router import AmisViewRouter

app = FastAPI()

# 创建站点
site = AmisSite(
    # 基础配置
    title="企业管理系统",
    logo="https://example.com/logo.png",
    favicon="https://example.com/favicon.ico",
    description="企业内部管理系统",
    
    # 主题配置
    theme="cxd",
    
    # 布局配置
    layout="aside",
    asideResizor=True,
    asideSticky=True,
    
    # 顶部配置
    header={
        "title": "企业管理系统",
        "logo": "https://example.com/logo.png",
        "body": [
            {
                "type": "dropdown-button",
                "label": "${user.name}",
                "className": "ml-auto",
                "trigger": "hover",
                "buttons": [
                    {
                        "type": "button",
                        "label": "个人设置",
                        "actionType": "link",
                        "link": "/profile"
                    },
                    {
                        "type": "button",
                        "label": "退出登录",
                        "actionType": "ajax",
                        "api": "post:/api/logout"
                    }
                ]
            }
        ]
    },
    
    # API 配置
    api_prefix="/api",
    
    # 国际化
    locale="zh-CN"
)

# 创建路由
dashboard_router = AmisViewRouter(
    name="仪表盘",
    icon="fa fa-dashboard"
)

user_router = AmisViewRouter(
    name="用户管理",
    icon="fa fa-users"
)

system_router = AmisViewRouter(
    name="系统设置",
    icon="fa fa-cog"
)

# 添加路由
site.add_router(dashboard_router)
site.add_router(user_router)
site.add_router(system_router)

# 挂载到应用
site.mount_to_app(app, prefix="/admin")
```

## 环境变量配置

推荐使用环境变量管理配置：

```python
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_title: str = "管理后台"
    app_logo: str = ""
    app_theme: str = "cxd"
    
    class Config:
        env_file = ".env"

settings = Settings()

site = AmisSite(
    title=settings.app_title,
    logo=settings.app_logo,
    theme=settings.app_theme
)
```

`.env` 文件：

```env
APP_TITLE=我的管理后台
APP_LOGO=https://example.com/logo.png
APP_THEME=cxd
```

## 下一步

- [API 参考](../api/core.md) - 查看完整的 API 文档
- [最佳实践](../best-practices/development.md) - 开发建议
- [示例项目](../getting-started/examples.md) - 查看实际应用

