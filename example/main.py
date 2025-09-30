from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi_amis.amis.components import App, PageSchema, Page, Grid, Container, Card, Button, Tpl, Form, InputText, InputNumber, Select, Checkboxes, Table


app = FastAPI()


def get_app_config():
    """获取应用配置"""
    amis_app = App()
    amis_app.type = 'app'
    amis_app.brandName = "FastAPI Amis 多页面示例"
    amis_app.logo = "https://suda.cdn.bcebos.com/images%2F2021-01%2Fdiamond.svg"

    # 设置页面列表
    amis_app.pages = [
        PageSchema(
            children=[
                PageSchema(
                    label="卡片页面",
                    icon="fa fa-th-large",
                    url="/cards",
                    schema=Page(
                        title="信息卡片展示",
                        body=Grid(
                            columns=[
                                Card(
                                    header={
                                        "title": "系统信息",
                                        "subTitle": "当前系统状态"
                                    },
                                    body={
                                        "type": "property",
                                        "items": [
                                            {"label": "系统版本", "content": "FastAPI Amis v1.0"},
                                            {"label": "运行时间", "content": "2天3小时"},
                                            {"label": "内存使用", "content": "45%"},
                                            {"label": "CPU使用", "content": "12%"}
                                        ]
                                    }
                                ),
                                Card(
                                    header={
                                        "title": "用户统计",
                                        "subTitle": "用户数据概览"
                                    },
                                    body={
                                        "type": "property",
                                        "items": [
                                            {"label": "总用户数", "content": "1,234"},
                                            {"label": "活跃用户", "content": "856"},
                                            {"label": "新增用户", "content": "23"},
                                            {"label": "在线用户", "content": "67"}
                                        ]
                                    }
                                ),
                                Card(
                                    header={
                                        "title": "快速操作",
                                        "subTitle": "常用功能入口"
                                    },
                                    body=Grid(
                                        columns=[
                                            {
                                                "body": Button(
                                                    label="添加用户",
                                                    level="primary",
                                                    size="sm"
                                                )
                                            },
                                            {
                                                "body": Button(
                                                    label="导出数据",
                                                    level="success",
                                                    size="sm"
                                                )
                                            }
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                )
            ]
        ),
    ]
    
    return amis_app

def get_page_config2():
    """获取应用配置"""
    amis_page = Page()
    amis_page.type = 'page'
    amis_page.title = "FastAPI Amis 页面示例"
    amis_page.logo = "https://suda.cdn.bcebos.com/images%2F2021-01%2Fdiamond.svg"
    


    # 设置页面列表
    amis_page.body = "Hello World!"
    
    return amis_page


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """首页"""
    amis_app = get_page_config2()
    return HTMLResponse(content=amis_app.render())


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)

# uvicorn example.main:app --host 0.0.0.0 --port 3000 --reload