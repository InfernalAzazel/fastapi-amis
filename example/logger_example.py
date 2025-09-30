"""
日志配置示例

演示如何使用 FastAPI-Amis 的日志系统。
"""

from fastapi_amis.core.logger import logger, LogConfig

# 1. 默认配置（自动）
# 导入 logger 时已自动配置为 INFO 级别，输出到控制台
logger.info("这是默认配置的日志")
logger.debug("这条不会显示（级别太低）")


# 2. 自定义配置
LogConfig.setup(
    level="DEBUG",
    log_file="logs/app.log",
    rotation="100 MB",
    retention="7 days",
    colorize=True
)

logger.debug("现在可以看到 DEBUG 日志了")
logger.info("日志同时输出到控制台和文件")


# 3. 接管 FastAPI/Uvicorn 日志
from fastapi import FastAPI
from fastapi_amis.core import AmisSite

app = FastAPI()

# 方式 1：通过 AmisSite 自动接管（推荐）
site = AmisSite(
    title="我的应用",
    intercept_fastapi_logs=True  # 自动接管 FastAPI/Uvicorn 日志
)
site.mount_to_app(app)

# 方式 2：手动接管
# LogConfig.intercept_logging(["uvicorn", "uvicorn.access", "fastapi"])

logger.success("FastAPI 日志已接管到 loguru")


# 4. 运行应用（所有日志都会通过 loguru 输出）
if __name__ == "__main__":
    import uvicorn
    
    # 配置 loguru
    LogConfig.setup(level="INFO", log_file="logs/uvicorn.log")
    
    # 接管 uvicorn 日志（必须在 uvicorn.run 之前）
    LogConfig.intercept_logging()
    
    # 启动服务（关键：log_config=None 禁用 uvicorn 默认日志）
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_config=None  # 禁用 uvicorn 默认日志配置
    )