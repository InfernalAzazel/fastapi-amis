from typing import Optional, Any, Dict
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException, RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi_amis.amis.types import BaseAmisApiOut
from fastapi_amis.core.logger import logger


def _log_exception(level: str, msg: str, request: Request, **extra) -> None:
    """统一的异常日志记录"""
    log_msg = f"{msg} at {request.url.path}"
    log_data = {"path": request.url.path, "method": request.method, **extra}
    getattr(logger, level)(log_msg, **log_data)


def _amis_response(status: int, msg: str, data: Any = None, http_code: int = 200) -> JSONResponse:
    """创建 Amis 格式响应"""
    return JSONResponse(
        status_code=http_code,
        content={"status": status, "msg": msg, "data": data}
    )


class AmisExceptionCode:
    """
    基础异常代码类
    
    所有自定义异常代码都应继承此类。
    每个异常代码定义为元组：(状态码, 消息, 描述)
    
    Examples:
        >>> class AmisExceptionCode:
        ...     USER_NOT_FOUND = (2001, "用户不存在", "指定的用户ID不存在")
    """
    pass


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
    _log_exception(
        "error",
        f"AmisAPIException: {exc.message} (status: {exc.status_code})",
        request,
        status_code=exc.status_code,
        description=exc.description,
        data=exc.data
    )
    return _amis_response(exc.status_code, exc.message, exc.data, exc.http_status_code)


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """处理 Pydantic 验证错误"""
    errors = exc.errors()
    _log_exception("warning", "Validation error", request, errors=errors)
    return _amis_response(1001, "参数验证失败", {"errors": errors})


async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """处理所有未捕获的异常"""
    logger.opt(exception=True).error(
        f"Uncaught exception: {type(exc).__name__}: {str(exc)} at {request.url.path}",
        path=request.url.path,
        method=request.method
    )
    return _amis_response(1000, "服务器内部错误", http_code=500)


def _create_http_exception_handler(status_map: Optional[Dict[int, int]]):
    """创建 HTTP 异常处理器"""
    async def handler(request: Request, exc: HTTPException) -> JSONResponse:
        """处理 FastAPI HTTPException"""
        _log_exception(
            "warning",
            f"HTTPException: {exc.detail} (status_code: {exc.status_code})",
            request,
            status_code=exc.status_code,
            detail=exc.detail
        )
        amis_status = (status_map or {}).get(exc.status_code, exc.status_code)
        return _amis_response(amis_status, str(exc.detail), http_code=exc.status_code)
    return handler


def register_amis_exception_handlers(
    app: FastAPI,
    status_map: Optional[Dict[int, int]] = None,
) -> None:
    """
    注册 Amis 异常处理器
    
    捕获所有异常类型：
    - AmisAPIException: 自定义业务异常
    - HTTPException: FastAPI HTTP 异常
    - RequestValidationError: Pydantic 验证错误
    - StarletteHTTPException: Starlette HTTP 异常
    - Exception: 所有其他未捕获的异常
    
    Args:
        app: FastAPI 应用实例
        status_map: HTTP 状态码到 Amis 状态码的映射
        
    Examples:
        >>> from fastapi import FastAPI
        >>> app = FastAPI()
        >>> 
        >>> # 使用默认配置
        >>> register_amis_exception_handlers(app)
        >>> 
        >>> # 自定义状态码映射
        >>> custom_map = {400: 1001, 401: 1002, 404: 2001}
        >>> register_amis_exception_handlers(app, status_map=custom_map)
    """
    http_handler = _create_http_exception_handler(status_map)
    
    handlers = [
        (AmisAPIException, amis_api_exception_handler),
        (RequestValidationError, validation_exception_handler),
        (HTTPException, http_handler),
        (StarletteHTTPException, http_handler),
        (Exception, global_exception_handler),
    ]
    
    for exc_class, handler in handlers:
        app.add_exception_handler(exc_class, handler)
    
    logger.info("Amis exception handlers registered successfully")