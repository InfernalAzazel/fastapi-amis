# 项目结构

良好的项目结构有助于代码的维护和扩展。

## 推荐结构

```
my-admin-project/
├── app/
│   ├── __init__.py
│   ├── main.py              # 应用入口
│   ├── config.py            # 配置文件
│   ├── models/              # 数据模型
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── product.py
│   ├── schemas/             # Pydantic 模式
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── product.py
│   ├── api/                 # API 路由
│   │   ├── __init__.py
│   │   ├── deps.py          # 依赖项
│   │   ├── users.py
│   │   └── products.py
│   ├── admin/               # 管理后台
│   │   ├── __init__.py
│   │   ├── site.py          # 站点配置
│   │   ├── routers/         # 管理路由
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   └── product.py
│   │   └── views/           # 管理视图
│   │       ├── __init__.py
│   │       ├── user.py
│   │       └── product.py
│   ├── core/                # 核心功能
│   │   ├── __init__.py
│   │   ├── security.py      # 安全相关
│   │   └── database.py      # 数据库连接
│   └── utils/               # 工具函数
│       ├── __init__.py
│       └── helpers.py
├── tests/                   # 测试文件
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_api/
│   └── test_admin/
├── alembic/                 # 数据库迁移
│   └── versions/
├── static/                  # 静态文件
├── templates/               # 模板文件
├── .env                     # 环境变量
├── .env.example             # 环境变量示例
├── pyproject.toml           # 项目配置
├── README.md                # 项目说明
└── requirements.txt         # 依赖列表（可选）
```

## 文件说明

### app/main.py

应用入口文件：

```python
from fastapi import FastAPI
from app.admin.site import create_admin_site
from app.api import users, products
from app.config import settings

app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION
)

# 注册 API 路由
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(products.router, prefix="/api/products", tags=["products"])

# 挂载管理后台
admin_site = create_admin_site()
admin_site.mount_to_app(app, prefix="/admin")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
```

### app/config.py

配置管理：

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_TITLE: str = "管理系统"
    APP_VERSION: str = "1.0.0"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = False
    
    # 数据库配置
    DATABASE_URL: str
    
    # 安全配置
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"

settings = Settings()
```

### app/models/user.py

数据模型：

```python
from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
```

### app/schemas/user.py

Pydantic 模式：

```python
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDB(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    
    class Config:
        from_attributes = True
```

### app/api/users.py

API 路由：

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate, UserInDB
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=dict)
async def get_users(
    page: int = 1,
    perPage: int = 10,
    db: Session = Depends(get_db)
):
    users = db.query(User).offset((page - 1) * perPage).limit(perPage).all()
    total = db.query(User).count()
    
    return {
        "status": 0,
        "msg": "ok",
        "data": {
            "items": users,
            "total": total
        }
    }

@router.post("/", response_model=dict)
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return {
        "status": 0,
        "msg": "创建成功",
        "data": db_user
    }
```

### app/admin/site.py

管理站点配置：

```python
from fastapi_amis.core.site import AmisSite
from app.admin.routers.user import user_router
from app.admin.routers.product import product_router

def create_admin_site() -> AmisSite:
    site = AmisSite(
        title="管理后台",
        logo="https://example.com/logo.png"
    )
    
    # 注册路由
    site.add_router(user_router)
    site.add_router(product_router)
    
    return site
```

### app/admin/routers/user.py

管理路由：

```python
from fastapi_amis.core.router import AmisViewRouter
from app.admin.views.user import UserListView, UserFormView

user_router = AmisViewRouter(
    name="用户管理",
    icon="fa fa-users"
)

# 注册视图
user_router.register(UserListView)
user_router.register(UserFormView)
```

### app/admin/views/user.py

管理视图：

```python
from fastapi_amis.core.views import AmisView
from fastapi_amis.amis.components import Page

class UserListView(AmisView):
    page_schema = "用户列表"
    url = "/users"
    
    page = Page(
        title="用户管理",
        body={
            "type": "crud",
            "api": "/api/users",
            "columns": [
                {"name": "id", "label": "ID"},
                {"name": "username", "label": "用户名"},
                {"name": "email", "label": "邮箱"},
            ]
        }
    )

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
                    "name": "username",
                    "label": "用户名",
                    "required": True
                },
                {
                    "type": "input-email",
                    "name": "email",
                    "label": "邮箱",
                    "required": True
                }
            ]
        }
    )
```

## 模块化组织

### 按功能模块分组

```
app/
├── modules/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── api.py
│   │   └── admin.py
│   ├── users/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── api.py
│   │   └── admin.py
│   └── products/
│       ├── __init__.py
│       ├── models.py
│       ├── schemas.py
│       ├── api.py
│       └── admin.py
```

### 按层次分组

```
app/
├── domain/          # 领域模型
├── application/     # 应用服务
├── infrastructure/  # 基础设施
└── presentation/    # 表现层
    ├── api/
    └── admin/
```

## 配置文件组织

### 多环境配置

```
app/
├── config/
│   ├── __init__.py
│   ├── base.py       # 基础配置
│   ├── development.py # 开发环境
│   ├── production.py  # 生产环境
│   └── testing.py     # 测试环境
```

## 下一步

- [开发建议](development.md) - 开发最佳实践
- [示例项目](../getting-started/examples.md) - 查看实际项目

