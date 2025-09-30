from typing import Optional, Any
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging
from fastapi_amis.amis.types import BaseAmisApiOut

logger = logging.getLogger(__name__)

class BaseAmisExceptionCode:
    """
    基础异常代码类
    
    所有自定义异常代码都应继承此类。
    每个异常代码定义为元组：(状态码, 消息, 描述)
    
    Examples:
        >>> class CustomExceptionCode(BaseAmisExceptionCode):
        ...     USER_NOT_FOUND = (2001, "用户不存在", "指定的用户ID不存在")
    """
    pass


class AmisExceptionCode(BaseAmisExceptionCode):
    """预定义的 Amis 异常代码"""
    
    # 通用异常 (1xxx)
    INTERNAL_ERROR = (1000, "服务器内部错误", "发生了意外错误，请稍后重试")
    INVALID_PARAMS = (1001, "参数错误", "请检查请求参数")
    UNAUTHORIZED = (1002, "未授权", "请先登录")
    FORBIDDEN = (1003, "无权限", "您没有权限执行此操作")
    NOT_FOUND = (1004, "资源不存在", "请求的资源未找到")
    
    # 用户相关异常 (2xxx)
    USER_NOT_FOUND = (2001, "用户不存在", "指定的用户ID不存在")
    USER_ALREADY_EXISTS = (2002, "用户已存在", "该用户名或邮箱已被注册")
    USER_PASSWORD_ERROR = (2003, "密码错误", "用户密码不正确")
    USER_DISABLED = (2004, "用户已禁用", "该用户账号已被禁用")
    
    # API 相关异常 (3xxx)
    INVALID_API_KEY = (3001, "无效的 API Key", "请提供有效的 API Key")
    API_RATE_LIMIT = (3002, "请求过于频繁", "请稍后再试")
    
    # 数据相关异常 (4xxx)
    DATA_NOT_FOUND = (4001, "数据不存在", "请求的数据未找到")
    DATA_ALREADY_EXISTS = (4002, "数据已存在", "该数据已存在")
    DATA_VALIDATION_ERROR = (4003, "数据验证失败", "提交的数据格式不正确")


class AmisAPIException(Exception):
    """
    Amis API 异常
    
    使用 BaseAmisApiOut 格式返回错误响应。
    
    Args:
        error_code: 异常代码元组 (status_code, message, description)
        http_status_code: HTTP 状态码，默认 200
        data: 额外的错误数据
        
    Examples:
        >>> raise AmisAPIException(
        ...     error_code=AmisExceptionCode.USER_NOT_FOUND,
        ...     http_status_code=200
        ... )
    """
    
    def __init__(
        self,
        error_code: tuple[int, str, str],
        http_status_code: int = 200,
        data: Optional[Any] = None
    ):
        self.status_code, self.message, self.description = error_code
        self.http_status_code = http_status_code
        self.data = data
        super().__init__(self.message)


class AmisResponseModel(BaseAmisApiOut):
    """
    Amis 响应模型（兼容 BaseAmisApiOut）
    
    用于成功响应，自动设置 status=0。
    
    Attributes:
        status: 状态码，0 表示成功
        msg: 提示信息
        data: 返回数据
        
    Examples:
        >>> return AmisResponseModel(
        ...     data={"user_id": 1},
        ...     msg="操作成功"
        ... )
    """
    ...


async def amis_api_exception_handler(request: Request, exc: AmisAPIException) -> JSONResponse:
    """处理 AmisAPIException"""
    logger.error(
        f"AmisAPIException: {exc.message} (status: {exc.status_code}) at {request.url.path}",
        extra={
            "status_code": exc.status_code,
            "description": exc.description,
            "data": exc.data,
            "path": request.url.path,
            "method": request.method,
        }
    )
    
    return JSONResponse(
        status_code=exc.http_status_code,
        content={
            "status": exc.status_code,
            "msg": exc.message,
            "data": exc.data
        }
    )


async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """处理所有未捕获的异常"""
    logger.error(
        f"Uncaught exception: {type(exc).__name__}: {str(exc)} at {request.url.path}",
        exc_info=True,
        extra={
            "path": request.url.path,
            "method": request.method,
        }
    )
    
    return JSONResponse(
        status_code=500,
        content={
            "status": 1000,
            "msg": "服务器内部错误",
            "data": None
        }
    )


def register_amis_exception_handlers(app: FastAPI) -> None:
    """
    注册 Amis 异常处理器
    
    Args:
        app: FastAPI 应用实例
        
    Examples:
        >>> from fastapi import FastAPI
        >>> app = FastAPI()
        >>> register_amis_exception_handlers(app)
    """
    app.add_exception_handler(AmisAPIException, amis_api_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)
    logger.info("Amis exception handlers registered successfully")