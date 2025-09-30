from enum import Enum


class ProgressEnum(str, Enum):
    """进度条模式"""

    line = "click"
    circle = "circle"
    dashboard = "dashboard"


class BarcodeEnum(str, Enum):
    """条形码格式"""

    auto = "auto"  # CODE128
    pharmacode = "pharmacode"
    codabar = "codabar"
    CODE128 = "CODE128"
    CODE128A = "CODE128A"
    CODE128B = "CODE128B"
    CODE128C = "CODE128C"
    EAN2 = "EAN2"
    EAN5 = "EAN5"
    EAN8 = "EAN8"
    EAN13 = "EAN13"
    UPC = "UPC"
    CODE39 = "CODE39"
    ITF14 = "ITF14"
    MSI = "MSI"
    MSI10 = "MSI10"
    MSI11 = "MSI11"
    MSI1010 = "MSI1010"
    MSI1110 = "MSI1110"


class StepStatusEnum(str, Enum):
    """
    步骤状态
    """
    wait = "wait"
    process = "process"
    finish = "finish"
    error = "error"


class TriggerEnum(str, Enum):
    """触发器类型"""

    click = "click"
    hover = "hover"
    focus = "focus"


class PlacementEnum(str, Enum):
    """放置位置"""

    top = "top"
    left = "left"
    right = "right"
    bottom = "bottom"


class LevelEnum(str, Enum):
    """按钮级别"""

    primary = "primary"
    secondary = "secondary"
    info = "info"
    success = "success"
    warning = "warning"
    danger = "danger"
    light = "light"
    dark = "dark"
    link = "link"
    default = "default"


class SizeEnum(str, Enum):
    """窗口大小"""

    xs = "xs"
    sm = "sm"
    md = "md"
    lg = "lg"
    xl = "xl"
    full = "full"


class DisplayModeEnum(str, Enum):
    """表单显示模式"""

    normal = "normal"  # normal mode
    horizontal = "horizontal"  # horizontal mode
    inline = "inline"  # inline mode


class LabelEnum(str, Enum):
    """标签样式"""

    primary = "primary"
    success = "success"
    warning = "warning"
    danger = "danger"
    default = "default"
    info = "info"


class StatusEnum(str, Enum):
    """默认状态"""

    success = "success"
    fail = "fail"
    pending = "pending"
    queue = "queue"
    schedule = "schedule"


class TabsModeEnum(str, Enum):
    """选项卡模式"""

    line = "line"
    card = "card"
    radio = "radio"
    vertical = "vertical"
    chrome = "chrome"
    simple = "simple"
    strong = "strong"
    tiled = "tiled"
    sidebar = "sidebar"
    collapse = "collapse"
    """collapse 容器, 用于将多个页面展示为折叠器"""
