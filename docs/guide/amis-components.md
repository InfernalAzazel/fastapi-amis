# Amis 组件

Amis 提供了丰富的 UI 组件，FastAPI Amis 对其进行了封装，使其更易于在 Python 中使用。

## 基础组件

### Page - 页面

页面是最顶层的容器组件：

```python
from fastapi_amis.amis.components import Page

page = Page(
    title="页面标题",
    subTitle="副标题",
    body=[
        # 页面内容
    ]
)
```

**常用属性：**

- `title`: 页面标题
- `subTitle`: 页面副标题  
- `body`: 页面内容（组件或组件列表）
- `toolbar`: 工具栏配置
- `aside`: 侧边栏配置

## 表单组件

### Form - 表单

用于数据输入和提交：

```python
{
    "type": "form",
    "api": "post:/api/users",
    "title": "用户表单",
    "body": [
        {
            "type": "input-text",
            "name": "name",
            "label": "姓名",
            "required": True,
            "placeholder": "请输入姓名"
        },
        {
            "type": "input-email",
            "name": "email",
            "label": "邮箱",
            "required": True
        },
        {
            "type": "input-password",
            "name": "password",
            "label": "密码",
            "required": True
        }
    ]
}
```

### 常用表单字段

#### 文本输入

```python
{
    "type": "input-text",
    "name": "username",
    "label": "用户名",
    "required": True,
    "minLength": 3,
    "maxLength": 20,
    "placeholder": "请输入用户名"
}
```

#### 数字输入

```python
{
    "type": "input-number",
    "name": "age",
    "label": "年龄",
    "min": 0,
    "max": 150
}
```

#### 选择器

```python
{
    "type": "select",
    "name": "role",
    "label": "角色",
    "options": [
        {"label": "管理员", "value": "admin"},
        {"label": "普通用户", "value": "user"}
    ]
}
```

#### 日期选择

```python
{
    "type": "input-date",
    "name": "birthday",
    "label": "生日",
    "format": "YYYY-MM-DD"
}
```

#### 文件上传

```python
{
    "type": "input-file",
    "name": "avatar",
    "label": "头像",
    "accept": "image/*",
    "maxSize": 1024 * 1024 * 2,  # 2MB
    "receiver": "/api/upload"
}
```

## 展示组件

### CRUD - 增删改查

最常用的数据表格组件：

```python
{
    "type": "crud",
    "syncLocation": False,
    "api": "/api/users",
    "columns": [
        {"name": "id", "label": "ID", "type": "text"},
        {"name": "name", "label": "姓名", "type": "text"},
        {"name": "email", "label": "邮箱", "type": "text"},
        {
            "name": "status",
            "label": "状态",
            "type": "status",
            "map": {
                "1": {"label": "正常", "status": "success"},
                "0": {"label": "禁用", "status": "danger"}
            }
        },
        {
            "type": "operation",
            "label": "操作",
            "buttons": [
                {
                    "label": "编辑",
                    "type": "button",
                    "actionType": "dialog",
                    "dialog": {
                        "title": "编辑用户",
                        "body": {
                            "type": "form",
                            "api": "put:/api/users/${id}",
                            "body": [...]
                        }
                    }
                },
                {
                    "label": "删除",
                    "type": "button",
                    "actionType": "ajax",
                    "api": "delete:/api/users/${id}",
                    "confirmText": "确定要删除吗？"
                }
            ]
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
    "footerToolbar": ["statistics", "pagination"]
}
```

### Table - 简单表格

不带增删改查功能的表格：

```python
{
    "type": "table",
    "data": {
        "items": [
            {"name": "张三", "age": 25},
            {"name": "李四", "age": 30}
        ]
    },
    "columns": [
        {"name": "name", "label": "姓名"},
        {"name": "age", "label": "年龄"}
    ]
}
```

### Cards - 卡片列表

以卡片形式展示数据：

```python
{
    "type": "cards",
    "source": "/api/products",
    "card": {
        "header": {
            "title": "${name}",
            "subTitle": "${category}"
        },
        "body": [
            {
                "type": "image",
                "src": "${image}",
                "className": "thumb-lg"
            },
            {
                "type": "tpl",
                "tpl": '<div>价格：¥${price}</div>'
            }
        ],
        "actions": [
            {
                "type": "button",
                "label": "详情",
                "actionType": "link",
                "link": "/products/${id}"
            }
        ]
    }
}
```

## 布局组件

### Grid - 网格布局

创建响应式网格布局：

```python
{
    "type": "grid",
    "columns": [
        {
            "md": 4,
            "body": [
                {
                    "type": "panel",
                    "title": "统计1",
                    "body": "内容1"
                }
            ]
        },
        {
            "md": 4,
            "body": [
                {
                    "type": "panel",
                    "title": "统计2",
                    "body": "内容2"
                }
            ]
        },
        {
            "md": 4,
            "body": [
                {
                    "type": "panel",
                    "title": "统计3",
                    "body": "内容3"
                }
            ]
        }
    ]
}
```

### Panel - 面板

带标题的容器组件：

```python
{
    "type": "panel",
    "title": "面板标题",
    "body": "面板内容",
    "actions": [
        {
            "type": "button",
            "label": "操作按钮"
        }
    ]
}
```

### Tabs - 标签页

创建标签页布局：

```python
{
    "type": "tabs",
    "tabs": [
        {
            "title": "标签1",
            "body": "内容1"
        },
        {
            "title": "标签2",
            "body": "内容2"
        }
    ]
}
```

## 交互组件

### Dialog - 对话框

弹出对话框：

```python
{
    "type": "button",
    "label": "打开对话框",
    "actionType": "dialog",
    "dialog": {
        "title": "对话框标题",
        "body": "对话框内容",
        "actions": [
            {
                "type": "button",
                "label": "确定",
                "actionType": "confirm"
            },
            {
                "type": "button",
                "label": "取消",
                "actionType": "cancel"
            }
        ]
    }
}
```

### Drawer - 抽屉

从侧边滑出的面板：

```python
{
    "type": "button",
    "label": "打开抽屉",
    "actionType": "drawer",
    "drawer": {
        "title": "抽屉标题",
        "body": "抽屉内容"
    }
}
```

## 数据可视化

### Chart - 图表

基于 ECharts 的图表组件：

```python
{
    "type": "chart",
    "api": "/api/stats/chart",
    "config": {
        "title": {
            "text": "销售统计"
        },
        "tooltip": {},
        "xAxis": {
            "type": "category",
            "data": ["一月", "二月", "三月", "四月", "五月", "六月"]
        },
        "yAxis": {
            "type": "value"
        },
        "series": [
            {
                "name": "销售额",
                "type": "line",
                "data": [820, 932, 901, 934, 1290, 1330]
            }
        ]
    }
}
```

## 特殊组件

### Service - 数据服务

用于获取数据并渲染：

```python
{
    "type": "service",
    "api": "/api/user/profile",
    "body": [
        {
            "type": "panel",
            "title": "个人信息",
            "body": [
                {"type": "static", "label": "姓名", "name": "name"},
                {"type": "static", "label": "邮箱", "name": "email"}
            ]
        }
    ]
}
```

### Wizard - 向导

多步骤表单：

```python
{
    "type": "wizard",
    "api": "post:/api/wizard",
    "steps": [
        {
            "title": "第一步",
            "body": [
                {"type": "input-text", "name": "name", "label": "姓名"}
            ]
        },
        {
            "title": "第二步",
            "body": [
                {"type": "input-email", "name": "email", "label": "邮箱"}
            ]
        },
        {
            "title": "完成",
            "body": "提交成功！"
        }
    ]
}
```

## 组件组合示例

### 完整的用户管理页面

```python
Page(
    title="用户管理",
    body=[
        {
            "type": "crud",
            "api": "/api/users",
            "filter": {
                "title": "搜索",
                "body": [
                    {
                        "type": "input-text",
                        "name": "keywords",
                        "placeholder": "搜索姓名或邮箱"
                    },
                    {
                        "type": "select",
                        "name": "status",
                        "label": "状态",
                        "options": [
                            {"label": "全部", "value": ""},
                            {"label": "正常", "value": "1"},
                            {"label": "禁用", "value": "0"}
                        ]
                    }
                ]
            },
            "columns": [
                {"name": "id", "label": "ID", "sortable": True},
                {"name": "name", "label": "姓名", "searchable": True},
                {"name": "email", "label": "邮箱"},
                {
                    "name": "status",
                    "label": "状态",
                    "type": "mapping",
                    "map": {
                        "1": "<span class='label label-success'>正常</span>",
                        "0": "<span class='label label-danger'>禁用</span>"
                    }
                },
                {
                    "name": "created_at",
                    "label": "创建时间",
                    "type": "date",
                    "format": "YYYY-MM-DD HH:mm:ss"
                },
                {
                    "type": "operation",
                    "label": "操作",
                    "buttons": [
                        {
                            "label": "编辑",
                            "type": "button",
                            "level": "link",
                            "actionType": "drawer",
                            "drawer": {
                                "title": "编辑用户",
                                "body": {
                                    "type": "form",
                                    "initApi": "/api/users/${id}",
                                    "api": "put:/api/users/${id}",
                                    "body": [
                                        {
                                            "type": "input-text",
                                            "name": "name",
                                            "label": "姓名",
                                            "required": True
                                        },
                                        {
                                            "type": "input-email",
                                            "name": "email",
                                            "label": "邮箱",
                                            "required": True
                                        },
                                        {
                                            "type": "switch",
                                            "name": "status",
                                            "label": "状态",
                                            "trueValue": 1,
                                            "falseValue": 0
                                        }
                                    ]
                                }
                            }
                        },
                        {
                            "label": "删除",
                            "type": "button",
                            "level": "link",
                            "className": "text-danger",
                            "actionType": "ajax",
                            "api": "delete:/api/users/${id}",
                            "confirmText": "确定要删除该用户吗？"
                        }
                    ]
                }
            ]
        }
    ]
)
```

## 更多资源

- [Amis 官方文档](https://aisuda.bce.baidu.com/amis/zh-CN/docs/index) - 完整的组件文档和示例
- [Amis 可视化编辑器](https://aisuda.github.io/amis-editor-demo/) - 在线编辑器
- [示例项目](examples.md) - 查看更多实际应用示例

## 下一步

- [站点配置](site-configuration.md) - 配置站点外观
- [最佳实践](../best-practices/development.md) - 开发建议

