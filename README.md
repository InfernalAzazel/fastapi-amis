# FastAPI Amis

FastAPI Amis 是一个基于 FastAPI 和 Amis 的 Python 框架，用于快速构建现代化的管理后台界面。

> 目前正在实验中请不要投入生产项目

## 功能特性

- 🚀 基于 FastAPI 的高性能 Web 框架
- 🎨 集成 Amis 低代码前端框架
- 📱 响应式设计，支持多端适配
- 🔧 灵活的组件化开发
- 📊 内置丰富的表单、表格、图表组件
- 🛠️ 支持自定义路由和视图

## 环境要求

- Python >= 3.10
- uv (Python 包管理器)
- FastAPI
- Uvicorn

## 安装

1. 克隆项目：
```bash
git clone https://github.com/InfernalAzazel/fastapi-amis.git

cd fastapi-amis
```

2. 安装 uv（如果尚未安装）：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. 安装依赖：
```bash
uv sync
```

这将自动创建虚拟环境并安装所有依赖。

## 运行示例

项目提供了两个示例，展示不同的使用方式：

### 示例 1：完整管理后台 (simple_example.py)
```bash
cd example
uv run python simple_example.py
```
访问：http://localhost:4000

### 示例 2：简单多页面应用 (main.py)
```bash
cd example
uv run python main.py
```
访问：http://localhost:3000

### 使用 uvicorn 运行（可选）
```bash
cd example
uv run uvicorn simple_example:create_app --host 0.0.0.0 --port 4000 --reload
# 或
uv run uvicorn main:app --host 0.0.0.0 --port 3000 --reload
```

## 项目结构

```
fastapi-amis/
├── fastapi_amis/           # 核心框架代码
│   ├── amis/              # Amis 组件定义
│   │   ├── components.py  # 组件类定义
│   │   ├── constants.py   # 常量定义
│   │   ├── types.py       # 类型定义
│   │   └── templates/     # Jinja2 模板
│   ├── core/              # 核心功能
│   │   ├── router.py      # 路由管理
│   │   ├── site.py        # 站点管理
│   │   └── views.py       # 视图基类
│   └── extensions/        # 扩展功能
└── example/               # 示例代码
    ├── main.py           # 多页面示例
    └── simple_example.py # 简单示例
```

## 快速开始

1. **导入必要的模块：**
```python
from fastapi import FastAPI
from fastapi_amis.core.router import AmisViewRouter
from fastapi_amis.core.site import AmisSite
from fastapi_amis.core.views import AmisView
from fastapi_amis.amis.components import Page
```

2. **创建路由器和视图：**
```python
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
```

3. **创建应用并挂载站点：**
```python
app = FastAPI()
site = AmisSite(title="管理后台")
site.add_router(user_router)
site.mount_to_app(app)
```

## 开发说明

- 项目使用 Python 3.10+ 开发
- 使用 uv 作为包管理器和虚拟环境管理工具
- 遵循 FastAPI 最佳实践
- 支持异步编程
- 使用 Pydantic 进行数据验证
- 集成 Amis 前端框架

### 开发环境设置

1. 确保已安装 uv：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. 安装开发依赖：
```bash
uv sync --dev
```

3. 激活虚拟环境：
```bash
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows
```

## 参考和感谢

本项目受到了以下优秀项目的启发和影响：

### 特别感谢

感谢 [amisadmin](https://github.com/amisadmin) 团队开发的 FastAPI-Amis-Admin 项目，为我们提供了宝贵的架构参考和设计思路。

感谢百度 [Amis](https://github.com/baidu/amis.git) 团队提供的优秀前端组件库，让后端开发者也能轻松构建现代化的管理界面。

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。