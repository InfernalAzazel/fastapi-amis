# 更新日志

本文档记录了 FastAPI Amis 的所有重要更改。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [未发布]

### 计划中的功能

- [ ] 添加更多 Amis 组件封装
- [ ] 支持主题自定义
- [ ] 添加权限管理系统
- [ ] 提供项目脚手架
- [ ] 支持国际化（i18n）

## [0.0.1] - 2025-01-XX

### 新增

- 🎉 首次发布
- ✨ 核心功能模块
  - `AmisView` - 视图基类
  - `AmisViewRouter` - 路由管理
  - `AmisSite` - 站点管理
- 🎨 Amis 组件封装
  - `Page` - 页面组件
  - 基础组件支持
  - 类型定义
- 📦 扩展功能
  - 异常处理
  - 日志配置
- 📝 文档
  - 完整的使用文档
  - 快速开始指南
  - API 参考
  - 示例项目
- 🧪 测试
  - 核心功能单元测试
  - 集成测试框架
- 🔧 工具链
  - 使用 uv 进行包管理
  - GitHub Actions CI/CD
  - PyPI 自动发布

### 技术栈

- Python >= 3.10
- FastAPI
- Pydantic >= 2.5.0
- Jinja2
- Amis 前端框架

---

## 版本说明

### 版本格式

版本号格式：`MAJOR.MINOR.PATCH`

- **MAJOR**: 不兼容的 API 更改
- **MINOR**: 向后兼容的功能新增
- **PATCH**: 向后兼容的问题修正

### 变更类型

- **新增 (Added)**: 新功能
- **变更 (Changed)**: 现有功能的变更
- **废弃 (Deprecated)**: 即将移除的功能
- **移除 (Removed)**: 已移除的功能
- **修复 (Fixed)**: 问题修复
- **安全 (Security)**: 安全性改进

---

## 贡献

查看完整的提交历史：[GitHub Commits](https://github.com/InfernalAzazel/fastapi-amis/commits/main)

感谢所有贡献者！🎉

[未发布]: https://github.com/InfernalAzazel/fastapi-amis/compare/v0.0.1...HEAD
[0.0.1]: https://github.com/InfernalAzazel/fastapi-amis/releases/tag/v0.0.1

