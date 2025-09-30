from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi_amis.extensions.exception import (
    AmisAPIException,
    AmisExceptionCode,
    AmisResponseModel,
    register_amis_exception_handlers,
)

# 默认已自动配置日志（INFO 级别，控制台输出）
# 如需自定义，使用：
# from fastapi_amis.core import LogConfig, configure_logging
# configure_logging({"level": "DEBUG", "log_file": "logs/app.log"})
# LogConfig.intercept_logging()  # 接管 FastAPI/Uvicorn 日志

app = FastAPI()

# 1. 注册异常处理器
register_amis_exception_handlers(app)

# 自定义状态码映射示例：
# custom_map = {400: 1001, 401: 2000, 403: 2001, 404: 3000}
# register_amis_exception_handlers(app, status_map=custom_map)


# 2. 定义数据模型
class User(BaseModel):
    id: int
    name: str


# 3. 成功响应示例
@app.get("/success", response_model=AmisResponseModel[User])
async def success():
    return AmisResponseModel(
        data=User(id=1, name="张三"),
        msg="操作成功"
    )
    # 返回: {"status": 0, "msg": "操作成功", "data": {"id": 1, "name": "张三"}}


# 4. 抛出异常示例
@app.get("/error")
async def error():
    raise AmisAPIException(error_code=AmisExceptionCode.USER_NOT_FOUND)
    # 返回: {"status": 2001, "msg": "用户不存在", "data": null}


# 5. 未捕获异常自动处理
@app.get("/uncaught")
async def uncaught():
    _ = 1 / 0  # 会被全局异常处理器捕获
    # 返回: {"status": 1000, "msg": "服务器内部错误", "data": null}


# 6. FastAPI HTTPException 自动处理
@app.get("/http-error")
async def http_error():
    raise HTTPException(status_code=404, detail="资源未找到")
    # 返回: {"status": 1004, "msg": "资源未找到", "data": null}


# 7. Pydantic 验证错误自动处理
@app.get("/validation-error")
async def validation_error(age: int):
    return {"age": age}
    # 访问 /validation-error?age=abc 会返回:
    # {"status": 1001, "msg": "参数验证失败", "data": {"errors": [...]}}


# 8. 自定义异常代码
class OrderExceptionCode(AmisExceptionCode):
    ORDER_NOT_FOUND = (5001, "订单不存在", "指定的订单ID不存在")
    PAYMENT_FAILED = (5002, "支付失败", "支付处理时发生错误")


@app.get("/order/{order_id}")
async def get_order(order_id: int):
    if order_id == 999:
        raise AmisAPIException(error_code=OrderExceptionCode.ORDER_NOT_FOUND)
    return AmisResponseModel(data={"order_id": order_id}, msg="获取成功")


if __name__ == "__main__":
    import uvicorn
    from fastapi_amis.core import LogConfig
    
    # 在启动前接管日志
    LogConfig.intercept_logging()
    
    # 使用 log_config=None 禁用 uvicorn 默认日志配置
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        log_config=None  # 关键：禁用 uvicorn 默认日志配置
    )