# 贡献指南

感谢你对 FastAPI Amis 项目的关注！我们欢迎任何形式的贡献，包括但不限于：

- 🐛 报告 Bug
- 💡 提出新功能
- 📝 改进文档
- 🔧 提交代码
- ✅ 编写测试

## 行为准则

参与本项目即表示你同意遵守我们的行为准则：

- 尊重所有贡献者
- 接受建设性的批评
- 关注对社区最有利的事情
- 对他人保持同理心

## 如何贡献

### 报告 Bug

如果你发现了 Bug，请在 [GitHub Issues](https://github.com/InfernalAzazel/fastapi-amis/issues) 创建一个新的 issue，并包含：

- 📋 Bug 的详细描述
- 🔄 重现步骤
- 💻 你的环境信息（Python 版本、操作系统等）
- 📸 如果可能，提供截图或错误日志

**Bug 报告模板：**

```markdown
## Bug 描述
简要描述遇到的问题

## 重现步骤
1. ...
2. ...
3. ...

## 期望行为
描述你期望发生什么

## 实际行为
描述实际发生了什么

## 环境信息
- OS: [e.g., macOS 14.0]
- Python: [e.g., 3.10.5]
- FastAPI Amis: [e.g., 0.0.1]
```

### 提出新功能

如果你有新功能的想法：

1. 首先在 [GitHub Issues](https://github.com/InfernalAzazel/fastapi-amis/issues) 创建一个 Feature Request
2. 描述这个功能的用途和价值
3. 如果可能，提供使用示例或 API 设计

**功能请求模板：**

```markdown
## 功能描述
简要描述提议的功能

## 使用场景
描述这个功能的使用场景

## 期望的 API
\`\`\`python
# 示例代码
\`\`\`

## 替代方案
是否考虑过其他实现方式？
```

### 改进文档

文档同样重要！你可以：

- 修正拼写或语法错误
- 添加更多示例
- 改进现有说明
- 翻译文档

文档位于 `docs/` 目录，使用 MkDocs 构建。

### 提交代码

#### 1. Fork 仓库

点击仓库页面右上角的 "Fork" 按钮。

#### 2. 克隆你的 Fork

```bash
git clone https://github.com/your-username/fastapi-amis.git
cd fastapi-amis
```

#### 3. 创建分支

```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/your-bug-fix
```

分支命名规范：

- `feature/xxx` - 新功能
- `fix/xxx` - Bug 修复
- `docs/xxx` - 文档改进
- `refactor/xxx` - 代码重构
- `test/xxx` - 测试相关

#### 4. 设置开发环境

```bash
# 安装 uv（如果尚未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 同步依赖
uv sync

# 激活虚拟环境
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate  # Windows
```

#### 5. 进行修改

遵循项目的代码规范：

- 使用 Python 3.10+ 特性
- 遵循 PEP 8 代码风格
- 添加类型注解
- 编写清晰的注释和文档字符串
- 保持代码简洁可读

#### 6. 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_core.py

# 查看测试覆盖率
pytest --cov=fastapi_amis
```

#### 7. 提交更改

```bash
git add .
git commit -m "feat: add new feature"
```

提交信息规范（遵循 [Conventional Commits](https://www.conventionalcommits.org/)）：

- `feat:` - 新功能
- `fix:` - Bug 修复
- `docs:` - 文档更新
- `style:` - 代码格式调整
- `refactor:` - 代码重构
- `test:` - 测试相关
- `chore:` - 构建/工具相关

#### 8. 推送到 GitHub

```bash
git push origin feature/your-feature-name
```

#### 9. 创建 Pull Request

1. 访问你的 Fork 页面
2. 点击 "Pull Request" 按钮
3. 填写 PR 描述，说明你的更改
4. 等待维护者审核

**Pull Request 模板：**

```markdown
## 变更类型
- [ ] Bug 修复
- [ ] 新功能
- [ ] 文档更新
- [ ] 代码重构

## 描述
简要描述这个 PR 的内容

## 相关 Issue
Closes #issue_number

## 测试
- [ ] 添加了新的测试
- [ ] 所有测试通过
- [ ] 手动测试通过

## 检查清单
- [ ] 代码遵循项目规范
- [ ] 添加了必要的文档
- [ ] 更新了 CHANGELOG
```

## 开发规范

### 代码风格

我们使用以下工具确保代码质量：

- **Ruff** - 代码检查和格式化
- **mypy** - 类型检查
- **pytest** - 测试框架

运行代码检查：

```bash
# 使用 ruff 格式化代码
ruff format .

# 检查代码风格
ruff check .

# 类型检查
mypy fastapi_amis
```

### 类型注解

所有函数都应该有类型注解：

```python
from typing import Optional, List

def get_users(
    page: int = 1,
    limit: int = 10,
    query: Optional[str] = None
) -> List[User]:
    ...
```

### 文档字符串

使用 Google 风格的文档字符串：

```python
def create_page(title: str, body: dict) -> Page:
    """创建一个新的页面。
    
    Args:
        title: 页面标题
        body: 页面内容配置
        
    Returns:
        创建的 Page 对象
        
    Raises:
        ValueError: 如果参数无效
    """
    ...
```

### 测试

- 为新功能编写测试
- 确保测试覆盖率不降低
- 测试应该独立且可重复

```python
def test_create_page():
    """测试页面创建功能"""
    page = Page(title="Test", body={})
    assert page.title == "Test"
```

## 发布流程

项目维护者负责发布新版本：

1. 更新版本号（`pyproject.toml` 和 `__init__.py`）
2. 更新 CHANGELOG.md
3. 创建 Git tag
4. 推送到 GitHub
5. GitHub Actions 自动发布到 PyPI

## 社区

- GitHub Issues - 报告问题和功能请求
- GitHub Discussions - 一般讨论和问答
- Email - 260987762@qq.com

## 许可证

贡献的代码将采用与项目相同的 [Apache 2.0](https://github.com/InfernalAzazel/fastapi-amis/blob/main/LICENSE) 许可证。

## 致谢

感谢所有为项目做出贡献的人！

你的名字将会出现在我们的[贡献者列表](https://github.com/InfernalAzazel/fastapi-amis/graphs/contributors)中。

