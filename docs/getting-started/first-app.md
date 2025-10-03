# 第一个应用

在这个教程中，我们将创建一个简单的管理后台应用，展示如何使用 FastAPI Amis 的核心功能。

## 创建项目

首先，创建一个新的项目目录：

```bash
mkdir my-admin-app
cd my-admin-app
```

## 创建应用文件

创建一个名为 `app.py` 的文件：

```python
from fastapi import FastAPI
from fastapi_amis.core.router import AmisViewRouter
from fastapi_amis.core.site import AmisSite
from fastapi_amis.core.views import AmisView
from fastapi_amis.amis.components import Page

# 创建 FastAPI 应用
app = FastAPI(title="我的管理后台")

# 创建站点
site = AmisSite(
    title="我的管理后台",
    logo="https://baidu.gitee.io/amis/static/logo_408c434.png"
)

# 创建用户管理路由
user_router = AmisViewRouter(name="用户管理", type="page")

@user_router.register
class UserListView(AmisView):
    """用户列表页面"""
    page_schema = "用户列表"
    url = "/users"
    
    page = Page(
        title="用户管理",
        body=[
            {
                "type": "crud",
                "syncLocation": False,
                "api": "/api/users",
                "columns": [
                    {"name": "id", "label": "ID", "type": "text"},
                    {"name": "name", "label": "姓名", "type": "text"},
                    {"name": "email", "label": "邮箱", "type": "text"},
                    {"name": "status", "label": "状态", "type": "status"},
                ]
            }
        ]
    )

# 创建仪表盘路由
dashboard_router = AmisViewRouter(name="仪表盘", type="page")

@dashboard_router.register
class DashboardView(AmisView):
    """仪表盘页面"""
    page_schema = "仪表盘"
    url = "/"
    
    page = Page(
        title="欢迎使用",
        body=[
            {
                "type": "panel",
                "title": "系统概览",
                "body": "这是一个使用 FastAPI Amis 构建的管理后台系统"
            },
            {
                "type": "grid",
                "columns": [
                    {
                        "body": [
                            {
                                "type": "panel",
                                "title": "用户总数",
                                "body": {
                                    "type": "tpl",
                                    "tpl": '<div style="font-size: 2em; text-align: center;">1,234</div>'
                                }
                            }
                        ]
                    },
                    {
                        "body": [
                            {
                                "type": "panel",
                                "title": "今日访问",
                                "body": {
                                    "type": "tpl",
                                    "tpl": '<div style="font-size: 2em; text-align: center;">567</div>'
                                }
                            }
                        ]
                    },
                    {
                        "body": [
                            {
                                "type": "panel",
                                "title": "活跃用户",
                                "body": {
                                    "type": "tpl",
                                    "tpl": '<div style="font-size: 2em; text-align: center;">89</div>'
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    )

# 添加路由到站点
site.add_router(dashboard_router)
site.add_router(user_router)

# 挂载到 FastAPI 应用
site.mount_to_app(app)

# 添加 API 端点（模拟数据）
@app.get("/api/users")
async def get_users():
    """获取用户列表"""
    return {
        "status": 0,
        "msg": "ok",
        "data": {
            "items": [
                {"id": 1, "name": "张三", "email": "zhangsan@example.com", "status": 1},
                {"id": 2, "name": "李四", "email": "lisi@example.com", "status": 1},
                {"id": 3, "name": "王五", "email": "wangwu@example.com", "status": 0},
            ],
            "total": 3
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## 运行应用

运行你的第一个应用：

```bash
python app.py
```

或者使用 uvicorn：

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

现在打开浏览器访问 http://localhost:8000，你将看到一个完整的管理后台界面！

## 代码解析

让我们逐步分析代码的各个部分：

### 1. 创建站点

```python
site = AmisSite(
    title="我的管理后台",
    logo="https://baidu.gitee.io/amis/static/logo_408c434.png"
)
```

`AmisSite` 是整个管理后台的容器，负责管理所有的路由和视图。

### 2. 创建路由

```python
user_router = AmisViewRouter(name="用户管理", type="page")
```

`AmisViewRouter` 用于组织相关的视图，`name` 参数会显示在侧边栏导航中。

### 3. 注册视图

```python
@user_router.register
class UserListView(AmisView):
    page_schema = "用户列表"
    url = "/users"
    page = Page(...)
```

使用装饰器 `@user_router.register` 将视图注册到路由器。每个视图定义一个页面：

- `page_schema`: 页面的描述
- `url`: 页面的访问路径
- `page`: Amis 页面组件

### 4. 定义 API 端点

```python
@app.get("/api/users")
async def get_users():
    return {
        "status": 0,
        "msg": "ok",
        "data": {...}
    }
```

Amis 的 CRUD 组件需要符合特定格式的 API 响应。

## 项目结构建议

随着项目的发展，建议采用以下结构：

```
my-admin-app/
├── app.py              # 主应用文件
├── models/             # 数据模型
│   └── user.py
├── routers/            # 路由定义
│   ├── __init__.py
│   ├── user.py
│   └── dashboard.py
├── views/              # 视图定义
│   ├── __init__.py
│   ├── user.py
│   └── dashboard.py
└── requirements.txt    # 依赖列表
```

## 下一步

恭喜！你已经创建了第一个 FastAPI Amis 应用。接下来你可以：

- [查看更多示例](examples.md) - 学习更多高级用法
- [了解 Amis 组件](../guide/amis-components.md) - 掌握丰富的 UI 组件
- [学习视图和路由](../guide/views-and-routers.md) - 深入理解核心概念

## 常见问题

### 如何修改端口？

在运行命令中指定端口：

```bash
uvicorn app:app --port 3000
```

### 如何启用热重载？

使用 `--reload` 参数：

```bash
uvicorn app:app --reload
```

### API 响应格式要求

Amis 要求 API 返回特定格式：

```json
{
  "status": 0,        // 0 表示成功
  "msg": "ok",        // 消息
  "data": {           // 数据
    "items": [...],   // 列表数据
    "total": 100      // 总数
  }
}
```

