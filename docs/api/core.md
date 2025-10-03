# 核心模块 API

FastAPI Amis 核心模块的 API 参考文档。

## AmisSite

站点管理类，用于创建和管理整个管理后台应用。

### 类定义

```python
class AmisSite:
    def __init__(
        self,
        title: str = "Admin",
        logo: Optional[str] = None,
        favicon: Optional[str] = None,
        description: Optional[str] = None,
        theme: str = "cxd",
        layout: str = "aside",
        **kwargs
    )
```

### 参数

- `title` (str): 站点标题，默认 "Admin"
- `logo` (Optional[str]): Logo URL
- `favicon` (Optional[str]): 网站图标 URL
- `description` (Optional[str]): 站点描述
- `theme` (str): 主题名称，默认 "cxd"
- `layout` (str): 布局模式，默认 "aside"

### 方法

#### add_router

添加路由器到站点。

```python
def add_router(
    self,
    router: AmisViewRouter,
    *, 
    visible: bool = True
) -> None
```

**参数：**

- `router` (AmisViewRouter): 要添加的路由器
- `visible` (bool): 是否在导航中显示，默认 True

**示例：**

```python
site = AmisSite(title="管理后台")
user_router = AmisViewRouter(name="用户管理")
site.add_router(user_router)
```

#### mount_to_app

将站点挂载到 FastAPI 应用。

```python
def mount_to_app(
    self,
    app: FastAPI,
    *,
    prefix: str = "",
    tags: Optional[List[str]] = None
) -> None
```

**参数：**

- `app` (FastAPI): FastAPI 应用实例
- `prefix` (str): URL 前缀，默认 ""
- `tags` (Optional[List[str]]): OpenAPI 标签

**示例：**

```python
app = FastAPI()
site.mount_to_app(app, prefix="/admin")
```

## AmisViewRouter

路由器类，用于组织相关的视图。

### 类定义

```python
class AmisViewRouter:
    def __init__(
        self,
        name: str,
        type: str = "page",
        icon: Optional[str] = None,
        visible: bool = True,
        **kwargs
    )
```

### 参数

- `name` (str): 路由器名称，显示在导航中
- `type` (str): 路由类型，默认 "page"
- `icon` (Optional[str]): 图标类名
- `visible` (bool): 是否在导航中显示，默认 True

### 方法

#### register

装饰器方法，用于注册视图到路由器。

```python
def register(
    self,
    view_class: Type[AmisView]
) -> Type[AmisView]
```

**参数：**

- `view_class` (Type[AmisView]): 视图类

**返回：**

- Type[AmisView]: 注册后的视图类

**示例：**

```python
router = AmisViewRouter(name="用户管理")

@router.register
class UserListView(AmisView):
    page_schema = "用户列表"
    url = "/users"
    page = Page(...)
```

## AmisView

视图基类，所有页面视图都应继承此类。

### 类定义

```python
class AmisView:
    page_schema: str
    url: str
    page: Page
    icon: Optional[str] = None
    visible: bool = True
    dependencies: List[Depends] = []
```

### 属性

- `page_schema` (str): 页面描述
- `url` (str): 访问路径
- `page` (Page): Amis Page 组件实例
- `icon` (Optional[str]): 页面图标
- `visible` (bool): 是否在导航中显示
- `dependencies` (List[Depends]): FastAPI 依赖项列表

### 示例

```python
class MyView(AmisView):
    page_schema = "我的页面"
    url = "/my-page"
    page = Page(
        title="页面标题",
        body=[...]
    )
```

### 高级用法

#### 动态页面

可以通过方法动态生成页面内容：

```python
class DynamicView(AmisView):
    page_schema = "动态页面"
    url = "/dynamic"
    
    def get_page(self, request: Request) -> Page:
        """根据请求动态生成页面"""
        user = request.state.user
        return Page(
            title=f"欢迎 {user.name}",
            body=[...]
        )
```

#### 依赖注入

使用 FastAPI 的依赖注入：

```python
from fastapi import Depends

def get_current_user(request: Request):
    return request.state.user

class UserProfileView(AmisView):
    page_schema = "个人资料"
    url = "/profile"
    dependencies = [Depends(get_current_user)]
    page = Page(...)
```

## 类型定义

### BaseAmisModel

所有 Amis 组件的基类。

```python
from pydantic import BaseModel

class BaseAmisModel(BaseModel):
    type: str
    
    class Config:
        extra = "allow"
```

### PageSchema

页面配置的类型定义。

```python
class PageSchema(BaseModel):
    title: Optional[str] = None
    subTitle: Optional[str] = None
    body: Union[Dict, List, str]
    toolbar: Optional[List] = None
    aside: Optional[Dict] = None
```

## 工具函数

### create_app_from_site

从站点创建 FastAPI 应用的便捷函数。

```python
def create_app_from_site(
    site: AmisSite,
    **fastapi_kwargs
) -> FastAPI:
    """创建并配置 FastAPI 应用"""
    app = FastAPI(**fastapi_kwargs)
    site.mount_to_app(app)
    return app
```

**示例：**

```python
site = AmisSite(title="管理后台")
# ... 配置站点

app = create_app_from_site(
    site,
    title="管理后台 API",
    version="1.0.0"
)
```

## 异常类

### AmisException

框架的基础异常类。

```python
class AmisException(Exception):
    def __init__(
        self,
        message: str,
        status_code: int = 400,
        **kwargs
    ):
        self.message = message
        self.status_code = status_code
        self.extra = kwargs
```

**示例：**

```python
from fastapi_amis.extensions.exception import AmisException

if not user:
    raise AmisException(
        message="用户不存在",
        status_code=404
    )
```

## 下一步

- [Amis 组件 API](components.md) - Amis 组件的 API 参考
- [扩展功能 API](extensions.md) - 扩展模块的 API 参考
- [类型定义](types.md) - 完整的类型定义

