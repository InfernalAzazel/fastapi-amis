# Amis 组件 API

FastAPI Amis 封装的 Amis 组件 API 参考。

## Page

页面组件，是最顶层的容器。

### 类定义

```python
class Page(BaseComponent):
    type: str = "page"
    title: Optional[str] = None
    subTitle: Optional[str] = None
    body: Union[Dict, List, str, BaseComponent] = []
    toolbar: Optional[List] = None
    aside: Optional[Dict] = None
```

### 参数

- `type` (str): 组件类型，固定为 "page"
- `title` (Optional[str]): 页面标题
- `subTitle` (Optional[str]): 页面副标题
- `body` (Union[Dict, List, str, BaseComponent]): 页面内容
- `toolbar` (Optional[List]): 工具栏配置
- `aside` (Optional[Dict]): 侧边栏配置

### 示例

```python
from fastapi_amis.amis.components import Page

page = Page(
    title="用户管理",
    subTitle="管理系统用户",
    body=[
        {
            "type": "crud",
            "api": "/api/users",
            "columns": [...]
        }
    ]
)
```

## BaseComponent

所有组件的基类。

### 类定义

```python
class BaseComponent(BaseModel):
    type: str
    className: Optional[str] = None
    visible: Optional[bool] = None
    hidden: Optional[bool] = None
    
    class Config:
        extra = "allow"
```

### 参数

- `type` (str): 组件类型
- `className` (Optional[str]): CSS 类名
- `visible` (Optional[bool]): 是否可见
- `hidden` (Optional[bool]): 是否隐藏

## 表单组件

### Form

表单容器组件。

```python
form = {
    "type": "form",
    "title": "表单标题",
    "api": "post:/api/endpoint",
    "body": [
        # 表单字段
    ],
    "actions": [
        {
            "type": "submit",
            "label": "提交"
        },
        {
            "type": "reset",
            "label": "重置"
        }
    ]
}
```

### InputText

文本输入字段。

```python
input_text = {
    "type": "input-text",
    "name": "username",
    "label": "用户名",
    "required": True,
    "minLength": 3,
    "maxLength": 20,
    "placeholder": "请输入用户名",
    "validations": {
        "isAlphanumeric": True
    },
    "validationErrors": {
        "isAlphanumeric": "只能包含字母和数字"
    }
}
```

### Select

选择器字段。

```python
select = {
    "type": "select",
    "name": "role",
    "label": "角色",
    "options": [
        {"label": "管理员", "value": "admin"},
        {"label": "普通用户", "value": "user"}
    ],
    "clearable": True,
    "searchable": True
}
```

## 展示组件

### CRUD

增删改查表格组件。

```python
crud = {
    "type": "crud",
    "api": "/api/users",
    "syncLocation": False,
    "columns": [
        {
            "name": "id",
            "label": "ID",
            "type": "text",
            "sortable": True
        },
        {
            "name": "name",
            "label": "姓名",
            "type": "text",
            "searchable": True
        }
    ],
    "headerToolbar": [
        "bulkActions",
        {
            "type": "button",
            "label": "新增",
            "actionType": "dialog",
            "level": "primary",
            "dialog": {
                "title": "添加用户",
                "body": {
                    "type": "form",
                    "api": "post:/api/users",
                    "body": [...]
                }
            }
        }
    ],
    "footerToolbar": ["statistics", "pagination"],
    "bulkActions": [
        {
            "label": "批量删除",
            "actionType": "ajax",
            "api": "delete:/api/users",
            "confirmText": "确定要删除选中的用户吗？"
        }
    ]
}
```

### Table

简单表格组件。

```python
table = {
    "type": "table",
    "data": {
        "items": [
            {"id": 1, "name": "张三", "age": 25},
            {"id": 2, "name": "李四", "age": 30}
        ]
    },
    "columns": [
        {"name": "id", "label": "ID"},
        {"name": "name", "label": "姓名"},
        {"name": "age", "label": "年龄"}
    ]
}
```

### Cards

卡片列表组件。

```python
cards = {
    "type": "cards",
    "source": "/api/products",
    "placeholder": "暂无数据",
    "card": {
        "header": {
            "title": "${name}",
            "subTitle": "${category}",
            "avatar": "${image}"
        },
        "body": [
            {
                "type": "tpl",
                "tpl": '价格：¥${price}'
            }
        ],
        "actions": [
            {
                "type": "button",
                "label": "查看详情",
                "actionType": "link",
                "link": "/products/${id}"
            }
        ]
    }
}
```

## 布局组件

### Grid

网格布局组件。

```python
grid = {
    "type": "grid",
    "columns": [
        {
            "md": 6,  # 占用 6 列（共 12 列）
            "body": [...]
        },
        {
            "md": 6,
            "body": [...]
        }
    ]
}
```

### Panel

面板组件。

```python
panel = {
    "type": "panel",
    "title": "面板标题",
    "body": "面板内容",
    "className": "panel-info",
    "actions": [
        {
            "type": "button",
            "label": "操作"
        }
    ]
}
```

### Tabs

标签页组件。

```python
tabs = {
    "type": "tabs",
    "tabs": [
        {
            "title": "基本信息",
            "body": [...]
        },
        {
            "title": "详细信息",
            "body": [...]
        }
    ]
}
```

## 交互组件

### Button

按钮组件。

```python
button = {
    "type": "button",
    "label": "按钮",
    "level": "primary",  # primary, secondary, success, danger, warning, info
    "size": "md",  # xs, sm, md, lg
    "actionType": "ajax",  # ajax, link, dialog, drawer, confirm
    "api": "post:/api/action",
    "confirmText": "确定执行此操作吗？"
}
```

### Dialog

对话框组件。

```python
dialog_button = {
    "type": "button",
    "label": "打开对话框",
    "actionType": "dialog",
    "dialog": {
        "title": "对话框标题",
        "size": "lg",  # xs, sm, md, lg, xl, full
        "body": {
            "type": "form",
            "api": "post:/api/submit",
            "body": [...]
        },
        "actions": [
            {
                "type": "button",
                "label": "取消",
                "actionType": "cancel"
            },
            {
                "type": "submit",
                "label": "确定",
                "level": "primary"
            }
        ]
    }
}
```

### Drawer

抽屉组件。

```python
drawer_button = {
    "type": "button",
    "label": "打开抽屉",
    "actionType": "drawer",
    "drawer": {
        "title": "抽屉标题",
        "position": "right",  # left, right, top, bottom
        "size": "md",
        "body": "抽屉内容"
    }
}
```

## 数据组件

### Service

数据服务组件，用于获取数据。

```python
service = {
    "type": "service",
    "api": "/api/data",
    "body": [
        {
            "type": "panel",
            "title": "数据展示",
            "body": "${data}"
        }
    ]
}
```

### Chart

图表组件（基于 ECharts）。

```python
chart = {
    "type": "chart",
    "api": "/api/chart-data",
    "config": {
        "title": {
            "text": "销售统计"
        },
        "tooltip": {},
        "legend": {
            "data": ["销售额"]
        },
        "xAxis": {
            "data": ["一月", "二月", "三月", "四月", "五月", "六月"]
        },
        "yAxis": {},
        "series": [
            {
                "name": "销售额",
                "type": "bar",
                "data": [5, 20, 36, 10, 10, 20]
            }
        ]
    }
}
```

## 工具方法

### dict()

将组件转换为字典。

```python
page = Page(title="测试")
page_dict = page.dict(exclude_none=True)
```

### json()

将组件转换为 JSON 字符串。

```python
page = Page(title="测试")
page_json = page.json(exclude_none=True)
```

## 类型别名

```python
from typing import Union, Dict, List

# 组件类型
ComponentType = Union[Dict, BaseComponent, str]

# 组件列表类型
ComponentList = List[ComponentType]

# 页面内容类型
BodyType = Union[ComponentType, ComponentList]
```

## 下一步

- [扩展功能 API](extensions.md) - 扩展模块 API
- [核心模块 API](core.md) - 核心模块 API
- [Amis 官方文档](https://aisuda.bce.baidu.com/amis/zh-CN/components/page) - 完整的组件文档

