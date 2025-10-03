# 扩展功能 API

FastAPI Amis 扩展模块的 API 参考文档。

## 异常处理

### AmisException

框架的基础异常类。

```python
class AmisException(Exception):
    """Amis 框架基础异常"""
    
    def __init__(
        self,
        message: str,
        status_code: int = 400,
        error_code: Optional[str] = None,
        **extra
    ):
        """
        Args:
            message: 错误消息
            status_code: HTTP 状态码
            error_code: 业务错误码
            **extra: 额外的错误信息
        """
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.extra = extra
        super().__init__(message)
```

**示例：**

```python
from fastapi_amis.extensions.exception import AmisException

# 抛出异常
raise AmisException(
    message="用户不存在",
    status_code=404,
    error_code="USER_NOT_FOUND"
)
```

### 异常处理器

注册全局异常处理器：

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi_amis.extensions.exception import AmisException

app = FastAPI()

@app.exception_handler(AmisException)
async def amis_exception_handler(request, exc: AmisException):
    """处理 Amis 异常"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": 1,
            "msg": exc.message,
            "code": exc.error_code,
            **exc.extra
        }
    )
```

## 管理扩展

### AdminExt

管理后台扩展基类。

```python
class AdminExt:
    """管理后台扩展基类"""
    
    def __init__(self, site: AmisSite):
        self.site = site
    
    def register(self) -> None:
        """注册扩展"""
        raise NotImplementedError
```

**使用示例：**

```python
from fastapi_amis.extensions.admin import AdminExt

class UserAdminExt(AdminExt):
    """用户管理扩展"""
    
    def register(self):
        """注册用户管理相关视图"""
        router = AmisViewRouter(name="用户管理")
        
        @router.register
        class UserListView(AmisView):
            ...
        
        self.site.add_router(router)

# 使用扩展
site = AmisSite()
user_ext = UserAdminExt(site)
user_ext.register()
```

## 日志功能

### setup_logging

配置日志系统。

```python
def setup_logging(
    level: str = "INFO",
    log_file: Optional[str] = None,
    format_string: Optional[str] = None
) -> None:
    """
    配置日志系统
    
    Args:
        level: 日志级别 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: 日志文件路径
        format_string: 日志格式字符串
    """
```

**示例：**

```python
from fastapi_amis.extensions.logging import setup_logging

# 基础配置
setup_logging(level="INFO")

# 输出到文件
setup_logging(
    level="DEBUG",
    log_file="app.log"
)

# 自定义格式
setup_logging(
    level="INFO",
    format_string="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

### get_logger

获取日志记录器。

```python
def get_logger(name: str) -> logging.Logger:
    """
    获取日志记录器
    
    Args:
        name: 记录器名称
    
    Returns:
        logging.Logger: 日志记录器实例
    """
```

**示例：**

```python
from fastapi_amis.extensions.logging import get_logger

logger = get_logger(__name__)

logger.debug("调试信息")
logger.info("普通信息")
logger.warning("警告信息")
logger.error("错误信息")
logger.critical("严重错误")
```

## 中间件

### AmisMiddleware

Amis 框架中间件。

```python
class AmisMiddleware:
    """Amis 中间件"""
    
    def __init__(
        self,
        app: ASGIApp,
        *,
        cors_origins: List[str] = None,
        request_id_header: str = "X-Request-ID"
    ):
        """
        Args:
            app: ASGI 应用
            cors_origins: CORS 允许的源
            request_id_header: 请求 ID 头名称
        """
```

**示例：**

```python
from fastapi import FastAPI
from fastapi_amis.extensions.middleware import AmisMiddleware

app = FastAPI()

app.add_middleware(
    AmisMiddleware,
    cors_origins=["http://localhost:3000"],
    request_id_header="X-Request-ID"
)
```

## 工具函数

### generate_schema

生成 Amis Schema。

```python
def generate_schema(
    component: BaseComponent,
    *,
    exclude_none: bool = True
) -> Dict:
    """
    生成 Amis Schema
    
    Args:
        component: Amis 组件
        exclude_none: 是否排除 None 值
    
    Returns:
        Dict: Amis Schema 字典
    """
```

**示例：**

```python
from fastapi_amis.amis.components import Page
from fastapi_amis.extensions.utils import generate_schema

page = Page(title="测试页面")
schema = generate_schema(page)
```

### validate_amis_response

验证 Amis API 响应格式。

```python
def validate_amis_response(
    response: Dict,
    *,
    strict: bool = False
) -> bool:
    """
    验证 Amis API 响应格式
    
    Args:
        response: 响应数据
        strict: 是否严格验证
    
    Returns:
        bool: 是否有效
    
    Raises:
        ValueError: 响应格式无效时抛出
    """
```

**示例：**

```python
from fastapi_amis.extensions.utils import validate_amis_response

response = {
    "status": 0,
    "msg": "ok",
    "data": {...}
}

is_valid = validate_amis_response(response)
```

### create_amis_response

创建标准的 Amis API 响应。

```python
def create_amis_response(
    data: Any = None,
    *,
    status: int = 0,
    msg: str = "ok",
    **extra
) -> Dict:
    """
    创建 Amis API 响应
    
    Args:
        data: 响应数据
        status: 状态码 (0=成功, 非0=失败)
        msg: 消息
        **extra: 额外的响应字段
    
    Returns:
        Dict: Amis 响应字典
    """
```

**示例：**

```python
from fastapi_amis.extensions.utils import create_amis_response

# 成功响应
response = create_amis_response(
    data={"items": [...], "total": 100}
)

# 失败响应
error_response = create_amis_response(
    status=1,
    msg="操作失败",
    data=None
)
```

## 装饰器

### amis_api

API 响应装饰器，自动转换为 Amis 格式。

```python
def amis_api(
    *,
    success_msg: str = "操作成功",
    error_msg: str = "操作失败"
):
    """
    Amis API 装饰器
    
    Args:
        success_msg: 成功消息
        error_msg: 失败消息
    """
```

**示例：**

```python
from fastapi import APIRouter
from fastapi_amis.extensions.decorators import amis_api

router = APIRouter()

@router.get("/users")
@amis_api(success_msg="获取用户列表成功")
async def get_users():
    users = await db.get_users()
    return {"items": users, "total": len(users)}
```

### require_permissions

权限检查装饰器。

```python
def require_permissions(
    *permissions: str,
    check_all: bool = True
):
    """
    权限检查装饰器
    
    Args:
        *permissions: 需要的权限列表
        check_all: 是否需要所有权限（True）还是任一权限（False）
    """
```

**示例：**

```python
from fastapi_amis.extensions.decorators import require_permissions

@router.get("/admin/users")
@require_permissions("user.read", "admin.access", check_all=True)
async def get_admin_users():
    return await db.get_all_users()
```

## 类型定义

### AmisResponse

Amis API 响应类型。

```python
from typing import TypedDict, Any, Optional

class AmisResponse(TypedDict):
    status: int
    msg: str
    data: Optional[Any]
```

### PageData

分页数据类型。

```python
class PageData(TypedDict):
    items: List[Any]
    total: int
    page: Optional[int]
    perPage: Optional[int]
```

## 下一步

- [核心模块 API](core.md) - 核心模块 API 参考
- [Amis 组件 API](components.md) - 组件 API 参考
- [使用指南](../guide/concepts.md) - 深入了解概念

