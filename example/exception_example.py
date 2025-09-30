from fastapi import FastAPI
from pydantic import BaseModel
from fastapi_amis.extensions.exception import (
    AmisAPIException,
    AmisExceptionCode,
    AmisResponseModel,
    BaseAmisExceptionCode,
    register_amis_exception_handlers,
)

app = FastAPI()

# 1. 注册异常处理器
register_amis_exception_handlers(app)


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


# 6. 自定义异常代码
class OrderExceptionCode(BaseAmisExceptionCode):
    ORDER_NOT_FOUND = (5001, "订单不存在", "指定的订单ID不存在")
    PAYMENT_FAILED = (5002, "支付失败", "支付处理时发生错误")


@app.get("/order/{order_id}")
async def get_order(order_id: int):
    if order_id == 999:
        raise AmisAPIException(error_code=OrderExceptionCode.ORDER_NOT_FOUND)
    return AmisResponseModel(data={"order_id": order_id}, msg="获取成功")


# 7. 预定义异常代码列表
"""
通用异常 (1xxx):
- INTERNAL_ERROR = (1000, "服务器内部错误", "...")
- INVALID_PARAMS = (1001, "参数错误", "...")
- UNAUTHORIZED = (1002, "未授权", "...")
- FORBIDDEN = (1003, "无权限", "...")
- NOT_FOUND = (1004, "资源不存在", "...")

用户异常 (2xxx):
- USER_NOT_FOUND = (2001, "用户不存在", "...")
- USER_ALREADY_EXISTS = (2002, "用户已存在", "...")
- USER_PASSWORD_ERROR = (2003, "密码错误", "...")
- USER_DISABLED = (2004, "用户已禁用", "...")

API 异常 (3xxx):
- INVALID_API_KEY = (3001, "无效的 API Key", "...")
- API_RATE_LIMIT = (3002, "请求过于频繁", "...")

数据异常 (4xxx):
- DATA_NOT_FOUND = (4001, "数据不存在", "...")
- DATA_ALREADY_EXISTS = (4002, "数据已存在", "...")
- DATA_VALIDATION_ERROR = (4003, "数据验证失败", "...")
"""


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)