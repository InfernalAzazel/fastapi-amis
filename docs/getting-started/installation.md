# 安装

本指南将帮助你在本地环境中安装和配置 FastAPI Amis。

## 环境要求

在开始之前，请确保你的系统满足以下要求：

- **Python**: 3.10 或更高版本
- **操作系统**: Windows, macOS, 或 Linux

## 使用 pip 安装

### 1. 安装稳定版本

从 PyPI 安装最新稳定版本：

```bash
pip install fastapi-amis
```

### 2. 安装开发依赖

如果你需要开发或运行示例，请安装开发依赖：

```bash
pip install fastapi-amis[dev]
```

这将安装以下额外的包：

- fastapi[standard] - FastAPI 及其标准依赖
- uvicorn - ASGI 服务器
- httpx - HTTP 客户端
- pytest - 测试框架
- 以及其他开发工具

## 使用 uv 安装（推荐）

[uv](https://github.com/astral-sh/uv) 是一个快速的 Python 包管理器和项目管理工具。

### 1. 安装 uv

=== "Linux/macOS"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows"

    ```powershell
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

### 2. 安装 FastAPI Amis

```bash
uv pip install fastapi-amis
```

### 3. 安装开发依赖

```bash
uv pip install fastapi-amis[dev]
```

## 从源码安装

如果你想使用最新的开发版本或参与项目开发：

### 1. 克隆仓库

```bash
git clone https://github.com/InfernalAzazel/fastapi-amis.git
cd fastapi-amis
```

### 2. 使用 uv 安装

```bash
# 安装 uv（如果尚未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 同步依赖（包括开发依赖）
uv sync

# 激活虚拟环境
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate  # Windows
```

### 3. 使用 pip 安装

```bash
# 创建虚拟环境
python -m venv .venv

# 激活虚拟环境
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate  # Windows

# 安装依赖
pip install -e ".[dev]"
```

## 验证安装

安装完成后，验证 FastAPI Amis 是否正确安装：

```python
import fastapi_amis
print(fastapi_amis.__version__)
```

或者在命令行中：

```bash
python -c "import fastapi_amis; print(fastapi_amis.__version__)"
```

## 运行示例

克隆仓库后，你可以运行示例项目：

### 简单示例

```bash
cd example
uv run python simple_example.py
# 或使用 python
python simple_example.py
```

访问 http://localhost:4000

### 多页面示例

```bash
cd example
uv run python main.py
# 或使用 python
python main.py
```

访问 http://localhost:3000

## 可选依赖

FastAPI Amis 支持以下可选依赖：

- `dev` - 开发工具和测试框架
- 未来可能添加更多可选依赖（如数据库驱动等）

安装可选依赖：

```bash
# 使用 pip
pip install fastapi-amis[dev]

# 使用 uv
uv pip install fastapi-amis[dev]
```

## 常见问题

### Python 版本不匹配

如果遇到 Python 版本问题，请确保你的 Python 版本至少是 3.10：

```bash
python --version
```

### 权限错误

如果在安装时遇到权限错误，可以尝试：

```bash
pip install --user fastapi-amis
```

### 虚拟环境

我们强烈建议在虚拟环境中安装 FastAPI Amis：

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install fastapi-amis
```

## 下一步

现在你已经安装了 FastAPI Amis，可以继续：

- [创建第一个应用](first-app.md)
- [查看示例项目](examples.md)
- [了解核心概念](../guide/concepts.md)

