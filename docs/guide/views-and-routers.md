# 视图和路由

视图和路由是 FastAPI Amis 的核心概念，本文将详细介绍如何使用它们。

## AmisViewRouter

路由器用于组织相关的视图，通常对应侧边栏的一个菜单项。

### 基本用法

```python
from fastapi_amis.core.router import AmisViewRouter

router = AmisViewRouter(
    name="用户管理",      # 显示名称
    type="page",         # 路由类型
    icon="fa fa-users"   # 图标（可选）
)
```

### 参数说明

- `name`: 路由器名称，显示在侧边栏
- `type`: 路由类型，通常为 "page"
- `icon`: 图标类名（Font Awesome 或自定义）
- `visible`: 是否在导航中显示（默认 True）

### 注册视图

使用装饰器注册视图：

```python
@router.register
class UserListView(AmisView):
    page_schema = "用户列表"
    url = "/users"
    page = Page(...)
```

### 多个路由器

一个应用可以有多个路由器：

```python
# 用户管理
user_router = AmisViewRouter(name="用户管理", type="page")

# 系统设置
system_router = AmisViewRouter(name="系统设置", type="page")

# 添加到站点
site.add_router(user_router)
site.add_router(system_router)
```

## AmisView

视图是页面的抽象，每个视图对应一个页面。

### 基本结构

```python
from fastapi_amis.core.views import AmisView
from fastapi_amis.amis.components import Page

class MyView(AmisView):
    # 页面描述
    page_schema = "我的页面"
    
    # 访问路径
    url = "/my-page"
    
    # 页面配置
    page = Page(
        title="页面标题",
        body=[...]
    )
```

### 必需属性

- `page_schema`: 页面的文字描述
- `url`: 页面的访问路径
- `page`: Amis Page 组件实例

### 可选属性

- `icon`: 页面图标
- `visible`: 是否在导航中显示
- `dependencies`: FastAPI 依赖项

### 动态页面

可以通过方法动态生成页面：

```python
class DynamicView(AmisView):
    page_schema = "动态页面"
    url = "/dynamic"
    
    def get_page(self, request):
        """根据请求动态生成页面"""
        user = request.state.user
        return Page(
            title=f"欢迎 {user.name}",
            body=[...]
        )
```

## 页面类型

### 1. 列表页面

展示数据列表：

```python
@router.register
class UserListView(AmisView):
    page_schema = "用户列表"
    url = "/users"
    
    page = Page(
        title="用户管理",
        body={
            "type": "crud",
            "api": "/api/users",
            "columns": [
                {"name": "id", "label": "ID", "type": "text"},
                {"name": "name", "label": "姓名", "type": "text"},
                {"name": "email", "label": "邮箱", "type": "text"},
            ],
            "headerToolbar": ["bulkActions", "export", "filter-toggler"],
            "footerToolbar": ["statistics", "pagination"],
        }
    )
```

### 2. 表单页面

创建或编辑数据：

```python
@router.register
class UserFormView(AmisView):
    page_schema = "添加用户"
    url = "/users/new"
    
    page = Page(
        title="添加用户",
        body={
            "type": "form",
            "api": "post:/api/users",
            "body": [
                {
                    "type": "input-text",
                    "name": "name",
                    "label": "姓名",
                    "required": True
                },
                {
                    "type": "input-email",
                    "name": "email",
                    "label": "邮箱",
                    "required": True
                },
                {
                    "type": "select",
                    "name": "role",
                    "label": "角色",
                    "options": [
                        {"label": "管理员", "value": "admin"},
                        {"label": "普通用户", "value": "user"}
                    ]
                }
            ]
        }
    )
```

### 3. 详情页面

展示单条数据的详细信息：

```python
@router.register
class UserDetailView(AmisView):
    page_schema = "用户详情"
    url = "/users/{id}"
    
    page = Page(
        title="用户详情",
        body={
            "type": "service",
            "api": "/api/users/${id}",
            "body": [
                {
                    "type": "panel",
                    "title": "基本信息",
                    "body": [
                        {"type": "static", "label": "ID", "name": "id"},
                        {"type": "static", "label": "姓名", "name": "name"},
                        {"type": "static", "label": "邮箱", "name": "email"},
                    ]
                }
            ]
        }
    )
```

### 4. 仪表盘

展示统计信息：

```python
@router.register
class DashboardView(AmisView):
    page_schema = "仪表盘"
    url = "/"
    
    page = Page(
        title="数据概览",
        body=[
            {
                "type": "grid",
                "columns": [
                    {
                        "body": {
                            "type": "panel",
                            "title": "用户总数",
                            "body": {
                                "type": "tpl",
                                "tpl": '<div class="stat-value">${count}</div>'
                            }
                        }
                    },
                    # 更多统计卡片...
                ]
            },
            {
                "type": "chart",
                "api": "/api/stats/chart",
                "config": {
                    "xAxis": {"type": "category"},
                    "yAxis": {},
                    "series": [{"type": "line", "data": []}]
                }
            }
        ]
    )
```

## 路由嵌套

可以创建嵌套的路由结构：

```python
# 父路由
user_router = AmisViewRouter(name="用户管理", type="page")

# 子视图
@user_router.register
class UserListView(AmisView):
    page_schema = "用户列表"
    url = "/list"
    page = Page(...)

@user_router.register
class UserAddView(AmisView):
    page_schema = "添加用户"
    url = "/add"
    page = Page(...)

@user_router.register
class UserEditView(AmisView):
    page_schema = "编辑用户"
    url = "/edit/{id}"
    page = Page(...)
```

## 权限控制

使用 FastAPI 的依赖注入进行权限控制：

```python
from fastapi import Depends, HTTPException

def require_admin(request: Request):
    """要求管理员权限"""
    if not request.state.user.is_admin:
        raise HTTPException(status_code=403, detail="权限不足")

@router.register
class AdminView(AmisView):
    page_schema = "管理员页面"
    url = "/admin"
    dependencies = [Depends(require_admin)]
    page = Page(...)
```

## 路由组织

### 按功能模块组织

```python
# routers/user.py
user_router = AmisViewRouter(name="用户管理")
# ... 注册用户相关视图

# routers/product.py
product_router = AmisViewRouter(name="商品管理")
# ... 注册商品相关视图

# main.py
from routers.user import user_router
from routers.product import product_router

site.add_router(user_router)
site.add_router(product_router)
```

### 按业务领域组织

```python
# 前台业务
frontend_site = AmisSite(title="前台系统")
frontend_site.add_router(order_router)
frontend_site.add_router(customer_router)

# 后台管理
admin_site = AmisSite(title="后台管理")
admin_site.add_router(user_router)
admin_site.add_router(system_router)

# 挂载到不同的路径
frontend_site.mount_to_app(app, prefix="/frontend")
admin_site.mount_to_app(app, prefix="/admin")
```

## 最佳实践

### 1. 命名规范

```python
# 路由器：使用复数名词 + _router
user_router = AmisViewRouter(name="用户管理")

# 视图：使用名词 + 动作 + View
class UserListView(AmisView): ...
class UserCreateView(AmisView): ...
class UserUpdateView(AmisView): ...
class UserDeleteView(AmisView): ...
```

### 2. URL 设计

```python
# 列表页
url = "/users"

# 创建页
url = "/users/new"

# 编辑页
url = "/users/{id}/edit"

# 详情页
url = "/users/{id}"
```

### 3. 代码组织

```python
# views/user.py
class UserViews:
    """用户相关视图"""
    
    @staticmethod
    def create_list_view():
        @user_router.register
        class UserListView(AmisView):
            ...
        return UserListView
    
    @staticmethod
    def create_form_view():
        @user_router.register
        class UserFormView(AmisView):
            ...
        return UserFormView
```

## 下一步

- [Amis 组件](amis-components.md) - 学习使用 Amis UI 组件
- [站点配置](site-configuration.md) - 配置站点外观和行为
- [API 参考](../api/core.md) - 查看完整的 API 文档

