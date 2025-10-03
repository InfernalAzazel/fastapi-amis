# 核心概念

理解 FastAPI Amis 的核心概念将帮助你更好地使用这个框架。

## 架构概览

FastAPI Amis 采用分层架构：

```
┌─────────────────────────────────────┐
│          前端 (Amis UI)             │
├─────────────────────────────────────┤
│      FastAPI Amis 框架层            │
│  ┌─────────┬──────────┬──────────┐  │
│  │  Site   │  Router  │   View   │  │
│  └─────────┴──────────┴──────────┘  │
├─────────────────────────────────────┤
│        FastAPI 核心框架             │
└─────────────────────────────────────┘
```

## 核心组件

### AmisSite - 站点

`AmisSite` 是整个应用的容器，负责：

- 管理所有路由器
- 配置全局设置（标题、Logo 等）
- 生成侧边栏导航
- 挂载到 FastAPI 应用

```python
from fastapi_amis.core.site import AmisSite

site = AmisSite(
    title="我的管理后台",
    logo="https://example.com/logo.png"
)
```

**主要方法：**

- `add_router(router)` - 添加路由器
- `mount_to_app(app, prefix="/")` - 挂载到 FastAPI 应用

### AmisViewRouter - 路由器

`AmisViewRouter` 用于组织相关的视图，一个路由器通常对应侧边栏的一个导航项。

```python
from fastapi_amis.core.router import AmisViewRouter

user_router = AmisViewRouter(
    name="用户管理",  # 导航显示名称
    type="page"       # 路由类型
)
```

**注册视图：**

```python
@user_router.register
class UserListView(AmisView):
    ...
```

### AmisView - 视图

`AmisView` 是页面的基类，每个视图对应一个页面。

```python
from fastapi_amis.core.views import AmisView
from fastapi_amis.amis.components import Page

class UserListView(AmisView):
    page_schema = "用户列表"  # 页面描述
    url = "/users"           # 访问路径
    
    page = Page(             # 页面配置
        title="用户管理",
        body={...}
    )
```

**属性说明：**

- `page_schema`: 页面的文字描述
- `url`: 页面的访问路径（相对于路由器）
- `page`: Amis Page 组件实例

## Amis 组件

FastAPI Amis 封装了 Amis 的组件，使其更易于在 Python 中使用。

### Page - 页面

页面是最顶层的组件：

```python
from fastapi_amis.amis.components import Page

page = Page(
    title="页面标题",
    body=[
        # 页面内容
    ]
)
```

### 常用组件

```python
# CRUD 表格
{
    "type": "crud",
    "api": "/api/users",
    "columns": [...]
}

# 表单
{
    "type": "form",
    "api": "post:/api/users",
    "body": [...]
}

# 卡片
{
    "type": "card",
    "header": {"title": "标题"},
    "body": "内容"
}
```

## 数据流

### 1. 请求流程

```
用户请求 → FastAPI 路由 → AmisView → 渲染 Page → 返回 HTML/JSON
```

### 2. API 交互

```
前端 Amis → API 请求 → FastAPI 端点 → 返回 JSON → 更新 UI
```

### 3. API 响应格式

Amis 要求特定的 JSON 格式：

```python
{
    "status": 0,        # 0=成功, 非0=失败
    "msg": "ok",        # 消息
    "data": {           # 数据
        "items": [...], # 列表数据
        "total": 100    # 总数（分页用）
    }
}
```

## 工作流程

### 典型的开发流程

1. **创建 FastAPI 应用**

```python
from fastapi import FastAPI
app = FastAPI()
```

2. **创建站点**

```python
from fastapi_amis.core.site import AmisSite
site = AmisSite(title="管理后台")
```

3. **创建路由器**

```python
from fastapi_amis.core.router import AmisViewRouter
router = AmisViewRouter(name="用户管理", type="page")
```

4. **创建视图**

```python
from fastapi_amis.core.views import AmisView

@router.register
class UserListView(AmisView):
    page_schema = "用户列表"
    url = "/users"
    page = Page(...)
```

5. **注册路由**

```python
site.add_router(router)
```

6. **挂载站点**

```python
site.mount_to_app(app)
```

7. **运行应用**

```python
import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)
```

## 路由结构

### URL 映射

假设你有以下配置：

```python
site = AmisSite()
user_router = AmisViewRouter(name="users")

@user_router.register
class UserListView(AmisView):
    url = "/list"
```

实际的访问路径为：

- 前端页面：`/` （站点首页）
- 视图页面：`/list` （通过前端路由访问）

### API 端点

你需要单独创建 API 端点：

```python
@app.get("/api/users")
async def get_users():
    return {
        "status": 0,
        "msg": "ok",
        "data": {"items": [...], "total": 100}
    }
```

## 依赖注入

FastAPI Amis 完全支持 FastAPI 的依赖注入系统：

```python
from fastapi import Depends

def get_current_user():
    return {"id": 1, "name": "张三"}

@router.register
class UserProfileView(AmisView):
    page_schema = "个人资料"
    url = "/profile"
    dependencies = [Depends(get_current_user)]
    page = Page(...)
```

## 异步支持

FastAPI Amis 完全支持异步编程：

```python
@app.get("/api/users")
async def get_users():
    users = await db.fetch_users()
    return {"status": 0, "data": {"items": users}}
```

## 类型系统

FastAPI Amis 使用 Pydantic 进行数据验证：

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

@app.post("/api/users")
async def create_user(user: User):
    # user 已经过验证
    return {"status": 0, "data": user.dict()}
```

## 下一步

- [视图和路由](views-and-routers.md) - 深入了解视图和路由
- [Amis 组件](amis-components.md) - 学习使用 Amis 组件
- [站点配置](site-configuration.md) - 配置你的站点

