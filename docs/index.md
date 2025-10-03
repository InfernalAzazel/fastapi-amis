# FastAPI Amis

<div align="center">

**基于 FastAPI 和 Amis 的 Python 框架，用于快速构建现代化的管理后台界面**

[![PyPI version](https://badge.fury.io/py/fastapi-amis.svg)](https://pypi.org/project/fastapi-amis/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

</div>

!!! warning "实验性项目"
    目前正在实验中，请不要投入生产项目

## 功能特性

- 🚀 **高性能** - 基于 FastAPI 的高性能 Web 框架
- 🎨 **低代码** - 集成 Amis 低代码前端框架
- 📱 **响应式设计** - 支持多端适配
- 🔧 **灵活组件化** - 灵活的组件化开发
- 📊 **丰富组件** - 内置丰富的表单、表格、图表组件
- 🛠️ **可扩展** - 支持自定义路由和视图

## 环境要求

- Python >= 3.10
- uv (Python 包管理器)
- FastAPI
- Uvicorn

## 快速安装

使用 pip 安装：

```bash
pip install fastapi-amis
```

使用 uv 安装：

```bash
uv pip install fastapi-amis
```

安装开发依赖：

```bash
pip install fastapi-amis[dev]
```

## 快速示例

创建一个简单的管理后台应用：

```python
from fastapi import FastAPI
from fastapi_amis.core.router import AmisViewRouter
from fastapi_amis.core.site import AmisSite
from fastapi_amis.core.views import AmisView
from fastapi_amis.amis.components import Page

# 创建路由器
user_router = AmisViewRouter(name="users", type="page")

# 注册视图
@user_router.register
class UserListView(AmisView):
    page_schema = "用户列表"
    url = "/users"
    page = Page(
        title="用户列表",
        body={"type": "crud", "api": "/api/users"}
    )

# 创建应用
app = FastAPI()
site = AmisSite(title="管理后台")
site.add_router(user_router)
site.mount_to_app(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

访问 http://localhost:8000 查看效果。

## 下一步

- [安装指南](getting-started/installation.md) - 详细的安装说明
- [第一个应用](getting-started/first-app.md) - 创建你的第一个应用
- [示例项目](getting-started/examples.md) - 查看更多示例
- [核心概念](guide/concepts.md) - 了解框架的核心概念

## 参考和感谢

本项目受到了以下优秀项目的启发和影响：

- [FastAPI-Amis-Admin](https://github.com/amisadmin/fastapi-amis-admin) - 感谢 amisadmin 团队提供的宝贵的架构参考和设计思路
- [Amis](https://github.com/baidu/amis) - 感谢百度 Amis 团队提供的优秀前端组件库

## 许可证

本项目采用 [Apache 2.0](https://github.com/InfernalAzazel/fastapi-amis/blob/main/LICENSE) 许可证。
