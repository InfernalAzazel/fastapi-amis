# 示例项目

FastAPI Amis 提供了多个示例项目，帮助你快速上手和学习不同的功能。

## 运行示例

首先克隆项目仓库：

```bash
git clone https://github.com/InfernalAzazel/fastapi-amis.git
cd fastapi-amis
```

安装依赖：

```bash
uv sync
# 或
pip install -e ".[dev]"
```

## 示例 1：简单管理后台

这是一个最简单的示例，展示了如何快速搭建一个管理后台。

### 运行示例

```bash
cd example
uv run python simple_example.py
# 或
python simple_example.py
```

访问：http://localhost:4000

### 代码位置

`example/simple_example.py`

### 功能展示

- ✅ 基本的页面结构
- ✅ 侧边栏导航
- ✅ 简单的 CRUD 操作
- ✅ 表单组件
- ✅ 表格组件

### 核心代码

```python
from fastapi import FastAPI
from fastapi_amis.core.router import AmisViewRouter
from fastapi_amis.core.site import AmisSite

def create_app():
    app = FastAPI()
    site = AmisSite(title="简单示例")
    
    # 添加路由和视图
    router = AmisViewRouter(name="首页", type="page")
    # ... 注册视图
    
    site.add_router(router)
    site.mount_to_app(app)
    return app
```

## 示例 2：多页面应用

这个示例展示了如何创建一个包含多个页面和功能模块的完整应用。

### 运行示例

```bash
cd example
uv run python main.py
# 或
python main.py
```

访问：http://localhost:3000

### 代码位置

`example/main.py`

### 功能展示

- ✅ 多个页面路由
- ✅ 仪表盘展示
- ✅ 用户管理
- ✅ 系统设置
- ✅ 数据可视化
- ✅ 复杂表单

### 核心代码

```python
app = FastAPI()
site = AmisSite(title="多页面示例")

# 仪表盘
dashboard_router = AmisViewRouter(name="仪表盘", type="page")
# ... 注册仪表盘视图

# 用户管理
user_router = AmisViewRouter(name="用户管理", type="page")
# ... 注册用户视图

# 添加所有路由
site.add_router(dashboard_router)
site.add_router(user_router)
site.mount_to_app(app)
```

## 示例 3：异常处理

展示如何在 FastAPI Amis 中处理异常。

### 代码位置

`example/exception_example.py`

### 功能展示

- ✅ 全局异常处理
- ✅ 自定义错误页面
- ✅ 错误日志记录
- ✅ 用户友好的错误提示

### 核心代码

```python
from fastapi_amis.extensions.exception import AmisException

@app.exception_handler(AmisException)
async def amis_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": 1, "msg": exc.message}
    )
```

## 示例 4：日志配置

展示如何配置和使用日志系统。

### 代码位置

`example/logger_example.py`

### 功能展示

- ✅ 日志配置
- ✅ 不同级别的日志
- ✅ 日志文件输出
- ✅ 结构化日志

## 使用 Uvicorn 运行

所有示例都可以使用 uvicorn 运行：

```bash
# 运行 simple_example.py
uvicorn example.simple_example:create_app --factory --reload --port 4000

# 运行 main.py
uvicorn example.main:app --reload --port 3000
```

## 常见用例

### 基础 CRUD

最常见的用例是创建、读取、更新和删除数据：

```python
@router.register
class UserCRUDView(AmisView):
    page_schema = "用户管理"
    url = "/users"
    
    page = Page(
        title="用户管理",
        body={
            "type": "crud",
            "api": "/api/users",
            "columns": [
                {"name": "id", "label": "ID"},
                {"name": "name", "label": "姓名"},
            ]
        }
    )
```

### 表单提交

创建表单页面：

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
                {"type": "input-text", "name": "name", "label": "姓名"},
                {"type": "input-email", "name": "email", "label": "邮箱"},
            ]
        }
    )
```

### 数据展示

展示统计数据：

```python
@router.register
class DashboardView(AmisView):
    page_schema = "仪表盘"
    url = "/dashboard"
    
    page = Page(
        title="数据概览",
        body=[
            {
                "type": "cards",
                "source": "/api/stats",
                "card": {
                    "body": [
                        {"type": "tpl", "tpl": "${title}"},
                        {"type": "tpl", "tpl": "${value}"}
                    ]
                }
            }
        ]
    )
```

## 进阶示例

### 自定义组件

如何创建和使用自定义组件：

```python
from fastapi_amis.amis.components import BaseComponent

class CustomCard(BaseComponent):
    type: str = "custom-card"
    title: str
    content: str
```

### API 集成

与后端 API 集成：

```python
@app.get("/api/users")
async def get_users(page: int = 1, perPage: int = 10):
    # 从数据库获取数据
    users = await db.get_users(page, perPage)
    return {
        "status": 0,
        "msg": "ok",
        "data": {
            "items": users,
            "total": await db.count_users()
        }
    }
```

### 权限控制

添加权限验证：

```python
from fastapi import Depends
from fastapi_amis.core.views import AmisView

@router.register
class AdminView(AmisView):
    page_schema = "管理员页面"
    url = "/admin"
    dependencies = [Depends(check_admin_permission)]
    
    page = Page(...)
```

## 完整项目模板

查看我们的项目模板仓库（即将推出），获取生产就绪的项目结构。

## 下一步

- [了解核心概念](../guide/concepts.md) - 深入理解框架原理
- [Amis 组件文档](../guide/amis-components.md) - 学习更多 UI 组件
- [API 参考](../api/core.md) - 查看完整的 API 文档

## 获取帮助

如果在运行示例时遇到问题：

1. 检查 Python 版本是否 >= 3.10
2. 确保所有依赖都已正确安装
3. 查看终端的错误信息
4. 访问 [GitHub Issues](https://github.com/InfernalAzazel/fastapi-amis/issues) 寻求帮助

