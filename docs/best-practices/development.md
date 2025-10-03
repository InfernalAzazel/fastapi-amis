# 开发建议

本文档提供 FastAPI Amis 项目的开发最佳实践和建议。

## 代码规范

### Python 代码风格

遵循 PEP 8 和 PEP 257 规范：

```python
# 好的示例
from typing import Optional, List
from fastapi_amis.core.views import AmisView

class UserListView(AmisView):
    """用户列表视图。
    
    展示系统中所有用户的列表，支持搜索和筛选。
    """
    page_schema = "用户列表"
    url = "/users"
    
    def get_page(self, request: Request) -> Page:
        """根据请求动态生成页面。
        
        Args:
            request: FastAPI 请求对象
            
        Returns:
            Page: 页面对象
        """
        return Page(...)
```

### 类型注解

始终使用类型注解：

```python
from typing import List, Optional, Dict, Any

def get_users(
    page: int = 1,
    per_page: int = 10,
    search: Optional[str] = None
) -> Dict[str, Any]:
    """获取用户列表"""
    ...
```

### 命名规范

```python
# 变量和函数：小写下划线
user_name = "张三"
def get_user_list(): ...

# 类：帕斯卡命名
class UserListView: ...

# 常量：大写下划线
MAX_PAGE_SIZE = 100
DEFAULT_PAGE = 1

# 私有属性/方法：前缀下划线
class MyClass:
    def __init__(self):
        self._private_var = "private"
    
    def _private_method(self): ...
```

## API 设计

### RESTful API

遵循 REST 原则：

```python
# 好的 API 设计
GET    /api/users           # 获取用户列表
GET    /api/users/{id}      # 获取单个用户
POST   /api/users           # 创建用户
PUT    /api/users/{id}      # 更新用户
DELETE /api/users/{id}      # 删除用户

# 避免
GET    /api/getUserList
POST   /api/createUser
```

### 统一响应格式

使用 Amis 标准响应格式：

```python
from typing import Any, Optional

def success_response(
    data: Any = None,
    msg: str = "操作成功"
) -> dict:
    """成功响应"""
    return {
        "status": 0,
        "msg": msg,
        "data": data
    }

def error_response(
    msg: str,
    status: int = 1
) -> dict:
    """错误响应"""
    return {
        "status": status,
        "msg": msg,
        "data": None
    }
```

### 分页处理

统一的分页参数和响应：

```python
from fastapi import Query

async def get_users(
    page: int = Query(1, ge=1, description="页码"),
    perPage: int = Query(10, ge=1, le=100, description="每页数量"),
    orderBy: Optional[str] = Query(None, description="排序字段"),
    orderDir: Optional[str] = Query("asc", regex="^(asc|desc)$", description="排序方向")
):
    # 计算偏移量
    offset = (page - 1) * perPage
    
    # 查询数据
    users = await db.get_users(offset=offset, limit=perPage)
    total = await db.count_users()
    
    return {
        "status": 0,
        "msg": "ok",
        "data": {
            "items": users,
            "total": total,
            "page": page,
            "perPage": perPage
        }
    }
```

## 错误处理

### 全局异常处理

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """全局异常处理器"""
    return JSONResponse(
        status_code=500,
        content={
            "status": 1,
            "msg": str(exc),
            "data": None
        }
    )
```

### 业务异常

定义清晰的业务异常：

```python
class BusinessException(Exception):
    """业务异常基类"""
    
    def __init__(self, message: str, code: str = None):
        self.message = message
        self.code = code
        super().__init__(message)

class UserNotFoundException(BusinessException):
    """用户不存在异常"""
    
    def __init__(self, user_id: int):
        super().__init__(
            message=f"用户 {user_id} 不存在",
            code="USER_NOT_FOUND"
        )
```

## 数据验证

### 使用 Pydantic

充分利用 Pydantic 的验证功能：

```python
from pydantic import BaseModel, Field, EmailStr, validator

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=6)
    age: Optional[int] = Field(None, ge=0, le=150)
    
    @validator('username')
    def username_alphanumeric(cls, v):
        """验证用户名只包含字母数字和下划线"""
        if not v.replace('_', '').isalnum():
            raise ValueError('用户名只能包含字母、数字和下划线')
        return v
```

## 性能优化

### 数据库查询优化

```python
# 使用索引
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)  # 添加索引
    username = Column(String, unique=True, index=True)

# 使用预加载避免 N+1 查询
from sqlalchemy.orm import joinedload

users = db.query(User)\
    .options(joinedload(User.profile))\
    .all()

# 只查询需要的字段
users = db.query(User.id, User.username, User.email).all()
```

### 异步处理

对于耗时操作使用异步：

```python
from fastapi import BackgroundTasks

@app.post("/users")
async def create_user(
    user: UserCreate,
    background_tasks: BackgroundTasks
):
    # 创建用户
    db_user = await create_user_in_db(user)
    
    # 后台发送欢迎邮件
    background_tasks.add_task(send_welcome_email, db_user.email)
    
    return success_response(db_user)
```

### 缓存

使用缓存减少数据库查询：

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_user_permissions(user_id: int) -> List[str]:
    """获取用户权限（带缓存）"""
    return db.query(Permission)\
        .join(UserPermission)\
        .filter(UserPermission.user_id == user_id)\
        .all()
```

## 安全最佳实践

### 密码处理

```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """哈希密码"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码"""
    return pwd_context.verify(plain_password, hashed_password)
```

### 认证和授权

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """获取当前用户"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无法验证凭证",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = await get_user(user_id)
    if user is None:
        raise credentials_exception
    
    return user
```

### 输入验证

永远不要信任用户输入：

```python
from pydantic import BaseModel, validator
import re

class UserInput(BaseModel):
    username: str
    
    @validator('username')
    def validate_username(cls, v):
        """验证用户名安全性"""
        # 防止 SQL 注入和 XSS
        if re.search(r'[<>\'"]', v):
            raise ValueError('用户名包含非法字符')
        return v
```

## 测试

### 单元测试

```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_user():
    """测试创建用户"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/api/users",
            json={
                "username": "testuser",
                "email": "test@example.com",
                "password": "password123"
            }
        )
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == 0
    assert "id" in data["data"]
```

### 集成测试

```python
@pytest.mark.asyncio
async def test_user_workflow():
    """测试用户完整流程"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # 创建用户
        response = await ac.post("/api/users", json={...})
        user_id = response.json()["data"]["id"]
        
        # 获取用户
        response = await ac.get(f"/api/users/{user_id}")
        assert response.status_code == 200
        
        # 更新用户
        response = await ac.put(f"/api/users/{user_id}", json={...})
        assert response.status_code == 200
        
        # 删除用户
        response = await ac.delete(f"/api/users/{user_id}")
        assert response.status_code == 200
```

## 日志记录

### 结构化日志

```python
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

def log_operation(
    operation: str,
    user_id: int,
    details: Dict[str, Any] = None
):
    """记录操作日志"""
    logger.info(
        f"Operation: {operation}",
        extra={
            "user_id": user_id,
            "operation": operation,
            "details": details or {}
        }
    )

# 使用
log_operation(
    operation="create_user",
    user_id=request.state.user.id,
    details={"username": "newuser"}
)
```

## 文档

### API 文档

使用 FastAPI 的自动文档功能：

```python
@app.post(
    "/users",
    response_model=UserResponse,
    summary="创建用户",
    description="创建一个新的用户账户",
    responses={
        200: {"description": "创建成功"},
        400: {"description": "请求参数错误"},
        409: {"description": "用户名或邮箱已存在"}
    }
)
async def create_user(user: UserCreate):
    """
    创建新用户。
    
    - **username**: 用户名（3-20个字符）
    - **email**: 邮箱地址
    - **password**: 密码（至少6个字符）
    """
    ...
```

## 下一步

- [项目结构](project-structure.md) - 了解推荐的项目结构
- [示例项目](../getting-started/examples.md) - 查看完整示例
- [API 参考](../api/core.md) - 查看API文档

