from fastapi import FastAPI
from fastapi_amis.core.router import AmisViewRouter
from fastapi_amis.core.site import AmisSite
from fastapi_amis.core.views import AmisView
from fastapi_amis.amis.components import Page

# 创建路由器
user_router = AmisViewRouter(name="a", type="app")
system_router = AmisViewRouter(name="a", type="app")
auth_router = AmisViewRouter(name="auth", type="page")

# 用户视图
@user_router.register
class UserListView(AmisView):
    page_schema = "用户列表"
    url = "/users"
    icon = "fa fa-user"
    page = Page(
        title="用户列表",
        body={
            "type": "crud",
            "api": "/api/users",
            "columns": [
                {"name": "id", "label": "ID", "width": 80, "sortable": True},
                {"name": "username", "label": "用户名", "width": 120, "searchable": True},
                {"name": "email", "label": "邮箱", "width": 200, "searchable": True},
                {"name": "role", "label": "角色", "width": 100},
                {"name": "status", "label": "状态", "width": 100, "type": "status"},
                {"name": "created_at", "label": "创建时间", "width": 150, "type": "datetime"}
            ],
            "headerToolbar": [
                {"type": "tpl", "tpl": "用户管理", "className": "v-middle"},
                {"type": "flex", "justify": "end", "items": [
                    {"type": "button", "actionType": "dialog", "label": "新增用户", "level": "primary", "dialog": {
                        "title": "新增用户",
                        "body": {"type": "form", "api": "/api/users", "body": [
                            {"type": "input-text", "name": "username", "label": "用户名", "required": True},
                            {"type": "input-email", "name": "email", "label": "邮箱", "required": True},
                            {"type": "input-password", "name": "password", "label": "密码", "required": True},
                            {"type": "select", "name": "role", "label": "角色", "options": [
                                {"label": "管理员", "value": "admin"},
                                {"label": "用户", "value": "user"}
                            ]}
                        ]}
                    }}
                ]}
            ]
        }
    )

@user_router.register  
class UserCreateView(AmisView):
    page_schema = "创建用户"
    url = "/users/create"
    icon = "fa fa-user"
    page = Page(
        title="创建用户",
        body={
            "type": "form",
            "api": "/api/users",
            "mode": "horizontal",
            "body": [
                {"type": "input-text", "name": "username", "label": "用户名", "required": True, "placeholder": "请输入用户名"},
                {"type": "input-email", "name": "email", "label": "邮箱", "required": True, "placeholder": "请输入邮箱"},
                {"type": "input-password", "name": "password", "label": "密码", "required": True, "placeholder": "请输入密码"},
                {"type": "input-password", "name": "confirm_password", "label": "确认密码", "required": True},
                {"type": "select", "name": "role", "label": "角色", "required": True, "options": [
                    {"label": "管理员", "value": "admin"},
                    {"label": "普通用户", "value": "user"},
                    {"label": "访客", "value": "guest"}
                ]},
                {"type": "switch", "name": "is_active", "label": "启用状态", "value": True},
                {"type": "textarea", "name": "description", "label": "备注", "placeholder": "请输入用户备注信息"}
            ],
            "actions": [
                {"type": "submit", "label": "提交", "level": "primary"},
                {"type": "reset", "label": "重置"}
            ]
        }
    )

# 系统视图
@system_router.register
class SystemInfoView(AmisView):
    page_schema = "系统信息"
    url = "/system/info"
    icon = "fa fa-server"
    page = Page(
        title="系统信息",
        body={
            "type": "property",
            "title": "系统状态",
            "items": [
                {"label": "系统版本", "content": "FastAPI Amis Admin v1.0.0"},
                {"label": "Python版本", "content": "Python 3.9+"},
                {"label": "运行时间", "content": "7天12小时"},
                {"label": "内存使用", "content": "512MB / 2GB (25.6%)"},
                {"label": "CPU使用", "content": "23.5%"},
                {"label": "磁盘使用", "content": "15.2GB / 100GB (15.2%)"},
                {"label": "网络状态", "content": "正常"},
                {"label": "数据库连接", "content": "已连接"}
            ]
        }
    )

@system_router.register
class SystemSettingsView(AmisView):
    page_schema = "系统设置"
    url = "/system/settings"
    icon = "fa fa-cog"
    page = Page(
        title="系统设置",
        body={
            "type": "form",
            "api": "/api/system/settings",
            "mode": "horizontal",
            "body": [
                {"type": "input-text", "name": "site_name", "label": "站点名称", "value": "FastAPI Amis Admin", "required": True},
                {"type": "input-email", "name": "admin_email", "label": "管理员邮箱", "value": "admin@example.com"},
                {"type": "input-url", "name": "site_url", "label": "站点地址", "value": "https://example.com"},
                {"type": "switch", "name": "debug_mode", "label": "调试模式", "value": False},
                {"type": "input-number", "name": "session_timeout", "label": "会话超时(分钟)", "value": 30, "min": 5, "max": 1440},
                {"type": "input-number", "name": "max_upload_size", "label": "最大上传大小(MB)", "value": 10, "min": 1, "max": 100},
                {"type": "select", "name": "timezone", "label": "时区", "value": "Asia/Shanghai", "options": [
                    {"label": "北京时间", "value": "Asia/Shanghai"},
                    {"label": "UTC", "value": "UTC"},
                    {"label": "纽约时间", "value": "America/New_York"}
                ]},
                {"type": "textarea", "name": "description", "label": "站点描述", "placeholder": "请输入站点描述"}
            ],
            "actions": [
                {"type": "submit", "label": "保存设置", "level": "primary"},
                {"type": "button", "label": "重置", "actionType": "reset"}
            ]
        }
    )

# 认证视图
@auth_router.register
class LoginView(AmisView):
    page_schema = "用户登录"
    url = "/login"
    page = Page(
        title="用户登录",
        body={
            "type": "form",
            "api": "/api/auth/login",
            "mode": "horizontal",
            "wrapWithPanel": True,
            "panelClassName": "login-panel",
            "body": [
                {
                    "type": "input-text",
                    "name": "username",
                    "label": "用户名",
                    "required": True,
                    "placeholder": "请输入用户名",
                    "clearable": True,
                    "prefix": {
                        "type": "icon",
                        "icon": "fa fa-user"
                    }
                },
                {
                    "type": "input-password",
                    "name": "password",
                    "label": "密码",
                    "required": True,
                    "placeholder": "请输入密码",
                    "clearable": True,
                    "prefix": {
                        "type": "icon",
                        "icon": "fa fa-lock"
                    }
                },
                {
                    "type": "switch",
                    "name": "remember_me",
                    "label": "记住我",
                    "value": False
                }
            ],
            "actions": [
                {
                    "type": "submit",
                    "label": "登录",
                    "level": "primary",
                    "size": "lg",
                    "className": "w-full"
                }
            ],
            "redirect": "/admin",
            "messages": {
                "saveSuccess": "登录成功！"
            }
        }
    )


def create_app():
    """创建 FastAPI 应用"""
    app = FastAPI(title="FastAPI Amis Admin")
    
    # 创建站点并注册路由器
    # 挂载到根路径 "/"
    site = AmisSite(title="管理后台")
    site.add_router(user_router)
    site.add_router(system_router)
    site.add_router(auth_router)
    site.mount_to_app(app) 
    

    # 基本路由
    @app.get("/api/info")
    async def api_info():
        return {"message": "FastAPI Amis Admin", "site_info": site.site_info}

    # 用户管理 API
    @app.get("/api/users")
    async def get_users(page: int = 1, perPage: int = 10, keyword: str = ""):
        """获取用户列表"""
        users = [
            {"id": 1, "username": "admin", "email": "admin@example.com", "role": "admin", "status": "active", "created_at": "2024-01-01 10:00:00"},
            {"id": 2, "username": "user1", "email": "user1@example.com", "role": "user", "status": "active", "created_at": "2024-01-02 11:00:00"},
            {"id": 3, "username": "user2", "email": "user2@example.com", "role": "user", "status": "inactive", "created_at": "2024-01-03 12:00:00"},
            {"id": 4, "username": "guest1", "email": "guest1@example.com", "role": "guest", "status": "active", "created_at": "2024-01-04 13:00:00"},
        ]
        
        # 关键词搜索
        if keyword:
            users = [u for u in users if keyword.lower() in u["username"].lower() or keyword.lower() in u["email"].lower()]
        
        # 分页
        start = (page - 1) * perPage
        end = start + perPage
        page_users = users[start:end]
        
        return {
            "status": 0,
            "msg": "ok",
            "data": {
                "items": page_users,
                "total": len(users)
            }
        }

    @app.post("/api/users")
    async def create_user(user_data: dict):
        """创建用户"""
        return {
            "status": 0,
            "msg": "用户创建成功",
            "data": {
                "id": 999,
                **user_data,
                "created_at": "2024-01-15 14:00:00"
            }
        }

    @app.put("/api/users/{user_id}")
    async def update_user(user_id: int, user_data: dict):
        """更新用户"""
        return {
            "status": 0,
            "msg": "用户更新成功",
            "data": {"id": user_id, **user_data}
        }

    @app.delete("/api/users/{user_id}")
    async def delete_user(user_id: int):
        """删除用户"""
        return {"status": 0, "msg": f"用户 {user_id} 删除成功"}

    # 系统管理 API
    @app.get("/api/system/settings")
    async def get_system_settings():
        """获取系统设置"""
        return {
            "status": 0,
            "msg": "ok",
            "data": {
                "site_name": "FastAPI Amis Admin",
                "admin_email": "admin@example.com",
                "site_url": "https://example.com",
                "debug_mode": False,
                "session_timeout": 30,
                "max_upload_size": 10,
                "timezone": "Asia/Shanghai",
                "description": "基于 FastAPI 和 Amis 的管理后台系统"
            }
        }

    @app.post("/api/system/settings")
    async def update_system_settings(settings: dict):
        """更新系统设置"""
        return {
            "status": 0,
            "msg": "系统设置更新成功",
            "data": settings
        }

    @app.get("/api/system/status")
    async def get_system_status():
        """获取系统状态"""
        return {
            "status": 0,
            "data": {
                "uptime": "7天12小时",
                "memory_usage": "512MB / 2GB (25.6%)",
                "cpu_usage": "23.5%",
                "disk_usage": "15.2GB / 100GB (15.2%)",
                "network_status": "正常",
                "database_status": "已连接"
            }
        }

    # 认证 API
    @app.post("/api/auth/login")
    async def login(login_data: dict):
        """用户登录"""
        username = login_data.get("username")
        password = login_data.get("password")
        remember_me = login_data.get("remember_me", False)
        
        # 简单的认证逻辑（实际项目中应该查询数据库）
        if username == "admin" and password == "admin123":
            return {
                "status": 0,
                "msg": "登录成功",
                "data": {
                    "user": {
                        "id": 1,
                        "username": "admin",
                        "email": "admin@example.com",
                        "role": "admin"
                    },
                    "token": "mock_jwt_token_123456789",
                    "expires_in": 3600 if not remember_me else 86400 * 7  # 1小时或7天
                }
            }
        else:
            return {
                "status": 1,
                "msg": "用户名或密码错误"
            }

    @app.post("/api/auth/logout")
    async def logout():
        """用户登出"""
        return {
            "status": 0,
            "msg": "登出成功"
        }

    return app


if __name__ == "__main__":
    import uvicorn
    
    print("=== FastAPI Amis Admin 示例 ===")
    print("访问 http://localhost:4000/ 查看管理后台")
    print("访问 http://localhost:4000/login 查看登录页面")
    print("访问 http://localhost:4000/api/info 查看应用信息")
    print("\n登录信息:")
    print("用户名: admin")
    print("密码: admin123")
    
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=4000, log_config=None)
