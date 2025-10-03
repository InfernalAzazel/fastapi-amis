from typing import Callable
from pydantic import Field
from fastapi_amis.amis.constants import *
from fastapi_amis.amis.types import *

RemarkT = Union[str, "Remark"]

# ==================== 布局组件 ====================

class Collapse(AmisNode):
    """
    Collapse 折叠器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/collapse#collapse-%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = 'collapse'
    """指定为 collapse 渲染器	"""

    disabled: bool = False
    """禁用"""

    collapsed: bool = True
    """初始状态是否折叠"""

    key: Optional[Union[str, int]] = None
    """标识"""

    header: Optional[Union[str, SchemaNode]] = None
    """标题"""

    body: Optional[Union[str, SchemaNode]] = None
    """内容"""

    showArrow: bool = True
    """是否展示图标"""

class CollapseGroup(AmisNode):
    """
    CollapseGroup 折叠器群组件
    """

    type: str = "collapse-group"

    """指定为 collapse-group 渲染器"""

    activeKey: Union[str, int, List[Union[int, str, None]], None] = None
    """初始化激活面板的 key"""

    accordion: Optional[bool] = None
    """手风琴模式"""

    expandIcon: Optional[SchemaNode] = None
    """自定义切换图标"""

    expandIconPosition: Literal["left", "right"] = "left"
    """设置图标位置，可选值left | right"""

    body: Optional[List[Union[Collapse, SchemaNode]]] = None

class Container(AmisNode):
    """
    Container 是一种容器组件，它可以渲染其他 amis 组件。

    - 注意 Container 组件因为历史原因多了一层 div，推荐使用 wrapper 来作为容器。

    参考：https://baidu.github.io/amis/zh-CN/components/container#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = 'container'
    """指定为 container 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    bodyClassName: Optional[str] = None
    """容器内容区的类名"""

    wrapperComponent: Optional[str] = 'div'
    """容器标签名"""

    style: Optional[str] = None
    """自定义样式"""

    body: Optional[SchemaNode] = None
    """容器内容"""

class Divider(AmisNode):
    """
    Divider 分割线

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/divider#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "divider"
    """"divider" 指定为 分割线 渲染器"""

    className: Optional[str] = None
    """	外层 Dom 的类名"""

    lineStyle: Optional[str] = None
    """分割线的样式，支持dashed和solid"""

    direction: str = "horizontal"
    """分割线的方向，支持horizontal和vertical，版本:3.5.0"""

    color: Optional[str] = None
    """分割线的颜色，版本:3.5.0"""

    rotate: Optional[int] = None
    """分割线的旋转角度，版本:3.5.0"""

    title: Optional[SchemaNode] = None
    """分割线的标题，版本:3.5.0"""

    titleClassName: Optional[str] = None
    """分割线的标题类名，版本:3.5.0"""

    titlePosition: Optional[str] = 'center'
    """分割线的标题位置，支持left、center和right，版本:3.5.0"""

class Flex(AmisNode):
    """
    Flex 布局

    Flex 布局是基于 CSS Flex 实现的布局效果，
    它比 Grid 和 HBox 对子节点位置的可控性更强，
    比用 CSS 类的方式更易用，并且默认使用水平垂直居中的对齐。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/flex#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "flex"
    """指定为 Flex 渲染器"""

    className: Optional[str] = None
    """css 类名"""

    justify: Optional[str] = None

    '''"start", "flex-start", "center", "end", "flex-end", "space-around", "space-between", "space-evenly"'''
    alignItems: Optional[str] = None

    '''对齐,选填: "stretch", "start", "flex-start", "flex-end", "end", "center", "baseline"'''

    style: Optional[dict] = None
    """自定义样式"""

    items: Optional[List[SchemaNode]] = None
    """组件列表"""

class Grid(AmisNode):
    """
    Grid 水平分栏

    参考： https://baidu.github.io/amis/zh-CN/components/grid#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Column(AmisNode):
        """列配置"""

        xs: Optional[int] = None
        """宽度占比： 1 - 12"""

        ClassName: Optional[str] = None
        """列类名"""

        sm: Optional[int] = None
        """宽度占比： 1 - 12"""

        md: Optional[int] = None
        """宽度占比： 1 - 12"""

        lg: Optional[int] = None
        """宽度占比： 1 - 12"""

        valign: Optional[str] = None
        """当前列内容的垂直对齐，选填：'top'|'middle'|'bottom'|'between"""

        body:Optional[List[SchemaNode]] = None

    type: str = "grid"
    """指定为 Grid 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    gap: Optional[str] = None

    """水平间距，选填: 'xs' | 'sm' | 'base' | 'none' | 'md' | 'lg'"""
    valign: Optional[str] = None

    """垂直对齐方式，选填: 'top' | 'middle' | 'bottom' | 'between'"""

    align: Optional[str] = None
    """水平对齐方式，选填: 'left' | 'right' | 'between' | 'center'"""

    columns: Optional[List[SchemaNode]] = None
    """列集合"""

class Grid2D(AmisNode):
    """
    Grid 2D 布局

    Grid 2D 是一种二维布局方式，它可以更直观设置组件位置。

    参考：https://baidu.github.io/amis/zh-CN/components/grid-2d
    """
    class Grids(AmisNode):
        x: Optional[int] = None
        """格子起始位置的横坐标"""

        y: Optional[int] = None
        """格子起始位置的纵坐标"""

        w: Optional[int] = None
        """格子横跨几个宽度"""

        h: Optional[int] = None
        """格子横跨几个高度"""

        width: Optional[Union[str, int]] = None
        """格子所在列的宽度，可以设置 auto"""

        height: Optional[Union[str, int]] = None
        """格子所在行的高度，可以设置 auto"""

        align: str = 'auto'
        """格子内容水平布局，选填: left/center/right/auto"""

        valign: str = 'auto'

        """格子内容垂直布局，可选填: top/bottom/middle/auto"""

    type: str = "grid-2d"

    """指定为 Grid 2D 渲染器"""

    gridClassName: Optional[str] = None
    """外层 Dom 的类名"""

    gap: Optional[Union[int, str]] = 0
    """格子间距，包括水平和垂直"""

    cols: int = 12
    """格子水平划分为几个区域"""

    rowHeight: int = 50
    """每个格子默认垂直高度"""

    rowGap: Optional[Union[int, str]] = None
    """格子垂直间距"""

    grids: Optional[List[SchemaNode]] = None

class HBox(AmisNode):
    """
    HBox 布局

    参考：https://baidu.github.io/amis/zh-CN/components/hbox#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Column(AmisNode):
        columnClassName: str = 'wrapper-xs'
        """列上类名"""

        valign: Optional[str] = None
        """'当前列内容的垂直对齐，选填: top' | 'middle' | 'bottom' | 'between'"""

    type: str = "hbox"
    """指定为 HBox 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    gap: Optional[str] = None
    """水平间距，选填: 'xs' | 'sm' | 'base' | 'none' | 'md' | 'lg'"""

    valign: Optional[str] = None
    """垂直对齐方式，选填: 'top' | 'middle' | 'bottom' | 'between'"""

    align: Optional[str] = None
    """水平对齐方式，选填: 'left' | 'right' | 'between' | 'center'"""

    columns: Optional[List[SchemaNode]] = None

class Page(BasePage):
    """
    Page 页面

    Page 组件是 amis 页面 JSON 配置中顶级容器组件，
    是整个页面配置的入口组件。
    """

    __default_template_path__: str = 'page.jinja2'

    type: str = 'page'
    """指定为 Page 组件"""

    title: Optional[SchemaNode] = None
    """页面标题"""

    subTitle: Optional[SchemaNode] = None
    """页面副标题"""

    remark: Optional["RemarkT"] = None
    """标题附近会出现一个提示图标，鼠标放上去会提示该内容。"""

    aside: Optional[SchemaNode] = None
    """往页面的边栏区域加内容"""

    asideResizor: Optional[bool] = None
    """页面的边栏区域宽度是否可调整"""

    asideMinWidth: Optional[int] = None
    """页面边栏区域的最小宽度"""

    asideMaxWidth: Optional[int] = None
    """页面边栏区域的最大宽度"""

    asideSticky: bool = True
    """用来控制边栏固定与否"""

    toolbar: Optional[SchemaNode] = None
    """往页面的右上角加内容，需要注意的是，当有 title 时，该区域在右上角，没有时该区域在顶部"""

    body: Optional[SchemaNode] = None
    """往页面的内容区域加内容"""

    className: Optional[str] = None
    """外层 dom 类名"""

    cssVars: Optional[dict] = None
    """自定义 CSS 变量，请参考样式"""

    toolbarClassName: Optional[str] = 'v-middle wrapper text-right bg-light b-b'
    """Toolbar dom 类名"""

    bodyClassName: Optional[str] = 'wrapper'
    """Body dom 类名"""

    asideClassName: Optional[str] = 'w page-aside-region bg-auto'
    """Aside dom 类名"""

    headerClassName: Optional[str] = 'bg-light b-b wrapper'
    """Header 区域 dom 类名"""

    initApi: Optional[API] = None
    """Page 用来获取初始数据的 api。返回的数据可以整个 page 级别使用。"""

    initFetch: bool = True
    """是否起始拉取 initApi"""

    initFetchOn: Optional[Expression] = None
    """是否起始拉取 initApi, 通过表达式配置"""

    interval: int = 3000
    """刷新时间(最小 1000)"""

    silentPolling: bool = False
    """	配置刷新时是否显示加载动画"""

    stopAutoRefreshWhen: Optional[Expression] = None
    """通过表达式来配置停止刷新的条件"""

    pullRefresh: Any = {'disabled': True}
    """下拉刷新配置（仅用于移动端）"""

class Pagination(AmisNode):
    """
    Pagination 分页组件

    参考：https://baidu.github.io/amis/zh-CN/components/pagination#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "pagination"
    """	指定为 Pagination 渲染器"""

    mode: Literal["simple", "normal"] = "normal"
    """迷你版本/简易版本 只显示左右箭头，配合 hasNext 使用"""

    layout: Union[str, List[str]] = ["pager"]
    """通过控制 layout 属性的顺序，调整分页结构布局"""

    maxButtons: Union[str, int] = 5
    """最多显示多少个分页按钮，最小为 5"""

    total: Optional[int] = None
    """总条数"""

    activePage: int = 1
    """当前页数"""

    perPage: int = 10
    """	每页显示多条数据"""

    showPerPage: bool = False

    """是否展示 perPage 切换器 layout 和 showPerPage 都可以控制"""
    size: Literal['sm', 'md'] = 'md'

    """组件尺寸，支持md、sm设置，版本: 6.0.0后支持变量"""
    ellipsisPageGap: Union[int, str] = 5
    """多页跳转页数，页数较多出现...时点击省略号时每次前进/后退的页数，默认为5，版本: 6.0.0后支持变量"""

    perPageAvailable: List[int] = [10, 20, 50, 100]
    """指定每页可以显示多少条"""

    showPageInput: bool = False
    """是否显示快速跳转输入框 layout 和 showPageInput 都可以控制"""

    disabled: bool = False
    """	是否禁用"""

    onPageChange: Optional[str] = None
    """分页改变触发，(page: number, perPage: number) => void;"""

class PaginationWrapper(AmisNode):
    """
    PaginationWrapper 分页容器

    分页容器组件，可以用来对已有列表数据做分页处理。
    """
    type: str = "pagination-wrapper"
    """指定为 Pagination-Wrapper 渲染器"""

    showPageInput: Optional[bool] = False
    """是否显示快速跳转输入框"""

    maxButtons: Optional[int] = 5
    """最多显示多少个分页按钮"""

    inputName: str = "items"
    """输入字段名"""

    outputName: str = "items"
    """输出字段名"""

    perPage: Optional[int] = None
    """每页显示多条数据"""

    position: Literal["top", "none", "bottom"] = "top"
    """分页显示位置，如果配置为 none 则需要自己在内容区域配置 pagination 组件，否则不显示"""

    body: Optional[SchemaNode] = None
    """内容区域"""

class Panel(AmisNode):
    """
    Panel 面板

    可以把相关信息以面板的形式展示到一块。

    参考: https://aisuda.bce.baidu.com/amis/zh-CN/components/panel#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "panel"
    """指定为 Panel 渲染器"""
    className: str = "panel-default"
    """外层 Dom 的类名"""

    headerClassName: str = "panel-heading"
    """header 区域的类名"""

    footerClassName: str = "panel-footer bg-light lter wrapper"
    """footer 区域的类名"""

    actionsClassName: str = "panel-footer"
    """actions 区域的类名"""

    bodyClassName: str = "panel-body"
    """body 区域的类名"""

    title: Optional[SchemaNode] = None
    """标题"""

    header: Optional[SchemaNode] = None
    """头部容器"""

    body: Optional[SchemaNode] = None
    """内容容器"""

    footer: Optional[SchemaNode] = None
    """底部容器"""

    affixFooter: Optional[bool] = None
    """是否固定底部容器"""

    actions: Optional[List["Action"]] = None
    """按钮区域"""

class Portlet(AmisNode):
    """
    Portlet 门户栏目

    门户栏目组件

    参考: https://aisuda.bce.baidu.com/amis/zh-CN/components/portlet#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Item(AmisNode):
        title: Optional[str] = None
        """	Tab 标题"""

        icon: Union[str, "Icon", None] = None
        """Tab 的图标"""

        tab: Optional[SchemaNode] = None
        """内容区"""

        toolbar: Optional[SchemaNode] = None
        """tabs 中的工具栏，随 tab 切换而变化"""

        reload: Optional[bool] = None
        """设置以后内容每次都会重新渲染，对于 crud 的重新拉取很有用"""

        unmountOnExit: Optional[bool] = None
        """每次退出都会销毁当前 tab 栏内容"""

        className: str = "bg-white b-l b-r b-b wrapper-md"
        """Tab 区域样式"""

    type: str = "portlet"

    className: Optional[str] = None
    """	外层 Dom 的类名"""

    tabsClassName: Optional[str] = None
    """Tabs Dom 的类名"""

    contentClassName: Optional[str] = None
    """Tabs content Dom 的类名"""

    tabs: Optional[List[Item]] = None
    """tabs 内容"""

    source: Optional[Any] = None
    """tabs 关联数据，关联后可以重复生成选项卡"""

    style: Union[str, dict, None] = None
    """自定义样式"""

    description: Optional[Template] = None
    """标题右侧信息"""

    hideHeader: Optional[bool] = None
    """隐藏头部"""

    divider: bool = False
    """去掉分隔线"""

    mountOnEnter: bool = False
    """只有在点中 tab 的时候才渲染"""

    unmountOnExit: bool = False
    """切换 tab 的时候销毁"""

    scrollable: bool = False
    """是否导航支持内容溢出滚动，vertical和chrome模式下不支持该属性；chrome模式默认压缩标签"""

class Tabs(AmisNode):
    """
    Tabs 选项卡

    选项卡容器组件

    参考: https://baidu.github.io/amis/zh-CN/components/tabs#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Item(AmisNode):
        title: Optional[Union[str, SchemaNode]] = None
        """Tab 标题，当是 SchemaNode 时，该 title 不支持 editable 为 true 的双击编辑"""

        icon: Union[str, "Icon", None] = None
        """Tab 的图标"""

        iconPosition: Literal['left', 'right'] = 'left'
        """Tab 的图标位置"""

        tab: Optional[SchemaNode] = None
        """内容区"""

        hash: Optional[str] = None
        """设置以后将跟 url 的 hash 对应"""

        reload: Optional[bool] = None
        """设置以后内容每次都会重新渲染，对于 crud 的重新拉取很有用"""

        unmountOnExit: Optional[bool] = None
        """每次退出都会销毁当前 tab 栏内容"""

        className: Optional[str] = "bg-white b-l b-r b-b wrapper-md"
        """Tab 区域样式"""

        tip: Optional[str] = None
        """3.2.0及以上版本支持 Tab 提示，当开启 showTip 时生效，作为 Tab 在 hover 时的提示显示，可不配置，如不设置，tabs[x].title 作为提示显示"""

        closable: bool = False
        """是否支持删除，优先级高于组件的 closable"""

        disabled: bool = False
        """是否禁用"""

    type: str = "tabs"
    """指定为 Tabs 渲染器"""

    defaultKey: Optional[Union[str, int]] = None
    """组件初始化时激活的选项卡，hash 值或索引值，支持使用表达式 2.7.1 以上版本"""

    activeKey: Optional[Union[str, int]] = None
    """激活的选项卡，hash 值或索引值，支持使用表达式，可响应上下文数据变化"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    linksClassName: Optional[str] = None
    """Tabs 标题区的类名"""

    contentClassName: Optional[str] = None
    """Tabs 内容区的类名"""

    tabsMode: Optional[TabsModeEnum] = None
    """展示模式，取值可以是 line、card、radio、vertical、chrome、simple、strong、tiled、sidebar"""

    tabs: Optional[List[Item]] = None
    """tabs 内容"""

    source: Optional[str] = None
    """tabs 关联数据，关联后可以重复生成选项卡"""

    toolbar: Optional[SchemaNode] = None
    """tabs 中的工具栏"""

    toolbarClassName: Optional[str] = None
    """tabs 中工具栏的类名"""

    mountOnEnter: bool = True
    """只有在点中 tab 的时候才渲染"""

    unmountOnExit: bool = False
    """切换 tab 的时候销毁"""

    addable: bool = False
    """是否支持新增"""

    addBtnText: str = '增加'
    """新增按钮文案"""

    closable: bool = False
    """是否支持删除"""

    draggable: bool = False
    """是否支持拖拽"""

    showTip: bool = False
    """是否支持提示"""

    showTipClassName: str = ''
    """提示的类"""

    editable: bool = False
    """是否可编辑标签名。当 tabs[x].title 为 SchemaNode 时，双击编辑 Tab 的 title 显示空的内容"""

    scrollable: bool = True
    """是否导航支持内容溢出滚动。（属性废弃）"""

    sidePosition: Literal['left', 'right'] = 'left'
    """sidebar 模式下，标签栏位置"""

    collapseOnExceed: Optional[int] = None
    """当 tabs 超出多少个时开始折叠"""

    collapseBtnLabel: str = 'more'
    """用来设置折叠按钮的文字"""

    swipeable: bool = False
    """是否开启手势滑动切换（移动端生效）"""

class Wrapper(AmisNode):
    """
    Wrapper 包裹容器

    简单的一个包裹容器组件，相当于用 div 包含起来，最大的用处是用来配合 css 进行布局。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/wrapper#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "wrapper"
    """指定为 Wrapper 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    size: Union[str, SizeEnum, None] = None
    """支持: xs、sm、md 和 lg"""

    style: Union[str, dict, None] = None
    """自定义样式"""

    body: Optional[SchemaNode] = None
    """内容容器"""

# ==================== 功能 ====================

class Action(AmisNode):
    """
    Action 行为按钮

    Action 行为按钮，是触发页面行为的主要方法之一

    参考： https://baidu.github.io/amis/zh-CN/components/action?page=1#%E9%80%9A%E7%94%A8%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "action"
    """指定为 Page 渲染器"""

    actionType: Optional[str] = None
    """【必填】这是 action 最核心的配置，来指定该 action 的作用类型，支持：ajax、link、url、drawer、dialog、confirm、cancel、prev、next、copy、close"""

    label: Optional[str] = None
    """按钮文本,可用 ${xxx} 取值"""

    level: Optional[LevelEnum] = LevelEnum.default.value
    """按钮样式，支持：link、primary、secondary、info、success、warning、danger、light、dark、default"""

    size: Optional[str] = None
    """按钮大小，支持：xs、sm、md、lg"""

    icon: Optional[str] = None
    """设置图标，例如fa fa-plus"""

    iconClassName: Optional[str] = None
    """给图标上添加类名"""

    rightIcon: Optional[str] = None
    """在按钮文本右侧设置图标，例如fa fa-plus"""

    rightIconClassName: Optional[str] = None
    """给右侧图标上添加类名"""

    active: Optional[bool] = None
    """按钮是否高亮"""

    activeLevel: Optional[str] = None
    """按钮高亮时的样式，配置支持同level"""

    activeClassName: str = 'is-active'
    """给按钮高亮添加类名"""

    block: Optional[bool] = None
    """用 display:"block" 来显示按钮"""

    confirmText: Optional[Template] = None
    """当设置后，操作在开始前会询问用户。可用 ${xxx} 取值"""

    confirmTitle: Optional[Template] = None
    """确认框标题，前提是 confirmText 有内容，支持模版语法"""

    reload: Optional[str] = None

    """指定此次操作完后，需要刷新的目标组件名字（组件的name值，自己配置的），多个请用 , 号隔开"""
    tooltip: Optional[str] = None

    """鼠标停留时弹出该段文字，也可以配置对象类型：字段为title和content。可用 ${xxx} 取值"""
    disabledTip: Optional[str] = None

    """被禁用后鼠标停留时弹出该段文字，也可以配置对象类型：字段为title和content。可用 ${xxx} 取值"""
    tooltipPlacement: str = 'top'

    """如果配置了tooltip或者disabledTip，指定提示信息位置，可配置top、bottom、left、right"""
    close: Optional[Union[bool, str]] = None

    """当action配置在dialog或drawer的actions中时，配置为true指定此次操作完后关闭当前dialog或drawer。当值为字符串，并且是祖先层弹框的名字的时候，会把祖先弹框关闭掉"""
    required: Optional[List[str]] = None
    """配置字符串数组，指定在form中进行操作之前，需要指定的字段名的表单项通过验证"""

    args: Union[dict, str, None] = None
    """事件参数"""

class ActionType:
    """行为按钮类型"""

    class Ajax(Action):
        actionType: str = "ajax"
        """ 点击后显示弹出窗口"""

        api: Optional[API] = None
        """请求地址，参考 api 格式说明"""

        redirect: Optional[Template] = None
        """指定当前请求结束后要重定向到的路径，可以是估值 ${xxx}."""

        feedback: Optional["Dialog"] = None
        """如果是ajax类型，当ajax恢复正常时，可以弹出一个对话框"""

        messages: Optional[dict] = None
        """
        用于其他交互。返回的数据可以在此对话框中使用。格式请参考对话框
        成功：AJAX作成功后将显示一条消息。它可以不指定。如果未指定，则以 api 返回为准。failed：Ajax作失败消息
        """

    class Dialog(Action):
        actionType: str = "dialog"
        """单击时显示弹出窗口"""
        
        dialog: Union["Dialog", "Service", SchemaNode]
        """指定弹出框的内容，格式可以参考 Dialog"""
        
        nextCondition: Optional[bool] = None
        """可用于设置下一个数据的条件，默认为 true"""

    class Drawer(Action):
        actionType: str = "drawer"
        """单击时显示侧边栏"""
        
        drawer: Union["Drawer", "Service", SchemaNode]
        """指定弹出框的内容，格式可以参考 Drawer"""

    class Copy(Action):
        actionType: str = "copy"
        """复制一段内容到剪贴板"""
        
        content: Template
        """指定要复制的内容。可用 ${xxx} 值"""
        
        copyFormat: Optional[str] = None
        """可以通过 copyFormat 设置复制格式，默认为 text text/html"""

    class Url(Action):
        """直接跳转"""
        
        actionType: str = "url"
        """直接跳转"""
        
        url: str
        """当按钮被点击时，将打开指定页面。可用 ${xxx} 值"""
        
        blank: Optional[bool] = None
        """如果为 true 将在新标签页中打开"""

    class Link(Action):
        """单页跳转"""
        
        actionType: str = "link"
        """单页跳转"""
        
        link: str
        """用于指定跳转地址。与 url 不同，这是单页跳转方法，不会重新渲染浏览器。请在 amis 平台中指定页面。可用 ${xxx} 值"""

    class Toast(Action):
        """Toast 轻提示"""
        
        class ToastItem(AmisNode):
            title: Optional[SchemaNode] = None
            """Toast 项目标题"""
            
            body: Optional[SchemaNode] = None
            """Toast 项目内容"""
            
            level: Optional[str] = None
            """默认 'info'，显示图标，可选 'info', 'success', 'error', 'warning'"""
            
            position: Optional[str] = None
            """默认 'top-center'，显示位置，可选 'top-right', 'top-center', 'top-left', 'bottom-center', 'bottom-left', 'bottom-right', 'center'"""
            
            closeButton: Optional[bool] = None
            """默认 False，是否显示关闭按钮"""
            
            showIcon: Optional[bool] = None
            """默认 True，是否显示图标"""
            
            timeout: Optional[int] = None
            """默认 5000"""

        actionType: str = "toast"
        """单页跳转"""
        
        items: Optional[List[ToastItem]] = None
        """ToastItems 列表"""
        
        position: Optional[str] = None
        """显示位置，可选 'top-right', 'top-center', 'top-left', 'bottom-center', 'bottom-left', 'bottom-right', 'center'"""
        
        closeButton: Optional[bool] = None
        """默认 False，是否显示关闭按钮，移动端不支持"""
        
        showIcon: Optional[bool] = None
        """默认 True，是否显示图标"""
        
        timeout: Optional[int] = None
        """默认 5000"""



class AnchorNav(AmisNode):
    """
    AnchorNav 锚点导航

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/anchor-nav#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Link(AmisNode):
        label: Optional[str] = None

        title: Optional[str] = None
        """区域 标题"""

        href: Optional[str] = None
        """区域 标识"""

        body: Optional[SchemaNode] = None
        """
        - 区域 内容区
        - 版本：6.1.0及以上版本垂直方向支持配置子节点
        """

        className: Optional[str] = None
        """区域成员 样式"""

    type: str = "anchor-nav"
    """指定为 AnchorNav 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    linkClassName: Optional[str] = None
    """导航 Dom 的类名"""

    sectionClassName: Optional[str] = None
    """锚点区域 Dom 的类名"""

    direction: Optional[Literal['vertical', 'horizontal']] = None
    """
    - 可以配置导航水平展示还是垂直展示
    - 默认值：'vertical'
    """

    active: Optional[str] = None
    """需要定位的区域"""

    links: Optional[list[Link]] = None
    """links 内容"""

class PageSchema(AmisNode):
    """
    页面配置

    参考：https://baidu.github.io/amis/zh-CN/components/app#%E5%B1%9E%E6%80%A7%E8%AF%B4%E6%98%8E
    """

    label: Optional[str] = None
    """菜单名称"""

    icon: str = "fa fa-flash"
    """菜单图标，比如：fa fa-file."""

    url: Optional[str] = None
    """页面路由路径，当路由命中该路径时，启用当前页面。当路径不是 / 打头时，会连接父级路径。比如：父级的路径为"""

    schema_: Optional[Union["Page", "Iframe", dict]] = Field(None, alias="schema")
    """页面的配置，具体配置请前往 Page 页面说明"""
    schemaApi: Optional[API] = None

    """如果想通过接口拉取，请配置。返回路径为 json>data。schema 和 schemaApi 只能二选一"""
    link: Optional[str] = None

    """如果想配置个外部链接菜单，只需要配置 link 即可"""
    redirect: Optional[str] = None

    """如果想配置个外部链接菜单，只需要配置 link 即可"""
    rewrite: Optional[str] = None

    """改成渲染其他路径的页面，这个方式页面地址不会发生修改"""
    isDefaultPage: Union[bool, str, None] = None

    """当你需要自定义 404 页面的时候有用，不要出现多个这样的页面，因为只有第一个才会有用"""
    visible: Union[bool, str, None] = None

    """有些页面可能不想出现在菜单中，可以配置成 false，另外带参数的路由无需配置，直接就是不可见的"""
    className: Optional[str] = None
    """菜单类名"""

    children: Optional[List["PageSchema"]] = None
    """子菜单"""

    tabsMode: Optional[TabsModeEnum] = None
    """展示模式，取值可以是 line、card、radio、vertical、chrome、simple、strong、tiled、sidebar"""

    def as_page_body(self, group_extra: Optional[Dict[str, Any]] = None, item_extra: Optional[Dict[str, Any]] = None):
        """
        将页面配置转换为页面主体组件
        
        根据当前页面的配置和子页面情况，生成相应的页面主体组件：
        - 如果有子页面，根据 tabsMode 模式生成不同的容器组件
        - 如果没有子页面，根据页面类型生成对应的内容组件
        
        Args:
            group_extra: 组级别的额外属性，用于自定义容器组件的属性
            item_extra: 子项级别的额外属性，用于自定义子页面组件的属性
            
        Returns:
            页面主体组件，可能是以下类型之一：
            - App: 当有子页面且 tabsMode 为 None 时
            - CollapseGroup: 当有子页面且 tabsMode 为 collapse 时
            - Tabs: 当有子页面且 tabsMode 为其他模式时
            - Page/Iframe: 当页面有 schema 配置时
            - Service: 当页面有 schemaApi 配置时
            - Page: 当页面有 link 配置时
            - None: 当页面没有任何内容配置时
        """
        if self.children:
            # 定义需要排除的属性，避免在子组件中重复传递
            exclude = {"type", "url", "schema", "schemaApi", "link", "redirect", "rewrite", "isDefaultPage",
                       "children"}
            
            # 根据 tabsMode 模式生成不同的容器组件
            if self.tabsMode is None:
                # 默认模式：使用 App 组件包装子页面
                body = App(pages=[PageSchema(children=self.children, schema={})])
            elif self.tabsMode == TabsModeEnum.collapse:
                # 折叠模式：使用 CollapseGroup 组件，每个子页面作为一个折叠项
                body = (
                    CollapseGroup.model_validate(self.model_dump(exclude=exclude, exclude_defaults=True))
                    .update_from_kwargs(
                        body=[
                            CollapseGroup.CollapseItem.model_validate(item.model_dump(exclude=exclude, exclude_defaults=True))
                            .update_from_kwargs(
                                header=item.label,  # 折叠项的标题
                                body=item.as_page_body(group_extra, item_extra),  # 递归处理子页面
                            )
                            .update_from_dict(item_extra or {})  # 应用子项额外属性
                            for item in self.children
                        ],
                    )
                    .update_from_dict(group_extra or {})  # 应用组级别额外属性
                )
            else:
                # 标签页模式：使用 Tabs 组件，每个子页面作为一个标签页
                body = (
                    Tabs.model_validate(self.model_dump(exclude=exclude, exclude_defaults=True))
                    .update_from_kwargs(
                        mountOnEnter=True,  # 进入时挂载，提高性能
                        tabs=[
                            Tabs.Item.model_validate(item.model_dump(exclude=exclude, exclude_defaults=True))
                            .update_from_kwargs(
                                title=item.label,  # 标签页标题
                                tab=item.as_page_body(group_extra, item_extra),  # 递归处理子页面
                            )
                            .update_from_dict(item_extra or {})  # 应用子项额外属性
                            for item in self.children
                        ],
                    )
                    .update_from_dict(group_extra or {})  # 应用组级别额外属性
                )
        elif self.schema_:
            # 直接使用配置的 schema 作为页面内容
            body = self.schema_
            if isinstance(body, Iframe):
                # 为 Iframe 设置默认高度
                body.height = body.height or 1080
        elif self.schemaApi:
            # 通过 API 获取页面内容
            body = Service(schemaApi=self.schemaApi)
        elif self.link:
            # 链接页面：创建一个包含链接的页面
            body = Page(body=Link(href=self.link, body=self.label, blank=True))
        else:
            # 没有任何内容配置
            body = None
        return body

class App(BasePage):
    """
    App 多页应用

    用于实现多页应用，适合于全屏模式，如果只是局部渲染请不要使用。
    """

    __default_template_path__: str = "app.jinja2"

    type: str = "app"
    """指定为 app 渲染器"""

    api: Optional[API] = None
    """页面配置接口，如果你想远程拉取页面配置请配置。返回配置路径 json>data>pages，具体格式请参考 pages 属性"""

    brandName: Optional[Template] = None
    """应用名称"""

    logo: Optional[str] = None
    """支持图片地址，或者 svg"""

    className: Optional[str] = None
    """css 类名"""

    header: Optional[Template] = None
    """顶部区域"""

    asideBefore: Optional[Template] = None
    """页面菜单上前面区域"""

    asideAfter: Optional[Template] = None
    """页面菜单下前面区域"""

    footer: Optional[Template] = None
    """脚页"""

    pages: Optional[List[Union[PageSchema, dict]]] = None
    """
    Array<页面配置>具体的页面配置。 通常为数组，
    数组第一层为分组，一般只需要配置 label 集合，如果你不想分组，
    直接不配置，真正的页面请在第二层开始配置，即第一层的 children 中
    """

class Breadcrumb(AmisNode):
    """
    Breadcrumb 面包屑

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/breadcrumb#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class BreadcrumbItem(AmisNode):
        label: Optional[str] = None
        """文本"""

        href: Optional[str] = None
        """链接"""

        icon: Optional[str] = None
        """图标"""

        dropdown: Optional[List] = None
        """下拉菜单，dropdown[]的每个对象都包含label、href、icon属性"""

    type: str = "breadcrumb"
    """指定为 breadcrumb 渲染器"""

    className: Optional[str] = None
    """外层类名"""

    itemClassName: Optional[str] = None
    """导航项类名"""

    separatorClassName: Optional[str] = None
    """分割符类名"""

    dropdownClassName: Optional[str] = None
    """下拉菜单类名"""

    dropdownItemClassName: Optional[str] = None
    """下拉菜单项类名"""

    separator: str = ">"
    """分隔符"""

    labelMaxLength: Optional[int] = None
    """
    - 最大展示长度
    - 默认值：16
    """

    tooltipPosition: Optional[Literal['top', 'bottom', 'left', 'right']] = None
    """
    - 浮窗提示位置
    - 默认值：'top'
    """

    source: Optional[API] = None
    "动态数据"

    items: Optional[List[BreadcrumbItem]] = None
    """项目"""

class Button(AmisNode):
    """
    Button 按钮

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/button#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "button"
    """指定为 button 渲染器"""

    className: Optional[str] = None
    """指定添加 button 类名"""

    label: Optional[str] = None
    """button 名称"""

    url: Optional[str] = None
    """点击跳转的地址，指定此属性 button 的行为和 a 链接一致"""

    size: Optional[str] = None
    """设置按钮大小"""

    actionType: Optional[Literal['button', 'reset', 'submit', 'clear', 'url']] = None
    """
    - 设置按钮类型
    - 默认值：'button'
    """

    level: Optional[Literal['link', 'primary', 'enhance', 'secondary', 'info', 'success', 'warning', 'danger', 'light', 'dark', 'default']] = None
    """
    - 设置按钮样式
    - 默认值：'default'
    """

    tooltip: Optional[Union[str, dict]] = None
    """气泡提示内容"""

    tooltipPlacement: Optional[Literal['top', 'right', 'bottom', 'left' ]] = None
    """
    - 气泡框位置器
    - 默认值：'top'
    """

    tooltipTrigger: Optional[Literal['hover', 'focus']] = None
    """触发 tootip"""

    disabled: Optional[bool] = None
    """
    - 按钮失效状态
    - 默认值: false
    """

    disabledTip: Optional[Union[str, dict]] = None
    """按钮失效状态下的提示"""

    block: Optional[bool] = None
    """
    - 将按钮宽度调整为其父宽度的选项
    - 默认值：false
    """

    loading: Optional[bool] = None
    """
    - 显示按钮 loading 效果
    - 默认值：false
    """

    loadingOn: Optional[str] = None
    """显示按钮 loading 表达式"""

class ButtonGroup(AmisNode):
    """
    ButtonGroup 按钮组

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/button-group#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "button-group"
    """指定为 button-group 渲染器"""

    vertical: Optional[bool] = None
    """
    - 是否使用垂直模式
    - 默认值：false
    """

    tiled: Optional[bool] = None
    """
    - 是否使用平铺模式
    - 默认值：false
    """

    btnLevel: Optional[Literal[
        'link', 'primary','secondary', 'info', 'success', 'warning', 'danger','light', 'dark', 'default']] = None
    """
    - 按钮样式
    - 默认值：'default'
    """

    btnActiveLevel: Optional[Literal[
        'link', 'primary', 'secondary', 'info', 'success', 'warning', 'danger', 'light', 'dark', 'default']] = None
    """
    - 选中按钮样式
    - 默认值：'default'
    """

    buttons: List[Action]
    """按钮"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

class Custom(AmisNode):
    """
    Custom 自定义组件

    用于实现自定义组件，它解决了之前 JS SDK 和可视化编辑器中难以支持自定义组件的问题。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/custom#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "custom"
    """指定为 custom 渲染器"""

    id: Optional[str] = None
    """节点 id"""

    name: Optional[str] = None
    """节点 名称"""

    className: Optional[str] = None
    """节点 class"""

    inline: bool = False
    """
    - 默认使用 div 标签，如果 true 就使用 span 标签
    - 默认值：false
    """

    html: Optional[str] = None
    """初始化节点 html"""

    onMount: Optional[str] = None
    """
    - 节点初始化之后调的用函数
    - 默认值：Function
    """

    onUpdate: Optional[str] = None
    """
    - 数据有更新的时候调用的函数
    - 默认值：Function
    """

    onUnmount: Optional[str] = None
    """
    - 节点销毁的时候调用的函数
    - 默认值：Function
    """

class DropDownButton(AmisNode):
    """
    DropDownButton 下拉菜单

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/dropdown-button#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "dropdown-button"
    """指定为 dropdown-button 渲染器"""

    label: Optional[str] = None
    """按钮文本"""

    className: Optional[str] = None
    """外层 CSS 类名"""

    btnClassName: Optional[str] = None
    """按钮 CSS 类名"""

    menuClassName: Optional[str] = None
    """下拉菜单 CSS 类名"""

    block: Optional[bool] = None
    """块状样式"""

    size: Optional[Literal["xs", "sm", "md", "lg"]] = None
    """尺寸"""

    align: Optional[Literal["left", "right"]] = None
    """位置"""

    buttons: List[Button] = None
    """配置下拉按钮"""

    iconOnly: Optional[bool] = None
    """只显示 icon"""

    defaultIsOpened: Optional[bool] = None
    """默认是否打开"""

    closeOnOutside: Optional[bool] = None
    """
    - 点击外侧区域是否收起
    - 默认值：true
    """

    closeOnClick: Optional[bool] = None
    """
    - 点击按钮后自动关闭下拉菜单
    - 默认值：false
    """

    trigger:  Optional[Literal['click', 'hover']] = None
    """
    - 触发方式
    - 默认值：'click'
    """

    hideCaret: Optional[bool] = None
    """
    - 隐藏下拉图标
    - 默认值：false
    """

class Nav(AmisNode):
    """
    Nav 导航

    用于展示链接导航

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/nav#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Overflow(AmisNode):
        enable: Optional[bool] = None
        """
        - 是否开启响应式收纳
        - 默认值：false
        """

        overflowLabel: Optional[Union[str, dict]] = None
        """菜单触发按钮的文字"""

        overflowIndicator: Optional[str] = None
        """
        - 菜单触发按钮的图标
        - 默认值：'fa fa-ellipsis'
        """

        maxVisibleCount: Optional[int] = None

        """开启响应式收纳后导航最大可显示数量，超出此数量的导航将被收纳到下拉菜单中，默认为自动计算"""
        wrapperComponent: Optional[str] = None

        """包裹导航的外层标签名，可以使用其他标签渲染"""
        style: Optional[dict] = None
        """自定义样式"""

        overflowClassName: Optional[dict] = None
        """菜单按钮 CSS 类名"""

        overflowPopoverClassName: Optional[dict] = None
        """Popover 浮层 CSS 类名"""

    class Link(AmisNode):
        label: Optional[str] = None
        """名称"""

        to: Optional[Template] = None
        """链接地址"""

        target: Optional[str] = None
        """链接关系"""

        icon: Optional[str] = None
        """图标"""

        children: Optional[List['Nav.Link']] = None
        """子链接"""

        unfolded: Optional[bool] = None
        """初始是否展开"""

        active: Optional[bool] = None
        """是否高亮"""

        activeOn: Optional[Expression] = None
        """是否高亮的条件，留空将自动分析链接地址"""

        defer: Optional[bool] = None
        """标记是否为懒加载项"""

        deferApi: Optional[API] = None
        """可以不配置，如果配置优先级更高"""

        disabled: Optional[bool] = None
        """是否禁用"""

        disabledTip: Optional[str] = None
        """禁用提示信息"""

        className: Optional[str] = None
        """菜单项自定义样式"""

        mode: Optional[Literal['group', 'divider']] = None
        """菜菜单项模式，分组模式、分割线"""

        overflow: Optional['Nav.Overflow'] = None
        """导航项响应式收纳配置"""


    class NavMatchFunc(AmisNode):
        link: Optional[List['Nav.Link']] = None
        """导航项对象"""

        keyword: Optional[str] = None
        """搜索关键字"""

    class SearchConfig(AmisNode):
        matchFunc: Optional['Nav.NavMatchFunc'] = None
        """自定义匹配函数, 默认模糊匹配导航对象中的label, title 和 key 字段"""

        className: Optional[str] = None
        """搜索框外层 CSS 类名"""

        placeholder: Optional[bool] = None
        """
        - 是否开启搜索
        - 默认值：'false'
        """

        mini: Optional[bool] = None
        """
        - 是否为 mini 模式
        - 默认值：'false'
        """

        enhance: Optional[bool] = None
        """
        - 是否为增强样式
        - 默认值：'false'
        """

        clearable: Optional[bool] = None
        """
        - 是否开启搜索
        - 默认值：'false'
        """

        searchImediately: Optional[bool] = None
        """
        - 是否立即搜索
        - 默认值：'false'
        """


    type: str = "nav"
    """指定为 Nav 渲染器"""

    mode: Optional[str] = None
    """
    - 导航模式，悬浮或者内联，默认内联模式	
    - 默认值：'inline'
    """

    collapsed: Optional[bool] = None
    """控制导航是否缩起"""

    indentSize: Optional[int] = None
    """
    - 层级缩进值，仅内联模式下生效
    - 默认值：16
    """

    level: Optional[int] = None
    """控制导航最大展示层级数"""

    defaultOpenLevel: Optional[int] = None
    """控制导航最大默认展开层级"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    popupClassName: Optional[str] = None
    """当为悬浮模式时，可自定义悬浮层样式"""

    expandIcon: Optional[Union[str, dict]] = None
    """自定义展开按钮"""

    expandPosition: Optional[Literal['before', 'after']] = None
    """展开按钮位置，不设置默认在前面	"""

    stacked: Optional[bool] = None
    """
    - 设置成 false 可以以 tabs 的形式展示
    - 默认值：true
    """

    accordion: Optional[bool] = None
    """是否开启手风琴模式"""

    source: Optional[API] = None
    """可以通过变量或 API 接口动态创建导航"""

    deferApi: Optional[API] = None
    """用来延时加载选项详情的接口，可以不配置，不配置公用 source 接口"""

    itemActions: Optional[SchemaNode] = None
    """更多操作相关配置"""

    draggable: Optional[bool] = None
    """是否支持拖拽排序"""

    dragOnSameLevel: Optional[bool] = None
    """仅允许同层级内拖拽"""

    saveOrderApi: Optional[API] = None
    """保存排序的 api"""

    itemBadge: Optional['Badge'] = None
    """角标"""

    links: Optional[list] = None
    """链接集合"""

    overflow: Optional[Overflow] = None
    """响应式收纳配置"""

    searchable: Optional[bool] = None
    """
    - 是否开启搜索
    - 默认值：false
    - 版本：3.5.0
    """

    searchConfig: Optional[SearchConfig] = None
    """
    - 搜索配置
    - 版本：3.5.0
    """

class PopOver(AmisNode):
    """
    PopOver 弹出提示

    popover 不是一个独立组件，它是嵌入到其它组件中使用的，目前可以在以下组件中配置

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/popover?page=1#%E5%B1%9E%E6%80%A7%E5%88%97%E8%A1%A8
    """
    mode: Optional[Literal['popOver', 'dialog', 'drawer']] = None
    """
    - 模式
    - 默认值：'popOver'
    """

    size: Optional[int] = None
    """当配置成 dialog 或者 drawer 的时候有用"""

    position: Optional[str] = None
    """配置弹出位置，只有 popOver 模式有用，默认是自适应"""

    offset: Optional[dict] = None
    """
    - 偏移
    - 默认值： {top: 0, left: 0}
    """

    trigger: Optional[Literal['click', 'hover']] = None
    """
    - 触发弹出的条件
    - 默认值：'click'
    """

    showIcon: Optional[bool] = None
    """是否显示图标。默认会有个放大形状的图标出现在列里面。如果配置成 false，则触发事件出现在列上就会触发弹出。"""

    title: Optional[str] = None
    """弹出框的标题"""

    body: Optional[Union[str, dict]] = None
    """弹出框的内容"""

class Service(AmisNode):
    """
    Service 功能型容器

    - amis 中部分组件，作为展示组件，
      自身没有使用接口初始化数据域的能力，例如：Table、Cards、List等，
      他们需要使用某些配置项，例如source，通过数据映射功能，
      在当前的 数据链 中获取数据，并进行数据展示。

    - 而Service组件就是专门为该类组件而生，它的功能是：配置初始化接口，
      进行数据域的初始化，然后在Service内容器中配置子组件，
      这些子组件通过数据链的方法，获取Service所拉取到的数据。

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/service#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Messages(AmisNode):

        fetchSuccess: Optional[str] = None
        """接口请求成功时的 toast 提示文字"""

        fetchFailed: Optional[str] = None
        """
        - 接口请求失败时 toast 提示文字
        - 默认值：'初始化失败'
        """

    type: str = "service"
    """指定为 service 渲染器	"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    body: Optional[SchemaNode] = None
    """内容容器"""

    api: Optional[API] = None
    """初始化数据域接口地址	"""

    ws: Optional[Union[str, dict]] = None
    """WebScocket 地址"""

    dataProvider: Optional[Union[str, dict]] = None
    """
    - 数据获取函数
    - 版本：1.4.0, 1.8.0 支持env参数，2.3.0 支持基于事件触发
    """

    initFetch: Optional[bool] = None
    """
    - 是否默认拉取
    - 默认值：false
    """

    schemaApi: Optional[API] = None
    """用来获取远程 Schema 接口地址"""

    initFetchSchema: Optional[bool] = None
    """是否默认拉取 Schema"""

    messages: Optional[Messages] = None
    """消息提示覆写，默认消息读取的是接口返回的 toast 提示文字，但是在此可以覆写它。"""

    interval: Optional[int] = None
    """轮询时间间隔，单位 ms(最低 1000)"""

    silentPolling: Optional[bool] = None
    """
    - 配置轮询时是否显示加载动画
    - 默认值：false
    """

    stopAutoRefreshWhen: Optional[Expression] = None
    """配置停止轮询的条件"""

    showErrorMsg: Optional[bool] = None
    """
    - 是否以 Alert 的形式显示 api 接口响应的错误信息，默认展示
    - 默认值：true
    - 版本：2.8.1
    """

class TooltipWrapper(AmisNode):
    """
    TooltipWrapper 文字提示容器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/tooltip#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "tooltip-wrapper"
    """指定为文字提示容器组件"""

    title: Optional[Optional[str]] = None
    """文字提示标题"""

    content: Optional[str] = None
    """文字提示内容, 兼容之前的 tooltip 属性"""

    placement: Optional[Literal['top', 'left', 'right', 'bottom']] = None
    """
    - 文字提示浮层出现位置
    - 默认值：'top'
    """

    tooltipTheme: Optional[Literal["light", "dark"]] = None
    """
    - 主题样式
    - 默认值：'light'
    """

    offset: Optional[list[int]] = None
    """
    - 文字提示浮层位置相对偏移量，单位 px
    - 默认值：[0, 0]
    """

    showArrow: Optional[bool] = None
    """
    - 是否展示浮层指向箭头
    - 默认值：true
    """

    enterable: Optional[bool] = None
    """
    - 是否鼠标可以移入到浮层中
    - 默认值：true
    """

    disabled: Optional[bool] = None
    """
    - 是否禁用浮层提示
    - 默认值：false
    """

    trigger: Union[Literal['hover','click', 'focus'], list[Literal['hover','click', 'focus']]] = None
    """
    - 浮层触发方式，支持数组写法["hover", "click"]
    - 默认值：'hover'
    """

    mouseEnterDelay: Optional[int] = None
    """
    - 浮层延迟展示时间，单位 ms
    - 默认值：0
    """

    mouseLeaveDelay: Optional[int] = None
    """
    - 浮层延迟隐藏时间，单位 ms
    - 默认值：300
    """

    rootClose: Optional[bool] = None
    """
    - 是否点击非内容区域关闭提示
    - 默认值：true
    """

    inline: Optional[bool] = None
    """
    - 内容区是否内联显示
    - 默认值：false
    """

    wrapperComponent: Optional[str] = None
    """
    - 容器标签名
    - 默认值：'div' | 'span'
    """

    body: Optional[SchemaNode] = None
    """内容容器"""

    style: Optional[Union[str, dict]] = None
    """内容区自定义样式"""

    tooltipStyle:  Optional[Union[str, dict]] = None
    """浮层自定义样式"""

    className: Optional[str] = None
    """内容区类名"""

    tooltipClassName: Optional[str] = None
    """文字提示浮层类名"""

# ==================== 数据输入 ====================

class Form(AmisNode):
    """
    Form 表单

    表单是 amis 中核心组件之一，主要作用是提交或者展示表单数据。

    参考: https://aisuda.bce.baidu.com/amis/zh-CN/components/form/index#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Messages(AmisNode):
        fetchSuccess: Optional[str] = None
        """获取成功时提示"""

        fetchFailed: Optional[str] = None
        """获取失败时提示"""

        saveSuccess: Optional[str] = None
        """保存成功时提示"""

        saveFailed: Optional[str] = None
        """保存失败时提示"""

    class Horizontal(AmisNode):
        left: Optional[int] = None
        """左侧标签的宽度比例"""

        right: Optional[int] = None
        """右侧控制器的宽度比"""

        justify: Optional[bool] = None

    type: str = "form"
    """指定 Form 渲染器"""

    name: Optional[str] = None
    """设置一个名字后，方便其他组件与其通信"""

    mode: Optional[Literal['normal', 'horizontal', 'inline']] = None
    """表单展示方式"""

    horizontal: Optional["Horizontal"] = None
    """
    - 当 mode 为 horizontal 时有用，用来控制 label 的展示占比
    - 默认值: '{"left":2, "right":10, "justify": false}'"""

    labelAlign: Optional[Literal["right", "left"]] = None
    """ 
    - 表单项标签对齐方式，默认右对齐，仅在 mode为horizontal 时生效
    - 默认值: right
    """

    labelWidth: Union[int, str, None] = None
    """表单项标签自定义宽度"""

    title: Optional[Optional[str]] = None
    """
    - Form 的标题 
    - 默认值'表单'"""

    submitText: Optional[Optional[str]] = None
    """
    - 默认的提交按钮名称，如果设置成空，则可以把默认按钮去掉
    - 默认值：'提交'
    """

    className: Optional[str] = None
    """外部 Dom 的类名"""

    body: Optional[List[Union["FormItem", SchemaNode]]] = None
    """Form 表单项集合"""

    actions: Optional[List["Action"]] = None
    """Form 提交按钮，成员为 Action"""

    messages: Optional[Messages] = None
    """消息提示覆写，默认消息读取的是 API 返回的消息，但是在此可以覆写它"""

    wrapWithPanel: Optional[bool] = None
    """
    - 是否让 Form 用 panel 包起来，设置为 false 后，actions 将无效
    - 默认值：true
    """

    panelClassName: Optional[str] = None
    """外层 panel 的类名"""

    api: Optional[API] = None
    """Form 用来保存数据的 api"""

    initApi: Optional[API] = None
    """Form 用来获取初始数据的 api"""

    rules: Optional[list] = None
    """表单组合校验规则"""

    interval: Optional[int] = None
    """
    - 刷新时间(最低 3000)
    - 默认值：3000
    """

    silentPolling: Optional[bool] = None
    """
    - 配置刷新时是否显示加载动画
    - 默认值：false
    """

    stopAutoRefreshWhen: Optional[str] = None
    """
    通过表达式 来配置停止刷新的条件
    """

    initAsyncApi: Optional[API] = None
    """Form 用来获取初始数据的 api,与 initApi 不同的是，会一直轮询请求该接口，直到返回 finished 属性为 true 才 结束"""

    initFetch: Optional[bool] = None
    """
    - 设置了 initApi 或者 initAsyncApi 后，默认会开始就发请求，设置为 false 后就不会起始就请求接口
    - 默认值：true
    """

    initFetchOn: Optional[str] = None
    """用表达式来配置"""

    initFinishedField: Optional[Optional[str]] = None
    """
    - 设置了 initAsyncApi 后，默认会从返回数据的 data.finished 来判断是否完成，也可以设置成其他的 xxx，就会从 data.xxx 中获取
    - 默认值：'finished'
    """

    initCheckInterval: Optional[int] = None
    """
    - 设置了 initAsyncApi 以后，默认拉取的时间间隔
    - 默认值：3000
    """

    asyncApi: Optional[API] = None
    """设置此属性后，表单提交发送保存接口后，还会继续轮询请求该接口，直到返回 finished 属性为 true 才 结束"""

    checkInterval: Optional[int] = None
    """
    - 轮询请求的时间间隔，默认为 3 秒。设置 asyncApi 才有效
    默认值：3000
    """

    finishedField: Optional[Optional[str]] = None
    """
    - 如果决定结束的字段名不是 finished 请设置此属性，比如 is_success
    - 默认值：'finished'
    """

    submitOnChange: Optional[bool] = None
    """
    - 表单修改即提交
    - 默认值：false
    """

    submitOnInit: Optional[bool] = None
    """
    - 初始就提交一次
    - 默认值：false
    """

    resetAfterSubmit: Optional[bool] = None
    """
    - 提交后是否重置表单
    - 默认值：false
    """

    primaryField: Optional[str] = None
    """
    - 设置主键 id, 当设置后，检测表单是否完成时（asyncApi），只会携带此数据
    - 默认值：'id'
    """

    target: Optional[str] = None
    """
    - 默认表单提交自己会通过发送 api 保存数据，但是也可以设定另外一个 form 的 name 值，或者另外一个 CRUD 模型的 name 值。 
    - 如果 target 目标是一个 Form ，则目标 Form 会重新触发 initApi，api 可以拿到当前 form 数据。
    - 如果目标是一个 CRUD 模型，则目标模型会重新触发搜索，参数为当前 Form 数据。
    - 当目标是 window 时，会把当前表单的数据附带到页面地址上。
    """

    redirect: Optional[str] = None
    """设置此属性后，Form 保存成功后，自动跳转到指定页面。支持相对地址，和绝对地址（相对于组内的)"""

    reload: Optional[str] = None
    """操作完后刷新目标对象。请填写目标组件设置的 name 值，如果填写为 window 则让当前页面整体刷新。"""

    autoFocus: Optional[bool] = None
    """
    - 是否自动聚焦
    - 默认值：false
    """

    canAccessSuperData: Optional[bool] = None
    """
    - 指定是否可以自动获取上层的数据并映射到表单项上
    - 默认值：true
    """

    persistData: Optional[str] = None
    """指定一个唯一的 key，来配置当前表单是否开启本地缓存"""

    persistDataKeys: Optional[List[str]] = None
    """指指定只有哪些 key 缓存"""

    clearPersistDataAfterSubmit: Optional[bool] = None
    """
    - 指定表单提交成功后是否清除本地缓存
    - 默认值：true
    """

    preventEnterSubmit: Optional[bool] = None
    """
    - 禁用回车提交表单
    - 默认值：false
    """

    trimValues: Optional[bool] = None
    """
    - trim 当前表单项的每一个值
    - 默认值：false
    """

    promptPageLeave: Optional[bool] = None
    """
    - form 还没保存，即将离开页面前是否弹框确认。
    - 默认值：false
    """

    columnCount: Optional[int] = None
    """
    - 表单项显示为几列
    - 默认值：0
    """

    inheritData: Optional[bool] = None
    """
    - 默认表单是采用数据链的形式创建个自己的数据域
    - 表单提交的时候只会发送自己这个数据域的数据
    - 如果希望共用上层数据域可以设置这个属性为 false
    - 这样上层数据域的数据不需要在表单中用隐藏域或者显式映射才能发送了
    """

    static: Optional[bool] = None
    """
    - 2.4.0 整个表单静态方式展示
    - 详情请查看示例页: https://aisuda.bce.baidu.com/amis/examples/form/switchDisplay
    """

    staticClassName: Optional[str] = None
    """2.4.0 表单静态展示时使用的类名"""

    closeDialogOnSubmit: Optional[bool] = None
    """提交的时候是否关闭弹窗。当 form 里面有且只有一个弹窗的时候，本身提交会触发弹窗关闭，此属性可以关闭此行为"""

    debug: Optional[bool] = None

class FormItem(AmisNode):
    """
    FormItem 普通表单项

    表单项 是组成一个表单的基本单位，它具有的一些特性会帮助我们更好地实现表单操作。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/formitem#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """



    class AutoFill(BaseAmisModel):

        showSuggestion: Optional[bool] = None
        """true 为参照录入，false 自动填充"""

        api: Optional[API] = None
        """自动填充接口/参照录入筛选 CRUD 请求配置"""

        silent: Optional[bool] = None
        """是否展示数据格式错误提示，默认为 true"""

        fillMappinng: Optional[SchemaNode] = None
        """自动填充/参照录入数据映射配置，键值对形式，值支持变量获取及表达式"""
        trigger: Optional[str] = None

        """showSuggestion 为 true 时，参照录入支持的触发方式，目前支持 change「值变化」｜ focus 「表单项聚焦」"""
        mode: Optional[str] = None

        """showSuggestion 为 true 时，参照弹出方式 dialog, drawer, popOver"""
        labelField: Optional[str] = None

        """showSuggestion 为 true 时，设置弹出 dialog,drawer,popOver 中 picker 的 labelField"""
        position: Optional[str] = None

        """showSuggestion 为 true 时，参照录入 mode 为 popOver 时，可配置弹出位置"""
        size: Optional[str] = None

        """showSuggestion 为 true 时，参照录入 mode 为 dialog 时，可设置大小"""
        columns: Optional[List[Union["TableColumn", "TableColumn2"]]] = None
        """showSuggestion 为 true 时，数据展示列配置"""

        filter: Optional[SchemaNode] = None
        """showSuggestion 为 true 时，数据查询过滤条件"""

    class StaticSchema(BaseAmisModel):
        limit: Optional[int] = None
        """
        - 2.4.0 select、checkboxes 等选择类组件多选时展示态展示的数量
        - 默认值：10
        """

    class Validation(BaseAmisModel):
        """
        表单项值发生变化即校验

        默认校验是当进行行为操作时，对表单项进行校验，如果你想每次表单项的值发生变化的时候就校验，请配置 "validateOnChange": true

        参考: https://aisuda.bce.baidu.com/amis/zh-CN/components/form/formitem#%E6%94%AF%E6%8C%81%E7%9A%84%E6%A0%BC%E5%BC%8F%E6%A0%A1%E9%AA%8C
        """
        isEmail: Optional[bool] = None
        """必须是 电子邮件"""

        isUrl: Optional[bool] = None
        """必须是 Url"""

        isNumeric: Optional[bool] = None
        """必须是 数值"""

        isAlpha: Optional[bool] = None
        """必须是 字母"""

        isAlphanumeric: Optional[bool] = None
        """必须是 字母或者数字"""

        isInt: Optional[bool] = None
        """必须是 整形"""

        isFloat: Optional[bool] = None
        """必须是 浮点形"""

        isLength: Optional[int] = None
        """是否长度正好等于设定值"""

        minLength: Optional[int] = None
        """最小长度"""

        maxLength: Optional[int] = None
        """最大长度"""

        maximum: Optional[int] = None
        """最大值"""

        minimum: Optional[int] = None
        """最小值"""

        equals: Optional[str] = None
        """当前值必须完全等于 xxx"""

        equalsField: Optional[str] = None
        """当前值必须与 xxx 变量值一致"""

        isJson: Optional[bool] = None
        """是否是合法的 Json 字符串"""

        isUrlPath: Optional[bool] = None
        """是 url 路径"""

        isPhoneNumber: Optional[bool] = None
        """是否为合法的手机号码"""

        isTelNumber: Optional[bool] = None
        """是否为合法的电话号码"""

        isZipcode: Optional[bool] = None
        """是否为邮编号码"""

        isId: Optional[bool] = None
        """是否为身份证号码，支持 18 位和 15 位验证，单个验证请使用 isId18 / isId15"""

        matchRegexp: Optional[str] = None
        """
        - 必须命中某个正则
        - matchRegexp${n}:/foo/ 这样的需要手动加入字段
        """

        isDateTimeSame: Optional[bool] = None
        """日期和目标日期相同，支持指定粒度，默认到毫秒 millisecond"""

        isDateTimeBefore: Optional[bool] = None
        """日期早于目标日期，支持指定粒度，默认到毫秒 millisecond"""

        isDateTimeAfter: Optional[bool] = None
        """日期晚于目标日期，支持指定粒度，默认到毫秒 millisecond"""

        isDateTimeSameOrBefore: Optional[bool] = None
        """日期早于目标日期或和目标日期相同，支持指定粒度，默认到毫秒 millisecond"""

        isDateTimeSameOrAfter: Optional[bool] = None
        """日期晚于目标日期或和目标日期相同，支持指定粒度，默认到毫秒 millisecond"""

        isDateTimeBetween: Optional[bool] = None
        """日期处于目标日期范围，支持指定粒度和区间的开闭形式，默认到毫秒 millisecond，左右开区间'()'"""

        isTimeSame: Optional[bool] = None
        """时间和目标时间相同，支持指定粒度，默认到毫秒 millisecond"""

        isTimeBefore: Optional[bool] = None
        """时间早于目标时间，支持指定粒度，默认到毫秒 millisecond"""

        isTimeAfter: Optional[bool] = None
        """时间晚于目标时间，支持指定粒度，默认到毫秒 millisecond"""

        isTimeSameOrBefore: Optional[bool] = None
        """时间早于目标时间或和目标时间相同，支持指定粒度，默认到毫秒 millisecond"""

        isTimeSameOrAfter: Optional[bool] = None
        """时间晚于目标时间或和目标时间相同，支持指定粒度，默认到毫秒 millisecond"""

        isTimeBetween: Optional[bool] = None
        """时间处于目标时间范围，支持指定粒度和区间的开闭形式，默认到毫秒 millisecond，左右开区间'()'"""

        isVariableName: Optional[bool] = None
        """是否为合法的变量名，默认规则为 /^[a-zA-Z_]+[a-zA-Z0-9]*$/ 可以自己指定如 {isVariableName: /^a.*$/}"""

    type: str = "input-text"
    """指定表单项类型"""

    className: Optional[str] = None
    """表单最外层类名"""

    inputClassName: Optional[str] = None
    """表单控制器类名"""

    labelClassName: Optional[str] = None
    """label 的类名"""

    name: Optional[str] = None
    """字段名，指定该表单项提交时的 key"""

    value: Optional[str] = None
    """表单默认值"""

    label: Union[bool, Template, None] = None
    """表单项标签"""

    labelAlign: Optional[str] = None
    """
    - 表单项标签对齐方式，默认右对齐，仅在 mode为horizontal 时生效
    - 默认值：'right'
    """

    labelRemark: Optional[RemarkT] = None
    """表单项标签描述"""

    description: Optional[Template] = None
    """表单项描述"""

    placeholder: Optional[str] = None
    """表单项描述"""

    inline: Optional[bool] = None
    """是否为 内联 模式"""

    strictMode: Optional[bool] = None
    """通过配置 false 可以及时获取所有表单里面的数据，否则可能会有不同步"""

    submitOnChange: Optional[bool] = None
    """是否该表单项值发生变化时就提交当前表单。"""

    disabled: Optional[bool] = None
    """当前表单项是否是禁用状态"""

    disabledOn: Optional[Expression] = None
    """当前表单项是否禁用的条件"""

    visible: Optional[bool] = None
    """当前表单项是否禁用的条件"""

    visibleOn: Optional[Expression] = None
    """当前表单项是否禁用的条件"""

    required: Optional[bool] = None
    """是否为必填"""

    requiredOn: Optional[Expression] = None
    """通过表达式来配置当前表单项是否为必填"""

    validations: Optional[Union["Validation", Expression]] = None
    """表单项值格式验证，支持设置多个，多个规则用英文逗号隔开"""

    validateApi: Optional[API] = None
    """表单校验接口"""

    autoFill: Optional[AutoFill] = None
    """数据录入配置，自动填充或者参照录入"""

    static: Optional[bool] = None
    """2.4.0 当前表单项是否是静态展示，目前支持静支持静态展示的表单项"""

    staticClassName: Optional[str] = None
    """2.4.0 静态展示时的类名"""

    staticLabelClassName: Optional[str] = None
    """2.4.0 静态展示时的 Label 的类名"""

    staticInputClassName: Optional[str] = None
    """2.4.0 静态展示时的 value 的类名"""

    staticSchema: Optional[StaticSchema] = None
    """2.4.0 自定义静态展示方式"""

class Control(AmisNode):
    """
    Control 表单项包裹

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/control
    """
    type: str =  'control'
    """指定 control 渲染器"""

    label: Optional[str] = None
    """标签"""

    description: Optional[str] = None
    """描述"""

    body: Optional[Union[str, dict, list]] = None
    """内容容器"""

class Options(AmisNode):
    """
    Options 选择器表单项

    - 选择器表单项 是指那些（例如下拉选择框）具有选择器特性的表单项

    - 它派生自 表单项，拥有表单项所有的特性

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/options#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    options: Optional[Union[ list[dict], list[str]]] = None
    """选项组，供用户选择"""

    source: Optional[Union[API, Tpl]] = None
    """选项组源，可通过数据映射获取当前数据域变量、或者配置 API 对象"""

    multiple: Optional[bool] = None
    """
    - 是否支持多选
    - 默认值: false
    """

    labelField: Optional[str] = None
    """
    - 标识选项中哪个字段是label值
    - 默认值: 'label'
    """

    valueField: Optional[str] = None
    """
    - 标识选项中哪个字段是label值
    - 默认值: 'value'
    """

    deferField: Optional[str] = None
    """
    - 标识选项中哪个字段是defer值
    - 默认值: 'defer'
    """

    joinValues: Optional[bool] = None
    """
    - 是否拼接value值
    - 默认值: true
    """

    extractValue: Optional[bool] = None
    """
    - 是否将value值抽取出来组成新的数组，只有在joinValues是false是生效
    - 默认值: false
    """

    itemHeight: Optional[int] = None
    """
    - 每个选项的高度，用于虚拟渲染
    - 默认值: 32
    """

    virtualThreshold: Optional[int] = None
    """
    - 在选项数量超过多少时开启虚拟渲染
    - 默认值: 100
    """

    valuesNoWrap: Optional[bool] = None
    """
    - 默认情况下多选所有选项都会显示，通过这个可以最多显示一行，超出的部分变成
    - 默认值: false
    """

class InputArray(FormItem):
    """
    InputArray 数组输入框

    InputArray 是一种简化的 Combo，用于输入多个某种类型的表单项，提交的时将以数组的形式提交。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-array#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-array"
    """指明为array组件"""
    items: Optional[Union[FormItem, SchemaNode]] = None
    """配置单项表单类型"""
    addable: Optional[bool] = None
    """是否可新增"""
    removable: Optional[bool] = None
    """是否可删除"""
    draggable: Optional[bool] = None
    """是否可以拖动排序, 需要注意的是当启用拖动排序的时候，会多一个$id 字段"""
    draggableTip: Optional[str] = None
    """
    - 可拖拽的提示文字，
    - 默认值：'可通过拖动每行中的【交换】按钮进行顺序调整'
    """
    addButtonText: Optional[str] = None
    """
    - 新增按钮文字
    - 默认值：'新增'
    """
    minLength: Optional[int] = None
    """限制最小长度"""
    maxLength: Optional[int] = None
    """限制最大长度"""
    scaffold: Optional[Any] = None
    """新增成员时的默认值，一般根据items的数据类型指定需要的默认值"""

class ButtonToolbar(AmisNode):
    """
    Button-Toolbar 按钮工具栏

    默认按钮会独占一行，如果想让多个按钮并排方式，可以使用 button-toolbar 组件包裹起来，另外还有能用 button-group 来在展现上更紧凑。
    """

    type: str = "button-toolbar"
    """指定为 ButtonToolbar 组件"""

    buttons: List[Action]
    """按钮组"""

class ButtonGroupSelect(FormItem):
    """
    Button-Group-Select 按钮点选

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/button-group-select#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "button-group-select"

    vertical: Optional[bool] = None
    """
    - 是否使用垂直模式
    - 默认值：false
    """

    tiled: Optional[bool] = None
    """
    - 是否使用平铺模式
    - 默认值：false
    """

    btnLevel: Optional[Literal['link', 'primary', 'secondary', 'info', 'success', 'warning', 'danger', 'light', 'dark', 'default']] = None
    """
    - 按钮样式
    - 默认值："default"
    """

    btnActiveLevel: Optional[Literal['link', 'primary', 'secondary', 'info', 'success', 'warning', 'danger', 'light', 'dark', 'default']] = None
    """
    - 选中按钮样式
    - 默认值："default"
    """

    options: Optional[OptionsNode] = None
    """选项组"""


    source: Optional[Union[str, Any]] = None
    """动态选项组"""

    multiple: Optional[bool] = None
    """
    - 多选
    - 默认值：false
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值："label"
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值："value"
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    autoFill: Optional[Dict[str, Any]] = None
    """自动填充"""

class ChainedSelect(FormItem):
    """
    Chained-Select 链式下拉框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/chain-select#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "chained-select"
    """指定为 chained-select 组件"""

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    autoComplete: Optional[Union[str, API]] = None
    """自动选中"""

    delimiter: Optional[str] = None
    """
    - 拼接符
    - 默认值：','
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值：','
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值：'value'
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

class Checkbox(FormItem):
    """
    Checkbox 勾选框

    用于实现勾选，功能和 Switch 类似，只是展现上不同。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/checkbox#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "checkbox"
    """指定为 checkbox 组件"""

    option: Optional[str] = None
    """选项说明"""

    trueValue: Optional[Union[str, int, bool]] = None
    """
    - 标识真值
    - 默认值：true
    """
    falseValue: Optional[Union[str, int, bool]] = None
    """
    - 标识假值
    - 默认值：false
    """

    optionType: Optional[Literal['default', 'button']] = None
    """
    - 设置 option 类型
    - 默认值：'default'
    """

class Checkboxes(FormItem):
    """
    Checkboxes 复选框

    用于实现多选

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/checkboxes#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "checkboxes"
    """指定为 checkboxes 组件"""

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    delimiter: Optional[str] = None
    """	
    - 拼接符
    - 默认值：','
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值：'label'
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值：'value'
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    columnsCount: Optional[int] = None
    """
    - 选项按几列显示，默认为一列
    - 默认值：1
    """

    menuTpl: Optional[str] = None
    """支持自定义选项渲染"""

    checkAll: Optional[bool] = None
    """
    - 是否支持全选
    - 默认值：false
    """

    inline: Optional[bool] = None
    """
    - 是否支持全选
    - 默认值：true
    """

    defaultCheckAll: Optional[bool] = None
    """
    - 默认是否全选
    - 默认值：false
    """

    creatable: Optional[bool] = None
    """
    - 新增选项
    - 默认值：false
    """

    createBtnLabel: Optional[str] = None
    """
    - 新增选项
    - 默认值：'新增选项'
    """

    addControls: Optional[List['FormItem']] = None
    """自定义新增表单项"""

    addApi: Optional[API] = None
    """配置新增选项接口"""

    editable: Optional[bool] = None
    """
    - 编辑选项
    - 默认值：false
    """

    editControls: Optional[List['FormItem']] = None
    """自定义编辑表单项"""

    editApi: Optional[API] = None
    """配置编辑选项接口"""

    removable: Optional[bool] = None
    """
    - 删除选项
    - 默认值：false
    """

    deleteApi: Optional[API] = None
    """
    - 配置删除选项接口
    - 默认值：false
    """

    optionType: Optional[Literal["default", "button"]] = None
    """
    - 按钮模式
    - 默认值：'default'
    """

    itemClassName: Optional[str] = None
    """	选项样式类名"""

    labelClassName: Optional[str] = None
    """labelClassName"""

class InputCity(FormItem):
    """
    InputCity 城市选择器

    城市选择器，方便输入城市，可以理解为自动配置了国内城市选项的 Select，支持到县级别。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-city#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = 'input-city'
    """指明为 input-city 组件"""

    allowCity: Optional[bool] = None
    """
    - 允许选择城市
    - 默认值：true
    """

    allowDistrict: Optional[bool] = None
    """
    允许选择区域
    - 默认值：true
    """

    searchable: Optional[bool] = None
    """
    是否出搜索框
    - 默认值：false
    """

    extractValue: Optional[bool] = None
    """
    - 如果设置成 false 值格式会变成对象，包含 code、province、city 和 district 文字信息
    - 默认值：true
    """

class InputColor(FormItem):
    """
    InputColor 颜色选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-color#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class PresetColor(AmisNode):
        title: Optional[str] = None
        """标题"""

        color: Optional[str] = None
        """颜色"""

    type: str = "input-color"
    """指明为 input-color 组件"""

    format: Optional[Literal['hex', 'hls', 'rgb', 'rgba']] = None
    """
    - 格式化
    - 默认值：'hex'
    """

    presetColors: Optional[list[PresetColor]] = None
    """选择器底部的默认颜色，数组内为空则不显示默认颜色"""

    allowCustomColor: Optional[bool] = None
    """
    - 为false时只能选择颜色，使用 presetColors 设定颜色选择范围
    - 默认值：true
    """

    clearable: Optional[bool] = None
    """
    - 是否显示清除按钮
    - 默认值：false
    """

    resetValue: Optional[str] = None
    """清除后，表单项值调整成该值"""

class Combo(FormItem):
    """
    Combo 组合

    用于将多个表单项组合到一起，实现深层结构的数据编辑。

    比如想提交 user.name 这样的数据结构，有两种方法：一种是将表单项的 name 设置为user.name，另一种就是使用 combo。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/combo#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "combo"
    """指定为 combo 组件"""

    formClassName: Optional[str] = None
    """单组表单项的类名"""

    items: Optional[list['FormItem']] = None
    """组合展示的表单项"""

    noBorder: Optional[bool] = None
    """
    - 单组表单项是否显示边框
    - 默认值：false
    """

    scaffold: Optional[dict] = None
    """单组表单项初始值"""

    multiple: Optional[bool] = False
    """是否多选"""

    multiLine: Optional[bool] = False
    """默认是横着展示一排，设置以后竖着展示"""

    minLength: Optional[int] = None
    """
    - 最少添加的条数
    - 版本: 2.4.1 版本后支持变量
    """

    maxLength: Optional[int] = None
    """
    - 最多添加的条数
    - 版本: 2.4.1 版本后支持变量
    """

    flat: Optional[bool] = False
    """
    - 是否将结果扁平化(去掉 name),只有当 items 的 length 为 1 且 multiple 为 true 的时候才有效
    - 默认值：false
    """

    joinValues: Optional[bool] = True
    """
    - 默认为 true 当扁平化开启的时候，是否用分隔符的形式发送给后端，否则采用 array 的方式
    - 默认值：true
    """

    delimiter: Optional[str] = None
    """当扁平化开启并且 joinValues 为 true 时，用什么分隔符"""

    addable: Optional[bool] = False
    """
    - 是否可新增
    - 默认值：false
    """

    addattop: Optional[bool] = False
    """
    - 在顶部添加
    - 默认值：false
    """

    removable: Optional[bool] = False
    """
    - 是否可删除
    - 默认值：false
    """

    deleteApi: Optional[API] = None
    """如果配置了，则删除前会发送一个 api，请求成功才完成删除"""

    deleteConfirmText: Optional[str] = None
    """当配置 deleteApi 才生效！删除时用来做用户确认"""

    draggable: Optional[bool] = False
    """
    - 是否可以拖动排序, 需要注意的是当启用拖动排序的时候，会多一个$id 字段
    - 默认值：false
    """

    draggableTip: Optional[str] = None
    """可拖拽的提示文字"""

    subFormMode: Optional[Literal['normal', 'horizontal', 'inline']] = None
    """
    - 子表单模式
    - 默认值：'normal'
    """

    subFormHorizontal: Optional[dict] = None
    """
    - 当 subFormMode 为 horizontal 时有用，用来控制 label 的展示占比
    - 默认值：false
    """

    placeholder: Optional[str] = None
    """
    - 没有成员时显示
    """

    canAccessSuperData: Optional[bool] = False
    """
    - 指定是否可以自动获取上层的数据并映射到表单项上
    - 默认值：false
    """

    conditions: Optional[dict] = None
    """数组的形式包含所有条件的渲染类型，单个数组内的test 为判断条件，数组内的items为符合该条件后渲染的schema"""

    typeSwitchable: Optional[bool] = None
    """
    - 是否可切换条件，配合conditions使用
    - 默认值：false
    """

    strictMode: Optional[bool] = True
    """默认为严格模式，设置为 false 时，当其他表单项更新是，里面的表单项也可以及时获取，否则不会"""

    syncFields: Optional[list[str]] = None
    """配置同步字段。只有 strictMode 为 false 时有效。如果 Combo 层级比较深，底层的获取外层的数据可能不同步。但是给 combo 配置这个属性就能同步下来。输入格式：["os"]"""

    nullable: Optional[bool]  = False
    """
    - 允许为空，如果子表单项里面配置验证器，且又是单条模式。可以允许用户选择清空（不填）
    - 默认值：false
    """

    itemClassName: Optional[str] = None
    """单组 CSS 类"""

    itemsWrapperClassName: Optional[str] = None
    """组合区域 CSS 类"""

    deleteBtn: Optional[Union[str, 'Button']] = None
    """
    - 只有当removable为 true 时有效; 如果为string则为按钮的文本；如果为Button则根据配置渲染删除按钮。
    - 默认值：'自定义删除按钮'
    """

    addBtn: Optional['Button'] = None
    """
    - 可新增自定义配置渲染新增按钮，在tabsMode: true下不生效。
    - 默认值：'自定义新增按钮'
    """

    addButtonClassName: Optional[str] = None
    """新增按钮 CSS 类名"""

    addButtonText: Optional[str] = None
    """新增按钮文字"""

class ConditionBuilder(FormItem):
    """
    组合条件

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/condition-builder#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Field(AmisNode):
        type: str = "text"

        label: Optional[str] = None
        """字段名称"""

        placeholder: Optional[str] = None
        """占位符"""

        operators: Optional[List[str]] = None
        """
        - 定义可以用于该字段的操作符列表。这些操作符用于构建查询条件
        - 默认值：[ 'equal', 'not_equal', 'is_empty', 'is_not_empty', 'like', 'not_like', 'starts_with', 'ends_with' ]
        """

        defaultOp: Optional[str] = None
        """
        - 设置默认使用的操作符
        - 默认值：'equal'
        """

    class Text(Field):
        """文本"""

    class Number(Field):
        """数字"""

        type: str = "number"

        minimum: Optional[int] = None
        """最小值"""

        maximum: Optional[int] = None
        """最大值"""

        step: Optional[int] = None
        """步长"""

    class Date(Field):
        """日期"""

        type: str = "date"

        defaultValue: Optional[str] = None
        """默认值"""

        format: Optional[str] = None
        """
        - 格式
        - 默认值：'YYYY-MM-DD'
        """

        inputFormat: Optional[str] = None
        """
        - 显示的日期格式
        - 默认值：'YYYY-MM-DD'
        """

    class Datetime(Date):
        """日期时间"""

        type: str = "datetime"

        timeFormat: Optional[str] = None
        """
        - 时间格式，决定输入框有哪些
        - 默认值：'HH:mm'
        """


    class Time(Date):
        """时间"""

        type: str = "time"

    class Select(Field):
        """下拉选择"""

        type: str = "select"

        options: Optional[OptionsNode] = None
        """选项列表"""

        source: Optional[API] = None
        """动态选项，请配置 api"""

        searchable: Optional[bool] = None
        """是否可以搜索"""

        autoComplete: Optional[API] = None
        """自动提示补全，每次输入新内容后，将调用接口，根据接口返回更新选项"""

        maxTagCount: Optional[int] = None
        """可以限制标签的最大展示数量，超出数量的部分会收纳到 Popover 中，可以通过 overflowTagPopover 配置 Popover 相关的属性，注意该属性仅在多选模式开启后生效"""

    class Custom(Field):
        value: Optional[Union[str, dict]] = None
        """字段配置右边值需要渲染的组件，支持 amis 输入类组件或自定义输入类组件"""

    class Option(AmisNode):
        label: str
        value: Any

    class InputSettings(AmisNode):
        type: str = 'text'
        """"类型: 'text', 'number', 'boolean', 'date', 'time', 'datetime', 'select'"""

        step: Optional[float] = None
        """"数字类型 - 步长"""

        min: Optional[float] = None
        """"数字类型 - 最小值"""

        max: Optional[float] = None
        """"数字类型 - 最大值"""

        precision: Optional[int] = None
        """"数字类型 - 精度"""

        format: Optional[str] = None
        """"日期时间类型 - 格式"""

        inputFormat: Optional[str] = None
        """"日期时间类型 - 输入框格式"""

        timeFormat: Optional[str] = None
        """"日期时间类型 - 时间格式"""

        options: Optional[List['ConditionBuilder.Option']] = None
        """"选择类型 - 选项集合"""

        multiple: Optional[bool] = None
        """"选择类型 - 是否多选"""

        trueLabel: Optional[str] = None
        """"布尔类型 - 真值 label"""

        falseLabel: Optional[str] = None
        """"布尔类型 - 假值 label"""

        defaultValue: Optional[Any] = None
        """"默认值"""


    type: str = "condition-builder"
    """指定为 condition-builder 组件"""

    className: Optional[str] = None
    """外部 dom 类名"""

    fieldClassName: Optional[str] = None
    """输入字段的类名"""

    source: Optional[str] = None
    """通过远程拉取配置项"""

    embed: Optional[bool] = None
    """
    - 内嵌展示
    - 默认值：true
    """

    fields: Optional[List[Union[Text, Number, Date, Datetime, Time, Select, Custom]]] = None
    """字段配置"""

    showANDOR: Optional[bool] = None
    """用于 simple 模式下显示切换按钮"""

    showNot: Optional[bool] = None
    """
    - 是否显示「非」按钮
    - 默认值：true
    """

    draggable: Optional[bool] = None
    """
    - 是否可拖拽
    - 默认值：true
    """

    searchable: Optional[bool] = None
    """字段是否可搜索"""

    selectMode: Optional[Literal['list', 'tree', 'chained']] = None
    """
    - 组合条件左侧选项类型
    - 默认值：'list'
    - 版本：'chained'模式需要3.2.0及以上版本
    """

    addBtnVisibleOn: Optional[bool] = None
    """
    - 表达式：控制按钮“添加条件”的显示。参数为depth、breadth，分别代表深度、长度。表达式需要返回boolean类型
    - 版本：3.2.0
    """

    inputSettings: Optional[InputSettings] = None
    """
    - 开启公式编辑模式时的输入控件类型
    - 版本：3.2.0
    """

    formula: Optional[dict] = None
    """
    - 字段输入控件变成公式编辑器
    - 版本：3.2.0
    """

    showIf: Optional[bool] = None
    """
    - 开启后条件中额外还能配置启动条件
    - 版本：3.2.0
    """

    formulaForIf: Optional[dict] = None
    """
    - 给 showIF 表达式用的公式信息
    - 版本：3.4.0
    """

class InputDate(FormItem):
    """
    InputDate 日期

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-date#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-date"
    """指明为 input-date 组件"""

    value: Optional[str] = None
    """默认值"""

    valueFormat: Optional[str] = None
    """
    - 日期选择器值格式，更多格式类型请参考 文档
    - 默认值：'X'
    - 版本：3.4.0 版本后支持
    """

    displayFormat: Optional[str] = None
    """
    - 日期选择器显示格式，即时间戳格式，更多格式类型请参考 文档
    - 默认值：'YYYY-MM-DD'
    - 版本：3.4.0 版本后支持
    """

    closeOnSelect: Optional[bool] = None
    """
    - 点选日期后，是否马上关闭选择框
    - 默认值：false
    """
    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择日期'
    """

    shortcuts: Optional[Union[str, list[str], list[dict]]] = None
    """
    - 日期快捷键，字符串格式为预设值，对象格式支持写表达式
    - 版本：3.1.0 版本后支持表达式
    """

    minDate: Optional[str] = None
    """限制最小日期"""

    maxDate: Optional[str] = None
    """限制最大日期"""

    utc: Optional[bool] = None
    """
    - 保存 utc 值
    - 默认值：false
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    embed: Optional[bool] = None
    """
    - 是否内联模式
    - 默认值：false
    """
    disabledDate: Optional[str] = None
    """用字符函数来控制哪些天不可以被点选"""

    popOverContainerSelector: Optional[str] = None
    """
    - 弹层挂载位置选择器，会通过querySelector获取
    - 版本：6.4.0 版本后支持表达式
    """

    name: Optional[str] = None
    """名称"""

    description: Optional[str] = None
    """描述"""

    format: Optional[str] = None
    """格式"""

    inputFormat: Optional[str] = None
    """输入格式"""

class InputDatetime(FormItem):
    """
    InputDatetime 日期时间

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-datetime#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-datetime"
    """指明为 input-datetime 组件"""

    value: Optional[str] = None
    """默认值"""

    valueFormat: Optional[str] = None
    """
    - 日期时间选择器值格式，更多格式类型请参考 文档
    - 默认值：'X'
    - 版本：3.4.0 版本后支持
    """

    displayFormat: Optional[str] = None
    """
    - 日期时间选择器显示格式，即时间戳格式，更多格式类型请参考 文档
    - 默认值：'YYYY-MM-DD HH:mm:ss'
    - 版本：3.4.0 版本后支持
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择日期以及时间'
    """

    shortcuts: Optional[Union[str, list[str], list[dict]]] = None
    """
    - 日期时间快捷键
    - 版本：3.1.0 版本后支持表达式
    """

    minDate: Optional[str] = None
    """限制最小日期时间"""

    maxDate: Optional[str] = None
    """限制最大日期时间"""

    utc: Optional[bool] = None
    """
    - 保存 utc 值
    - 默认值：false
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    embed: Optional[bool] = None
    """
    - 是否内联
    - 默认值：false
    """

    timeConstraints: Optional[dict] = None
    """
    - 请参考 input-time 里的说明
    - 默认值：true
    """

    isEndDate: Optional[dict] = None
    """
    - 如果配置为 true，会自动默认为 23:59:59 秒
    - 默认值：false
    """

    disabledDate: Optional[str] = None
    """用字符函数来控制哪些天不可以被点选"""

    popOverContainerSelector: Optional[str] = None
    """
    - 弹层挂载位置选择器，会通过querySelector获取
    - 版本：6.4.0 版本后支持
    """

class InputMonth(FormItem):
    """
    InputMonth 月份

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-month#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-month-range"
    """指明为 input-month-range 组件"""

    value: Optional[str] = None
    """默认值"""

    valueFormat: Optional[str] = None
    """
    - 月份选择器值格式，更多格式类型请参考 moment
    - 默认值：'X'
    - 版本：3.4.0 版本后支持
    """

    displayFormat: Optional[str] = None
    """
    - 月份选择器显示格式，即时间戳格式，更多格式类型请参考 moment
    - 默认值：'YYYY-MM'
    - 版本：3.4.0 版本后支持
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择月份'
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    popOverContainerSelector: Optional[bool] = None
    """
    - 弹层挂载位置选择器，会通过querySelector获取
    - 版本：6.4.0
    """

class InputDateRange(FormItem):
    """
    InputDateRange 日期范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-date-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-date-range"
    """指明为 input-date-range 组件"""

    valueFormat: Optional[str] = None
    """
    - 日期选择器值格式
    - 默认值：'X'
    - 版本：3.4.0 版本后支持
    """

    displayFormat: Optional[str] = None
    """
    - 日期时间选择器显示格式，即时间戳格式，更多格式类型请参考 文档
    - 默认值：'YYYY-MM-DD'
    - 版本：3.4.0 版本后支持
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择日期范围'
    """

    shortcuts: Optional[Union[str, list[str], list[dict]]] = None
    """
    - 日期时间快捷键
    - 版本：3.1.0 版本后支持表达式
    """

    minDate: Optional[str] = None
    """限制最小日期时间"""

    maxDate: Optional[str] = None
    """限制最大日期时间"""

    minDuration: Optional[str] = None
    """限制最小跨度，如： 2days"""

    maxDuration: Optional[str] = None
    """限制最大跨度，如：1year"""

    utc: Optional[bool] = None
    """
    - 保存 utc 值
    - 默认值：false
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    embed: Optional[bool] = None
    """
    - 是否内联
    - 默认值：false
    """

    animation: Optional[bool] = None
    """
    - 是否启用游标动画
    - 默认值：false
    - 版本：2.2.0
    """

    extraName: Optional[str] = None
    """
    - 是否存成两个字段
    - 版本：3.3.0
    """

    transform: Optional[str] = None
    """
    - 日期数据处理函数，用来处理选择日期之后的的值，返回值为 Moment对象
    - 版本：3.5.0
    """

    popOverContainerSelector: Optional[str] = None
    """
    - 弹层挂载位置选择器，会通过querySelector获取
    - 版本：6.4.0 版本后支持
    """

class InputDatetimeRange(FormItem):
    """
    InputDatetimeRange 日期时间范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-datetime-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-datetime-range"
    """指明为 input-datetime-range 组件"""

    valueFormat: Optional[str] = None
    """
    - 日期选择器值格式
    - 默认值：'X'
    - 版本：3.4.0 版本后支持
    """

    displayFormat: Optional[str] = None
    """
    - 日期时间选择器显示格式，即时间戳格式，更多格式类型请参考 文档
    - 默认值：'YYYY-MM-DD'
    - 版本：3.4.0 版本后支持
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择日期范围'
    """

    shortcuts: Optional[Union[str, list[str], list[dict]]] = None
    """
    - 日期时间快捷键
    - 版本：3.1.0 版本后支持表达式
    """

    minDate: Optional[str] = None
    """限制最小日期时间"""

    maxDate: Optional[str] = None
    """限制最大日期时间"""

    utc: Optional[bool] = None
    """
    - 保存 utc 值
    - 默认值：false
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    animation: Optional[bool] = None
    """
    - 是否启用游标动画
    - 默认值：false
    - 版本：2.2.0
    """

    extraName: Optional[str] = None
    """
    - 是否存成两个字段
    - 版本：3.3.0
    """

    popOverContainerSelector: Optional[str] = None
    """
    - 弹层挂载位置选择器，会通过querySelector获取
    - 版本：6.4.0 版本后支持
    """

class InputMonthRange(FormItem):
    """
    InputMonthRange 月份范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-month-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-month-range"
    """指明为 input-month-range 组件"""

    format: Optional[str] = None
    """
    - 日期选择器值格式
    - 默认值：'X'
    - 版本：3.4.0 版本后支持
    """

    inputFormat: Optional[str] = None
    """
    - 日期选择器显示格式
    - 默认值：'YYYY-DD'
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择日期范围'
    """

    minDate: Optional[str] = None
    """限制最小日期时间"""

    maxDate: Optional[str] = None
    """限制最大日期时间"""

    minDuration: Optional[str] = None
    """限制最小跨度，如： 2days"""

    maxDuration: Optional[str] = None
    """限制最大跨度，如：1year"""

    utc: Optional[bool] = None
    """
    - 保存 utc 值
    - 默认值：false
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    embed: Optional[bool] = None
    """
    - 是否内联
    - 默认值：false
    """
    animation: Optional[bool] = None
    """
    - 是否启用游标动画
    - 默认值：false
    - 版本：2.2.0
    """

    extraName: Optional[str] = None
    """
    - 是否存成两个字段
    - 版本：3.3.0
    """

    popOverContainerSelector: Optional[str] = None
    """
    - 弹层挂载位置选择器，会通过querySelector获取
    - 版本：6.4.0 版本后支持
    """

class InputKV(FormItem):
    """
    InputKV 键值对

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-kv#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-kv"
    """指明为 input-kv 组件"""

    valueType: Optional[str] = None
    """
    - 值类型
    - 默认值: 'input-text'
    """

    keyPlaceholder: Optional[str] = None
    """key 的提示信息的"""
    valuePlaceholder: Optional[str] = None
    """value 的提示信息的"""

    draggable: Optional[bool] = None
    """
    - 是否可拖拽排序
    - 默认值: true
    """

    defaultValue: Optional[Union[str, int, dict]] = None
    """默认值"""

    autoParseJSON: Optional[bool] = None
    """
    - 是否自动转换 json 对象字符串
    - 默认值: true
    """

    keySchema: Optional[SchemaNode] = None
    """
    - 自定义 key schema
    - 版本: 3.1.0 及以上版本
    """

    valueSchema: Optional[SchemaNode] = None
    """
    - 自定义 value 的 schema
    - 版本: 3.1.0 及以上版本
    """

class InputKVS(FormItem):
    """
    InputKVS 键值对象

    - 版本: 2.1.0 及以上版本

    这个组件的功能和 input-kv 类似，input-kv 的 value 值只支持一个对象，
    input-kvs 的最大不同就是 value 支持对象和数组，可以用来支持深层结构编辑。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-kvs
    """

    type: str = "input-kvs"
    """指明为 input-kvs 组件"""

    addButtonText: Optional[str] = None
    """默认的 'New field'，而是 Add 按钮的文本"""

    draggable: Optional[bool] = None

    """默认 True，是否允许拖拽排序"""
    keyItem: Optional[SchemaNode] = None
    """key 字段"""

    valueItems: Optional[list[SchemaNode]] = None
    """键的项"""

class InputFormula(FormItem):
    """
    InputFormula 公式编辑器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-formula#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-formula"
    """指明为 input-formula 组件"""

    title: Optional[Optional[str]] = None
    """
    - 弹框标题
    - 默认值：'公式编辑器'
    """

    header: Optional[str] = None
    """编辑器 header 标题，如果不设置，默认使用表单项label字段"""

    evalMode: Optional[bool] = None
    """
    - 表达式模式 或者 模板模式，模板模式则需要将表达式写在 ${ 和 } 中间
    - 默认值：true
    """

    variables: Optional[list[dict]] = None
    """可用变量"""

    variableMode: Literal['tabs', 'tree', 'list'] = 'list'
    """
    - 可配置成 tabs 或者 tree 默认为列表，支持分组
    - 默认值：'list'
    """

    functions: Optional[list[dict]] = None
    """可以不设置，默认就是 amis-formula 里面定义的函数，如果扩充了新的函数则需要指定"""

    inputMode: Optional[Literal['button', 'input-button', 'input-group']] = None
    """控件的展示模式"""

    icon: Optional[str] = None
    """可以不设置，默认就是 amis-formula 里面定义的函数，如果扩充了新的函数则需要指定"""

    btnLabel: Optional[str] = None
    """
    - 按钮文本，inputMode为button时生效
    - 默认值：'公示编辑'
    """

    level: Optional[Literal['info', 'success', 'warning','danger','link','primary','dark','light']] = None
    """
    - 按钮样式
    - 默认值：'default'
    """

    allowInput: Optional[bool] = None
    """输入框是否可输入"""

    btnSize: Optional[Literal['xs', 'sm', 'md', 'lg']] = None
    """按钮大小"""

    borderMode: Optional[Literal['full', 'half', 'none']] = None
    """输入框边框模式"""

    placeholder: Optional[str] = None
    """
    - 输入框占位符
    - 默认值：'暂无数据'
    """

    className: Optional[str] = None
    """控件外层 CSS 样式类名"""

    variableClassName: Optional[str] = None
    """变量面板 CSS 样式类名"""

    functionClassName: Optional[str] = None
    """函数面板 CSS 样式类名"""

    mixedMode: Optional[bool] = None
    """混合模式"""

class DiffEditor(FormItem):
    """
    DiffEditor 对比编辑器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/diff-editor#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "diff-editor"
    """指明为 diff-editor 组件"""

    language: Optional[str] = None
    """编辑器高亮的语言，可选 支持的语言"""

    diffValue: Optional[Template] = None
    """左侧值"""

class Editor(FormItem):
    """
    Editor 编辑器

    用于实现代码编辑，如果要实现富文本编辑请使用 Rich-Text。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/editor
    """

    type: str = "editor"
    """指定 editor 渲染器"""

    language: Optional[str] = None
    """编辑器高亮的语言，支持通过 ${xxx} 变量获取"""

    size: Optional[str] = None
    """编辑器高度，取值可以是 md、lg、xl、xxl"""

    allowFullscreen: Optional[bool] = None
    """是否显示全屏模式开关"""

    options: Optional[dict] = None
    """monaco 编辑器的其它配置，比如是否显示行号等，请参考这里，不过无法设置 readOnly，只读模式需要使用 disabled: true"""

    placeholder: Optional[str] = None
    """占位描述，没有值的时候展示"""

class FieldSet(FormItem):
    type: str = 'fieldSet'
    """
    FieldSet 表单项集合

    FieldSet 是用于分组展示表单项的一种容器型组件，可以折叠。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/fieldset#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    className: Optional[str] = None
    """CSS 类名"""

    headingClassName: Optional[str] = None
    """标题 CSS 类名"""

    bodyClassName: Optional[str] = None
    """内容区域 CSS 类名"""

    title: Optional[SchemaNode] = None
    """标题"""

    body: Optional['FormItem'] = None
    """表单项集合"""

    mode: Optional[str] = None
    """展示默认，同 Form 中的模式"""

    collapsable: Optional[bool] = None
    """是否可折叠"""

    collapsed: Optional[bool] = None
    """默认是否折叠"""

    collapseTitle: Optional[SchemaNode] = None
    """收起的标题"""

    size: Optional[Literal['xs', 'sm', 'base', 'md', 'lg']] = None
    """大小"""

class InputExcel(AmisNode):
    """
    InputExcel 解析 Excel

    - 2.10.0 以上版本支持 xls 文件格式，2.9.0 及以下版本只支持 xlsx

    这个组件是通过前端对 Excel 进行解析，将结果作为表单项，使用它有两个好处：

    1.节省后端开发成本，无需再次解析 Excel

    2.可以前端实时预览效果，比如配合 input-table 组件进行二次修改

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-excel#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = 'input-excel'

    allSheets: Optional[bool] = None
    """是否解析所有 sheet"""

    parseMode: Optional[str] = None
    """解析模式"""

    includeEmpty: Optional[bool] = None
    """是否包含空值"""

    plainText: Optional[bool] = None
    """是否解析为纯文本"""

    placeholder: Optional[str] = None
    """
    - 占位文本提示
    - 默认值："拖拽 Excel 到这，或点击上传"
    - 版本：2.8.1	
    """

    autoFill: Optional[dict[str, str]] = None
    """
    - 自动填充
    - 版本：3.5.0
    """

class InputFile(FormItem):
    """
    InputFile 文件上传

    参考: https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-file#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-file"

    receiver: Optional[API] = None
    """
    - 上传文件接口
    - 默认值：'text/plain'
    """

    accept: Optional[str] = None
    """
    - 默认只支持纯文本，要支持其他类型，请配置此属性为文件后缀.xxx
    - 默认值：'text/plain'
    """

    capture: Optional[str] = None
    """
    - 用于控制 input[type=file] 标签的 capture 属性，在移动端可控制输入来源
    - 默认值：'undefined'
    """

    asBase64: Optional[bool] = None
    """
    - 将文件以base64的形式，赋值给当前组件
    - 默认值：false
    """

    asBlob: Optional[bool] = None
    """
    - 将文件以二进制的形式，赋值给当前组件
    - 默认值：false
    """

    maxSize: Optional[int] = None
    """
    - 默认没有限制，当设置后，文件大小大于此值将不允许上传。单位为B
    - 默认值：false
    """

    maxLength: Optional[int] = None
    """默认没有限制，当设置后，一次只允许上传指定数量文件"""

    multiple: Optional[bool] = None
    """是否多选"""

    drag: Optional[bool] = None
    """
    - 是否为拖拽上传
    - 默认值：false
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    delimiter: Optional[str] = None
    """
    - 拼接符
    - 默认值：','
    """

    autoUpload: Optional[bool] = None
    """
    - 否选择完就自动开始上传
    - 默认值：true
    """

    hideUploadButton: Optional[bool] = None
    """
    - 隐藏上传按钮
    - 默认值：false
    """

    stateTextMap: Optional[dict] = None
    """
    - 上传状态文案
    - 默认值：{ init: '', pending: '等待上传', uploading: '上传中', error: '上传出错', uploaded: '已上传', ready: '' }
    """

    fileField: Optional[str] = None
    """
    - 如果你不想自己存储，则可以忽略此属性。
    - 默认值：'file'
    """

    nameField: Optional[str] = None
    """
    - 接口返回哪个字段用来标识文件名
    - 默认值：'name'
    """

    valueField: Optional[str] = None
    """
    - 文件的值用那个字段来标识
    - 默认值：'value'
    """

    urlField: Optional[str] = None
    """
    - 文件下载地址的字段名
    - 默认值：'url'
    """

    btnLabel: Optional[str] = None
    """上传按钮的文字"""

    downloadUrl: Optional[Union[bool, str]] = None
    """
    - 默认显示文件路径的时候会支持直接下载，可以支持加前缀如：http://xx.dom/filename= ，如果不希望这样，可以把当前配置项设置为 false
    - 版本： 1.1.6 版本开始支持
    """

    useChunk: Optional[bool] = None
    """
    - amis 所在服务器，限制了文件上传大小不得超出 10M，所以 amis 在用户选择大文件的时候，自动会改成分块上传模式
    - 默认值：'auto'
    """

    chunkSize: Optional[int] = None
    """
    - 分块大小
    - 默认值：5 * 1024 * 1024
    """

    startChunkApi: Optional[API] = None
    """启动块接口"""

    chunkApi: Optional[API] = None
    """块接口"""

    finishChunkApi: Optional[API] = None
    """完成块接口"""

    concurrency: Optional[int] = None
    """分块上传时并行个数"""

    documentation: Optional[str] = None
    """文档内容"""

    documentLink: Optional[str] = None
    """文档链接"""

    autoFill: Optional[dict[str, str]] = None
    """
    - 初表单反显时是否执行
    - 默认值：true
    """

class Formula(AmisNode):
    """
    Formula 公式

    可以设置公式，将公式结果设置到指定表单项上。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/formula#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "formula"

    name: Optional[str] = None
    "需要应用的表单项name值，公式结果将作用到此处指定的变量中去"

    formula: Optional[Expression] = None
    """应用的公式"""

    condition: Optional[Expression] = None
    """公式作用条件"""

    initSet: Optional[bool] = None
    """
    - 初始化时是否设置
    - 默认值：true
    """

    autoSet: Optional[bool] = None
    """
    - 观察公式结果，如果计算结果有变化，则自动应用到变量上
    - 默认值：true
    """

    id: Optional[bool] = None
    """定义个名字，当某个按钮的目标指定为此值后，会触发一次公式应用。这个机制可以在 autoSet 为 false 时用来手动触发"""

class Group(AmisNode):
    """
    Group 表单项组

    表单项，默认都是一行显示一个，Group 组件用于在一行展示多个表单项，
    会自动根据表单项数量均分宽度。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/group#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "group"

    className: Optional[str] = None
    """CSS 类名"""

    label: Optional[str] = None
    """group 的标签"""

    body: Optional[List['FormItem']] = None
    """表单项集合"""

    mode: Optional[str] = None
    """展示默认，同 Form 中的模式"""

    gap: Optional[Literal['xs', 'sm', 'normal']] = None
    """表单项之间的间距"""

    direction: Optional[Literal['vertical', 'horizontal']] = None
    """
    - 可以配置水平展示还是垂直展示
    - 默认值：'horizontal'
    """

class Hidden(AmisNode):
    """"
    Hidden 隐藏字段

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/form/hidden
    """
    type: Optional[str] = 'hidden'

    name: Optional[str]= None
    """对应字段名称"""

    value: Optional[int] = None
    """默认值"""

class InputImage(FormItem):
    """
    InputImage 图片

    图片格式输入，需要实现接收器，提交时将以 url 的方式提交，
    如果需要以表单方式提交请使用 InputFile。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-image#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Crop(BaseAmisModel):
        aspectRatio: Optional[float] = None
        """裁剪比例。浮点型，默认 1 即 1:1，如果要设置 16:9 请设置 1.7777777777777777 即 16 / 9。"""

        rotatable: Optional[bool] = None
        """
        - 裁剪时是否可旋转
        - 默认值：false
        """

        scalable: Optional[bool] = None
        """
        - 裁剪时是否可缩放
        - 默认值：false
        """

        viewMode: Optional[int] = None
        """
        - 裁剪时的查看模式，0 是无限制
        - 默认值：1
        """

        cropFormat: Optional[int] = None
        """
        - 裁剪文件格式
        - 默认值：'image/png'
        """

        cropQuality: Optional[int] = None
        """
        - 裁剪文件格式的质量，用于 jpeg/webp，取值在 0 和 1 之间
        - 默认值：1
        """

    class Limit(BaseAmisModel):
        width: Optional[int] = None
        """限制图片宽度"""

        height: Optional[int] = None
        """限制图片高度"""

        minWidth: Optional[int] = None
        """限制图片最小宽度"""

        minHeight: Optional[int] = None
        """限制图片最小高度"""

        maxWidth: Optional[int] = None
        """限制图片最大宽度"""

        maxHeight: Optional[int] = None
        """限制图片最大高度"""

        aspectRatio: Optional[int] = None
        """
        限制图片宽高比，格式为浮点型数字，默认 1 即 1:1，
        如果要设置 16:9 请设置 1.7777777777777777 即 16 / 9。
        如果不想限制比率，请设置空字符串。
        """

    type: str = "input-image"


    receiver: Optional[API] = None
    """上传文件接口"""

    accept: Optional[str] = None
    """
    - 支持的图片类型格式，请配置此属性为图片后缀，例如.jpg,.png
    - 默认值：'.jpeg,.jpg,.png,.gif'
    """

    capture: Optional[str] = None
    """
    - 控制 input[type=file] 标签的 capture 属性
    - 默认值：'undefined'
    """

    maxSize: Optional[int] = None
    """文件大小限制，单位为B"""

    maxLength: Optional[int] = None
    """一次只允许上传指定数量文件"""

    multiple: Optional[bool] = None
    """
    - 是否多选
    - 默认值：false
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    delimiter: Optional[str] = None
    """
    - 拼接符
    - 默认值：','
    """

    autoUpload: Optional[bool] = None
    """
    - 是否选择完自动上传
    - 默认值：true
    """

    hideUploadButton: Optional[bool] = None
    """
    - 隐藏上传按钮
    - 默认值：false
    """

    fileField: Optional[str] = None
    """
    - 文件字段名称
    - 默认值：'file'
    """

    crop: Optional[Union[bool, Crop]] = None
    """ 用来设置是否支持裁剪"""


    limit: Optional[Limit] = None
    """限制图片大小"""

    frameImage: Optional[str] = None
    """默认占位图地址"""

    fixedSize: Optional[bool] = None
    """是否开启固定尺寸"""

    fixedSizeClassName: Optional[str] = None
    """固定尺寸展示尺寸"""

    initAutoFill: Optional[bool] = None
    """
    - 表单反显时是否执行 autoFill
    - 默认值：false
    """

    uploadBtnText: Optional[Union[str, SchemaNode]]= None
    """上传按钮文案"""

    dropCrop: Optional[bool] = None
    """
    - 图片上传后是否进入裁剪模式
    - 默认值：true
    """

    initCrop: Optional[bool] = None
    """
    - 初始化后是否立即进入裁剪模式
    - 默认值：false
    """

    draggable: Optional[bool] = None
    """
    - 是否支持拖拽排序
    - 默认值：false
    """

    draggableTip: Optional[str] = None
    """
    - 拖拽提示文案
    - 默认值：'拖拽排序'
    """

class InputGroup(FormItem):
    """
    Input-Group 输入框组合

    输入框组合选择器 可用于输入框与其他组件进行组合。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-group#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class ValidationConfig(BaseModel):
        errorMode: Optional[Literal['full', 'partial']] = None
        """
        - 错误提示风格, full: 整体飘红,partial: 仅错误元素飘红
        - 默认值：'full'
        """

        delimiter: Optional[str] = None
        """
        - 单个子元素多条校验信息的分隔符
        - 默认值：';'
        """

    type: str = "input-group"

    className: Optional[str] = None
    """CSS 类名"""

    body: Optional[list[Union[FormItem, AmisNode]]] = None
    """表单项集合"""

    validationConfig: Optional[ValidationConfig] = None
    """
    - 校验相关配置
    - 版本：2.8.0
    """

class ListSelect(FormItem):
    """
    ListSelect 选择器

    ListSelect 一般用来实现选择，可以单选也可以多选，和 Radio/Checkboxs 最大的不同是在展现方面支持带图片。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/list-select#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "list-select"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[API] = None
    """动态选项组"""

    multiple: Optional[bool] = None
    """
    - 是否多选
    - 默认值：false
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值："label"
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值："value"
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    autoFill: Optional[dict] = None
    """自动填充"""

    listClassName: Optional[str] = None
    """支持配置 list div 的 CSS 类名"""

class LocationPicker(FormItem):
    """
    LocationPicker 地理位置

    参数：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/location-picker#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class LocationData(BaseAmisModel):
        address: str
        """地址信息"""

        lng: float
        """
        - 经度
        - 范围：[-180, 180]
        """

        lat: float
        """
        - 维度
        - 范围：[-90, 90]
        """

        vendor: Optional[Literal['baidu', 'gaode']] = None
        """地图厂商类型"""


    type: str = "location-picker"

    value: Optional[LocationData] = None
    """参考 LocationData"""

    vendor: Optional[Literal['baidu', 'gaode']] = None
    """
    - 地图厂商
    - 默认值：'baidu'
    """

    ak: Optional[str] = None
    """百度/高德地图的 ak"""

    clearable: Optional[bool] = None
    """
    - 输入框是否可清空
    - 默认值：false
    """

    placeholder: Optional[str] = None
    """
    - 默认提示
    - 默认值：'请选择位置'
    """

    autoSelectCurrentLoc: Optional[bool] = None
    """
    - 是否自动选中当前地理位置
    - 默认值：false
    """

    onlySelectCurrentLoc: Optional[bool] = None
    """
    - 是否限制只能选中当前地理位置
    - 默认值：false
    """

    coordinatesType: Optional[Literal['bd09', 'gcj02']] = None
    """
    - 坐标系类型
    - 默认值：'bd09'
    """

class UUID(AmisNode):
    """
    UUID 字段

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/uuid
    """

    type: str = "uuid"

    name: Optional[str] = None
    """字段名称"""

    length: Optional[int] = None
    """如果设置，则生成短随机数，如果未设置，则生成 UUID"""

class MatrixCheckboxes(FormItem):
    """
    MatrixCheckboxes 矩阵

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/form/matrix-checkboxes#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class RowItem(AmisNode):
        label: str

    class ColumnItem(AmisNode):
        label: str

    type: str = "matrix-checkboxes"

    columns: Optional[List[ColumnItem]]
    """列信息，数组中 label 字段是必须给出的"""

    rows: Optional[List[RowItem]] = None
    """行信息，数组中 label 字段是必须给出的"""

    rowLabel: Optional[str] = None
    """行标题说明"""

    source: Optional[API] = None
    """API 地址，如果选项组不固定，可以通过配置 source 动态拉取"""

    multiple: Optional[bool] = None
    """
    - 是否多选
    - 默认值：true
    """

    singleSelectMode: Optional[Literal['cell', 'row', 'column']] = None
    """
    - 设置单选模式，multiple为false时有效
    - 默认值：'column'
    """

    textAlign: Optional[str] = None
    """
    - 当开启多选+全选时
    - 默认值：'center'
    """

    yCheckAll: Optional[bool] = None
    """
    - 列上的全选
    - 默认值：false
    """

    xCheckAll: Optional[bool] = None
    """
    - 行上的全选
    - 默认值：false
    """

class NestedSelect(FormItem):
    """
    NestedSelect 级联选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/nestedselect#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "nested-select"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    delimiter: Optional[bool] = None
    """
    - 拼接符
    - 默认值：false
    """

    labelField: Optional[bool] = None
    """
    - 选项标签字段
    - 默认值：'label'
    """

    valueField: Optional[bool] = None
    """
    - 选项值字段
    - 默认值：'value'
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    autoFill: Optional[Dict[str, Any]] = None
    """自动填充"""

    cascade: Optional[bool] = None
    """
    - 设置 true时，当选中父节点时不自动选择子节点
    - 默认值：false
    """

    withChildren: Optional[bool] = None
    """
    - 选中父节点时，值里面将包含子节点的值
    - 默认值：false
    """

    onlyChildren: Optional[bool] = None
    """
    - 多选时，选中父节点时，是否只将其子节点加入到值中
    - 默认值：false
    """

    searchable: Optional[bool] = None
    """
    - 可否搜索
    - 默认值：false
    """

    searchPromptText: Optional[str] = None
    """
    - 搜索框占位文本
    - 默认值：'输入内容进行检索'
    """

    noResultsText: Optional[str] = None
    """
    - 无结果时的文本
    - 默认值：'未找到任何结果'
    """

    multiple: Optional[bool] = None
    """
    - 可否多选
    - 默认值：false
    """

    hideNodePathLabel: Optional[bool] = None
    """
    - 是否隐藏选择框中已选择节点的路径 label 信息
    - 默认值：false
    """

    onlyLeaf: Optional[bool] = None
    """
    - 只允许选择叶子节点
    - 默认值：false
    """

    maxTagCount: Optional[int] = None
    """
    - 标签的最大展示数量
    - 版本：3.3.0
    """

    overflowTagPopover: Optional[Dict[str, Any]] = None
    """
    - 收纳浮层的配置属性
    - 默认值: {"placement": "top", "trigger": "hover", "showArrow": false, "offset": [0, -10]}
    - 版本：3.3.0
    """

class InputNumber(FormItem):
    """
    InputNumber 数字输入框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-number#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-number"

    min: Optional[Union[int, Template]] = None
    """最小值"""

    max: Optional[Union[int, Template]] = None
    """最大值"""

    step: Optional[int] = None
    """步长"""

    precision: Optional[int] = None
    """精度，即小数点后几位，支持 0 和正整数"""

    showSteps: Optional[bool] = None
    """
    - 是否显示上下点击按钮
    - 默认值：true
    """

    readOnly: Optional[bool] = None
    """
    - 只读
    - 默认值：false
    """

    prefix: Optional[str] = None
    """前缀"""

    suffix: Optional[str] = None
    """后缀"""

    unitOptions: Optional[List[str]] = None
    """单位选项"""

    kilobitSeparator: Optional[bool] = None
    """
    - 千分分隔
    - 默认值：false
    """

    keyboard: Optional[bool] = None
    """
    - 键盘事件（方向上下）
    - 默认值：true
    """

    big: Optional[bool] = None
    """
    - 是否使用大数
    - 默认值：false
    """

    displayMode: Optional[Literal['base', 'enhance']] = None
    """
    - 样式类型
    - 默认值：'base'
    """

    borderMode: Optional[Literal['full', 'half', 'none']] = None
    """
    - 边框模式，全边框，还是半边框，或者没边框
    - 默认值：'full'
    """

    resetValue: Optional[Union[int, str]] = None
    """
    - 清空输入内容时，组件值将设置为 resetValue
    - 默认值：""
    """

    clearValueOnEmpty: Optional[bool] = None
    """
    - 内容为空时从数据域中删除该表单项对应的值
    - 默认值：false
    """

class InputText(FormItem):
    """
    InputText 输入框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-text#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class AddOn(AmisNode):
        """
        其他参数请参考按钮文档
        """
        type: Optional[str] = None
        """请选择 text 、button 或者 submit"""

        label: Optional[str] = None
        """文字说明"""

        position: Optional[Literal['left', 'right']] = 'right'
        """addOn 位置"""



    type: str = "input-text"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    autoComplete: Optional[Union[str, API]] = None
    """自动补全"""

    multiple: Optional[bool] = None
    """是否多选"""

    delimiter: Optional[str] = None
    """
    - 拼接符
    - 默认值：','
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值：'label'
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值：'value'
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    addOn: Optional[AddOn] = None
    """输入框附加组件"""

    trimContents: Optional[bool] = None
    """是否去除首尾空白文本"""

    clearValueOnEmpty: Optional[bool] = None
    """文本内容为空时去掉这个值"""

    creatable: Optional[bool] = None
    """是否可以创建，默认为可以"""

    clearable: Optional[bool] = None
    """是否可清除"""

    resetValue: Optional[str] = None
    """
    - 清除后设置此配置项给定的值
    - 默认值：''
    """

    prefix: Optional[str] = None
    """
    - 前缀
    - 默认值：''
    """

    suffix: Optional[str] = None
    """
    - 后缀
    - 默认值：''
    """

    showCounter: Optional[bool] = None
    """是否显示计数器"""

    minLength: Optional[int] = None
    """限制最小字数"""

    maxLength: Optional[int] = None
    """限制最大字数"""

    transform: Optional[Dict[str, bool]] = None
    """自动转换值"""

    borderMode: Optional[Literal['full', 'half', 'none']] = None
    """
    - 输入框边框模式
    - 默认值："full"
    """

    inputControlClassName: Optional[str] = None
    """control 节点的 CSS 类名"""

    nativeInputClassName: Optional[str] = None
    """原生 input 标签的 CSS 类名"""

    nativeAutoComplete: Optional[str] = None
    """
    - 原生 input 标签的 autoComplete 属性
    - 默认值：'off'
    """

class InputPassword(InputText):
    """
    InputPassword 密码输入框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-password#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-password"

    revealPassword: Optional[bool] = None
    """
    - 是否展示密码显/隐按钮
    - 默认值：true
    """

class ChartRadios(FormItem):
    """
    ChartRadios 图表单选框

    图表点选功能，用来做多个图表联动

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/chart-radios#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "chained-radios"

    options: Optional[OptionsNode] = None
    """选项组"""

    config: Optional[Dict[str, Any]] = None
    """echart 图表配置"""

    showTooltipOnHighlight: Optional[bool] = None
    """
    - 高亮的时候是否显示 tooltip
    - 默认值：false
    """

    chartValueField: Optional[str] = None
    """
    - 图表数值字段名
    - 默认值："value"
    """

class InputQuarter(InputDate):
    """
    InputQuarter 季度

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-quarter#%E4%BA%8B%E4%BB%B6%E8%A1%A8
    """

    type: str = "input-quarter"

class InputQuarterRange(FormItem):
    """
    InputQuarterRange 季度范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-quarter-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-quarter-range"

    valueFormat: Optional[str] = None
    """
    - 日期选择器值格式
    - 默认值：'X'
    """

    displayFormat: Optional[str] = None
    """
    - 日期选择器显示格式
    - 默认值：'YYYY-DD'
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值："请选择季度范围"
    """

    minDate: Optional[str] = None
    """限制最小日期"""

    maxDate: Optional[str] = None
    """限制最大日期"""

    minDuration: Optional[str] = None
    """限制最小跨度，如：2quarter"""

    maxDuration: Optional[str] = None
    """限制最大跨度，如：4quarter"""

    utc: Optional[bool] = None
    """
    - 保存 UTC 值
    - 默认值：false
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    embed: Optional[bool] = None
    """
    - 是否内联模式
    - 默认值：false
    """

    animation: Optional[bool] = None
    """
    - 是否启用游标动画
    - 默认值：true
    """

    extraName: Optional[str] = None
    """是否存成两个字段"""

    popOverContainerSelector: Optional[str] = None
    """弹层挂载位置选择器"""

class InputRange(FormItem):
    """
    InputRange 滑块

    可以用于选择单个数值或数值范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-range"

    className: Optional[str] = None
    """css 类名"""

    value: Optional[Union[int, str, Dict[str, float], List[int]]] = None
    """当前值"""

    min: Optional[Union[int, str]] = None
    """
    - 最小值，支持变量
    - 默认值：0
    """

    max: Optional[Union[int, str]] = None
    """
    - 最大值，支持变量
    - 默认值：100
    """

    disabled: Optional[bool] = None
    """
    - 是否禁用
    - 默认值：false
    """

    step: Optional[Union[int, str]] = None
    """
    - 步长，支持变量
    - 默认值：1
    """

    showSteps: Optional[bool] = None
    """
    - 是否显示步长
    - 默认值：false
    """

    parts: Optional[Union[int, List[int]]] = None
    """
    - 分割的块数
    - 默认值：1
    """

    marks: Optional[Dict[Union[int, str], Union[str, int, Dict[str, Any]]]] = None
    """刻度标记，支持自定义样式"""

    tooltipVisible: Optional[bool] = None
    """
    - 是否显示滑块标签
    - 默认值：false
    """

    tooltipPlacement: Optional[Literal['top', 'right', 'bottom', 'left']] = None
    """
    - 滑块标签的位置
    - 默认值：'top'
    """

    tipFormatter: Optional[Callable[[Any], Any]] = None
    """控制滑块标签显隐函数"""

    multiple: Optional[bool] = None
    """
    - 支持选择范围
    - 默认值：false
    """

    joinValues: Optional[bool] = None
    """
    - 默认为 true，选择的 value 会通过 delimiter 连接起来
    - 默认值：true
    """

    delimiter: Optional[str] = None
    """
    - 分隔符
    - 默认值：','
    """

    unit: Optional[str] = None
    """单位"""

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：false
    """

    showInput: Optional[bool] = None
    """
    - 是否显示输入框
    - 默认值：false
    """

    showInputUnit: Optional[bool] = None
    """
    - 是否显示输入框单位
    - 默认值：false
    """

    onChange: Optional[Callable[[Any], None]] = None
    """当组件的值发生改变时，会触发 onChange 事件"""

    onAfterChange: Optional[Callable[[Any], None]] = None
    """与 onmouseup 触发时机一致，把当前值作为参数传入"""

class InputRating(FormItem):
    """
    InputRating 评分

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-rating#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-rating"

    value: Optional[float] = None
    """当前值"""

    half: Optional[bool] = None
    """
    - 是否使用半星选择
    - 默认值：false
    """

    count: Optional[int] = None
    """
    - 总星数
    - 默认值：5
    """

    readOnly: Optional[bool] = None
    """
    - 只读
    - 默认值：false
    """

    allowClear: Optional[bool] = None
    """
    - 是否允许再次点击后清除
    - 默认值：true
    """

    colors: Optional[Union[str, Dict[str, str]]] = None
    """
    - 星星被选中的颜色
    - 默认值：{'2': '#abadb1', '3': '#787b81', '5': '#ffa900'}
    """

    inactiveColor: Optional[str] = None
    """
    - 未被选中的星星的颜色
    - 默认值：'#e7e7e8'
    """

    texts: Optional[Dict[str, str]] = None
    """星星被选中时的提示文字"""

    textPosition: Optional[Literal['right', 'left']] = None
    """
    - 文字的位置
    - 默认值：right
    """

    char: Optional[str] = None
    """
    - 自定义字符
    - 默认值：★
    """

    className: Optional[str] = None
    """自定义样式类名"""

    charClassName: Optional[str] = None
    """自定义字符类名"""

    textClassName: Optional[str] = None
    """自定义文字类名"""

class InputRepeat(FormItem):

    """
    InputRepeat 重复频率选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-repeat#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-repeat"

    options: Optional[str] = None
    """
    - 可用配置 secondly,minutely,hourly,daily,weekdays,weekly,monthly,yearly
    - 默认值：'hourly,daily,weekly,monthly'
    """

    placeholder: Optional[str] = None
    """
    - 当不指定值时的说明
    - 默认值：'不重复'
    """

class InputRichText(FormItem):
    """
    InputRichText 富文本编辑器

    目前富文本编辑器基于两个库：froala 和 tinymce，默认使用 tinymce。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-rich-text#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-rich-text"

    saveAsUbb: Optional[bool] = None
    """是否保存为 ubb 格式"""

    receiver: Optional[API] = None
    """默认的图片保存 API"""

    videoReceiver: Optional[API] = None
    """默认的视频保存 API，仅支持 froala 编辑器"""

    fileField: Optional[str] = None
    """上传文件时的字段名"""

    size: Optional[Literal['md', 'lg']] = None
    """框的大小"""

    options: Optional[Dict[str, Any]] = None
    """需要参考 tinymce 或 froala 的文档"""

    buttons: Optional[List[str]] = None
    """froala 专用，配置显示的按钮"""

    vendor: Optional[Literal['froala']] = None
    """只需要加一行 "vendor": "froala" 配置就行，froala 是付费产品，需要设置 richTextToken 才能去掉水印"""

class InputSignature(AmisNode):
    """
    InputSignature 签名面板

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-signature#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    width: Optional[int] = None
    """组件宽度，最小 300"""

    height: Optional[int] = None
    """组件高度，最小 160"""

    color: Optional[str] = None
    """
    - 手写字体颜色
    - 默认值：'#000'
    """

    bgColor: Optional[str] = None
    """
    - 面板背景颜色
    - 默认值：'#EFEFEF'
    """

    clearBtnLabel: Optional[str] = None
    """
    - 清空按钮名称
    - 默认值：'清空'
    """

    undoBtnLabel: Optional[str] = None
    """
    - 撤销按钮名称
    - 默认值：'撤销'
    """

    confirmBtnLabel: Optional[str] = None
    """
    - 确认按钮名称
    - 默认值：'确认'
    """

    embed: Optional[bool] = None
    """是否内嵌"""

    embedConfirmLabel: Optional[str] = None
    """
    - 内嵌容器确认按钮名称
    - 默认值：'确认'
    """

    ebmedCancelLabel: Optional[str] = None
    """
    - 内嵌容器取消按钮名称
    - 默认值：'取消'
    """

    embedBtnIcon: Optional[str] = None
    """内嵌按钮图标"""

    embedBtnLabel: Optional[str] = None
    """
    - 内嵌按钮文案
    - 默认值：'点击签名'
    """

class InputSubForm(FormItem):
    """
    InputSubForm 子表单

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-sub-form#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-sub-form"

    multiple: Optional[bool] = None
    """
    - 是否为多选模式
    - 默认值：false
    """

    labelField: Optional[str] = None
    """当值中存在这个字段，则按钮名称将使用此字段的值来展示。"""

    btnLabel: Optional[str] = None
    """
    - 按钮默认名称
    - 默认值："设置"
    """

    minLength: Optional[int] = None
    """
    - 限制最小个数。
    - 默认值：0
    """

    maxLength: Optional[int] = None
    """
    - 限制最大个数。
    - 默认值：0
    """

    draggable: Optional[bool] = None
    """是否可拖拽排序"""

    addable: Optional[bool] = None
    """是否可新增"""

    removable: Optional[bool] = None
    """是否可删除"""

    addButtonClassName: Optional[str] = None
    """
    - 新增按钮 CSS 类名
    - 默认值：""
    """

    itemClassName: Optional[str] = None
    """
    - 值元素 CSS 类名
    - 默认值：""
    """

    itemsClassName: Optional[str] = None
    """
    - 值包裹元素 CSS 类名
    - 默认值：""
    """

    form: Optional[Form] = None
    """子表单配置，同 Form"""

    addButtonText: Optional[str] = None
    """
    - 自定义新增一项的文本
    - 默认值：""
    """

    showErrorMsg: Optional[bool] = None
    """
    - 是否在左下角显示报错信息
    - 默认值：true
    """

class InputTable(FormItem):
    """
    InputTable 表格

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-table#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-table"

    addable: Optional[bool] = None
    """
    - 是否可增加一行
    - 默认值：false
    """

    copyable: Optional[bool] = None
    """
    - 是否可复制一行
    - 默认值：false
    """

    copyData: Optional[Dict[str, Any]] = None
    """控制复制时的数据映射，不配置时复制整行数据"""

    childrenAddable: Optional[bool] = None
    """
    - 是否可增加子级节点
    - 默认值：false
    """

    editable: Optional[bool] = None
    """
    - 是否可编辑
    - 默认值：false
    """

    removable: Optional[bool] = None
    """
    - 是否可删除
    - 默认值：false
    """

    showTableAddBtn: Optional[bool] = None
    """
    - 是否显示表格操作栏添加按钮
    - 默认值：true
    """

    showFooterAddBtn: Optional[bool] = None
    """
    - 是否显示表格下方添加按钮
    - 默认值：true
    """

    addApi: Optional[API] = None
    """新增时提交的 API"""

    footerAddBtn: Optional[SchemaNode] = None
    """底部新增按钮配置"""

    updateApi: Optional[API] = None
    """修改时提交的 API"""

    deleteApi: Optional[API] = None
    """删除时提交的 API"""

    addBtnLabel: Optional[str] = None
    """增加按钮名称"""

    addBtnIcon: Optional[str] = None
    """
    - 增加按钮图标
    - 默认值："plus"
    """

    subAddBtnLabel: Optional[str] = None
    """子级增加按钮名称"""

    subAddBtnIcon: Optional[str] = None
    """
    - 子级增加按钮图标
    - 默认值："sub-plus"
    """

    copyBtnLabel: Optional[str] = None
    """复制按钮文字"""

    copyBtnIcon: Optional[str] = None
    """
    - 复制按钮图标
    - 默认值："copy"
    """

    editBtnLabel: Optional[str] = None
    """
    - 编辑按钮名称
    - 默认值：""
    """

    editBtnIcon: Optional[str] = None
    """
    - 编辑按钮图标
    - 默认值："pencil"
    """

    deleteBtnLabel: Optional[str] = None
    """
    - 删除按钮名称
    - 默认值：""
    """

    deleteBtnIcon: Optional[str] = None
    """
    - 删除按钮图标
    - 默认值："minus"
    """

    confirmBtnLabel: Optional[str] = None
    """
    - 确认编辑按钮名称
    - 默认值：""
    """

    confirmBtnIcon: Optional[str] = None
    """
    - 确认编辑按钮图标
    - 默认值："check"
    """

    cancelBtnLabel: Optional[str] = None
    """
    - 取消编辑按钮名称
    - 默认值：""
    """

    cancelBtnIcon: Optional[str] = None
    """
    - 取消编辑按钮图标
    - 默认值："times"
    """

    needConfirm: Optional[bool] = None
    """
    - 是否需要确认操作
    - 默认值：true
    """

    canAccessSuperData: Optional[bool] = None
    """
    - 是否可以访问父级数据
    - 默认值：false
    """

    strictMode: Optional[bool] = None
    """
    - 性能优化选项
    - 默认值：true
    """

    minLength: Optional[Union[int, str]] = None
    """
    - 最小行数
    - 默认值：0
    """

    maxLength: Optional[Union[int, str]] = None
    """
    - 最大行数
    - 默认值：Infinity
    """

    perPage: Optional[int] = None
    """每页展示几行数据，如果不配置则不会显示分页器"""

    columns: Optional[List[Dict[str, Any]]] = None
    """列信息"""

class InputTag(FormItem):
    """
    InputTag 标签选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-tag#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-tag"

    options: Optional[OptionsNode] = None
    """选项组"""

    optionsTip: Optional[Union[List[Dict[str, Any]], List[str]]] = None
    """
    - 选项提示
    - 默认值："最近您使用的标签"
    """

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    delimiter: Optional[str] = None
    """
    - 拼接符
    - 默认值：'false'
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值：'label'
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值：'value'
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    clearable: Optional[bool] = None
    """
    - 在有值的时候是否显示一个删除图标在右侧
    - 默认值：false
    """

    resetValue: Optional[str] = None
    """
    - 删除后设置此配置项给定的值
    - 默认值：""
    """

    max: Optional[int] = None
    """允许添加的标签的最大数量"""

    maxTagLength: Optional[int] = None
    """单个标签的最大文本长度"""

    maxTagCount: Optional[int] = None
    """标签的最大展示数量"""

    overflowTagPopover: Optional[Dict[str, Any]] = None
    """
    - 收纳浮层的配置属性
    - 默认值: {"placement": "top", "trigger": "hover", "showArrow": false, "offset": [0, -10]}
    """

    enableBatchAdd: Optional[bool] = None
    """
    - 是否开启批量添加模式
    - 默认值：false
    """

    separator: Optional[str] = None
    """
    - 开启批量添加后，输入多个标签的分隔符
    - 默认值："-"
    """

class InputTime(FormItem):
    """
    InputTime 时间

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-time#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-time"

    value: Optional[str] = None
    """默认值"""

    valueFormat: Optional[str] = None
    """
    - 时间选择器值格式
    - 默认值：X
    - 3.4.0 版本后支持
    """

    displayFormat: Optional[str] = None
    """
    - 时间选择器显示格式
    - 默认值：HH:mm
    - 3.4.0 版本后支持
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值："请选择时间"
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    timeConstraints: Optional[Dict[str, bool]] = None
    """
    - 时间约束
    - 默认值：true
    """

    popOverContainerSelector: Optional[str] = None
    """弹层挂载位置选择器"""

class InputTimeRange(FormItem):
    """
    InputTimeRange 时间范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-time-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-time-range"

    valueFormat: Optional[str] = None
    """
    - 时间范围选择器值格式
    - 默认值：HH:mm
    - 3.4.0
    """

    displayFormat: Optional[str] = None
    """
    - 时间范围选择器显示格式
    - 默认值：HH:mm
    - 3.4.0
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值："请选择时间范围"
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    embed: Optional[bool] = None
    """
    - 是否内联模式
    - 默认值：false
    """

    animation: Optional[bool] = None
    """
    - 是否启用游标动画
    - 默认值：true
    - 2.2.0
    """

    extraName: Optional[str] = None
    """是否存成两个字段 - 3.3.0"""

    popOverContainerSelector: Optional[str] = None
    """弹层挂载位置选择器 - 6.4.0"""

class InputTree(FormItem):
    """
    InputTree 树形选择框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-tree#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-tree"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    autoComplete: Optional[API] = None
    """自动提示补全"""

    multiple: Optional[bool] = None
    """
    - 是否多选
    - 默认值：false
    """

    delimiter: Optional[str] = None
    """
    - 拼接符
    - 默认值：'false'
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值：'label'
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值：'value'
    """

    iconField: Optional[str] = None
    """
    - 图标值字段
    - 默认值：'icon'
    """

    deferField: Optional[str] = None
    """
    - 懒加载字段
    - 默认值：'defer'
    - 版本：3.6.0
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    creatable: Optional[bool] = None
    """
    - 新增选项
    - 默认值：false
    """

    addControls: Optional[List[FormItem]] = None
    """自定义新增表单项"""

    addApi: Optional[API] = None
    """配置新增选项接口"""

    editable: Optional[bool] = None
    """
    - 编辑选项
    - 默认值：false
    """

    editControls: Optional[List[FormItem]] = None
    """自定义编辑表单项"""

    editApi: Optional[API] = None
    """配置编辑选项接口"""

    removable: Optional[bool] = None
    """
    - 删除选项
    - 默认值：false
    """

    deleteApi: Optional[API] = None
    """配置删除选项接口"""

    searchable: Optional[bool] = None
    """
    - 是否可检索
    - 默认值：false
    - 版本：2.8.0前仅tree-select支持
    """

    hideRoot: Optional[bool] = None
    """
    - 是否隐藏根节点
    - 默认值：true
    """

    rootLabel: Optional[str] = None
    """
    - 顶级节点文字
    - 默认值："顶级"
    """

    showIcon: Optional[bool] = None
    """
    - 是否显示图标
    - 默认值：true
    """

    showRadio: Optional[bool] = None
    """
    - 是否显示单选按钮
    - 默认值：false
    """

    showOutline: Optional[bool] = None
    """
    - 是否显示树层级展开线
    - 默认值：false
    """

    initiallyOpen: Optional[bool] = None
    """
    - 默认展开所有层级
    - 默认值：true
    """

    unfoldedLevel: Optional[int] = None
    """
    - 默认展开级数
    - 默认值：1
    """

    autoCheckChildren: Optional[bool] = None
    """
    - 选中父节点时级联选择子节点
    - 默认值：true
    """

    cascade: Optional[bool] = None
    """
    - 子节点可反选
    - 默认值：false
    """

    withChildren: Optional[bool] = None
    """
    - 值包含父子节点值
    - 默认值：false
    """

    onlyChildren: Optional[bool] = None
    """
    - 值只包含子节点值
    - 默认值：false
    """

    onlyLeaf: Optional[bool] = None
    """
    - 只允许选择叶子节点
    - 默认值：false
    """

    rootCreatable: Optional[bool] = None
    """
    - 是否可以创建顶级节点
    - 默认值：false
    """

    rootCreateTip: Optional[str] = None
    """
    - 创建顶级节点的悬浮提示
    - 默认值："添加一级节点"
    """

    minLength: Optional[int] = None
    """最少选中的节点数"""

    maxLength: Optional[int] = None
    """最多选中的节点数"""

    treeContainerClassName: Optional[str] = None
    """树最外层容器类名"""

    enableNodePath: Optional[bool] = None
    """
    - 节点路径模式
    - 默认值：false
    """

    pathSeparator: Optional[str] = None
    """
    - 节点路径的分隔符
    - 默认值：'/'
    """

    highlightTxt: Optional[str] = None
    """标签中需要高亮的字符"""

    itemHeight: Optional[int] = None
    """
    - 每个选项的高度
    - 默认值：32
    """

    virtualThreshold: Optional[int] = None
    """
    - 虚拟渲染的阈值
    - 默认值：100
    """

    menuTpl: Optional[str] = None
    """选项自定义渲染 HTML 片段"""

    enableDefaultIcon: Optional[bool] = None
    """
    - 为选项添加默认的前缀 Icon
    - 默认值：true
    """

    heightAuto: Optional[bool] = None
    """
    - 自动增长高度
    - 默认值：false
    - 版本：3.0.0
    """

class InputVerificationCode(FormItem):
    """
    InputVerificationCode 验证码输入

    注意 InputVerificationCode, 可通过粘贴完成填充数据。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-verification-code#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    length: Optional[int] = None
    """
    - 验证码的长度
    - 默认值：6
    """

    masked: Optional[bool] = None
    """
    - 是否是密码模式
    - 默认值：false
    """

    separator: Optional[str] = None
    """分隔符，支持表达式"""

class InputYear(InputDate):
    """
    Year 年份选择

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-year#%E5%8A%A8%E4%BD%9C%E8%A1%A8
    """

    type: str = "input-year"

class InputYearRange(FormItem):

    """
    InputYearRange 年份范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-year-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "input-year-range"

    valueFormat: Optional[str] = None
    """
    - 年份选择器值格式
    - 默认值：X
    - 版本：3.4.0
    """

    displayFormat: Optional[str] = None
    """
    - 年份选择器显示格式
    - 默认值：'YYYY'
    - 版本：3.4.0
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择年份范围'
    """

    minDate: Optional[str] = None
    """限制最小日期"""

    maxDate: Optional[str] = None
    """限制最大日期"""

    minDuration: Optional[str] = None
    """限制最小跨度，如：2year"""

    maxDuration: Optional[str] = None
    """限制最大跨度，如：4year"""

    utc: Optional[bool] = None
    """
    - 保存 UTC 值
    - 默认值：false
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    embed: Optional[bool] = None
    """
    - 是否内联模式
    - 默认值：false
    """

    animation: Optional[bool] = None
    """
    - 是否启用游标动画
    - 默认值：true
    - 版本：2.2.0
    """

    popOverContainerSelector: Optional[str] = None
    """弹层挂载位置选择器 - 版本：6.4.0"""

class JSONSchema(AmisNode):
    """
    JSONSchema

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/json-schema#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str =  'json-schema'

    name: Optional[str] =  None
    """
    - 字段名称
    - 默认值: 'value'
    """

    label: Optional[str] = None
    """标签"""

    schema_: Optional[Union[str, Dict[str, Any]]] = Field(None, alias="schema")
    """指定 json-schema"""

class JSONSchemaEditor(AmisNode):
    """
    JSONSchema Editor

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/json-schema-editor#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = 'json-schema-editor'

    rootTypeMutable: Optional[bool] = None
    """
    - 顶级类型是否可配置
    - 默认值：false
    """

    showRootInfo: Optional[bool] = None
    """
    - 是否显示顶级类型信息
    - 默认值：false
    """

    disabledTypes: Optional[List[Literal['string', 'number', 'interger', 'object', 'number', 'array', 'boolean', 'null']]] = None
    """用来禁用默认数据类型"""

    definitions: Optional[Dict[str, Any]] = None
    """用来配置预设类型"""

    mini: Optional[bool] = None
    """用来开启迷你模式"""

    placeholder: Optional[Dict[str, Any]] =None
    """
    - 属性输入控件的占位提示文本
    - 默认值：{key: "字段名", title: "名称", description: "描述", default: "默认值", empty: "<空>"}
    - 版本：2.8.0
    """

class Picker(FormItem):
    """
    Picker 列表选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/picker#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class OverflowConfig(BaseModel):
        maxTagCount: Optional[int] = None
        """
        - 标签的最大展示数量
        - 默认值：-1
        """

        displayPosition: Optional[List[Literal['select', 'crud']]] = None
        """
        - 收纳标签生效的位置
        - 默认值：['select', 'crud']
        """

        overflowTagPopover: Optional[Dict[str, Any]] = None
        """
        - 选择器内收纳标签的 Popover 配置
        - 默认值：{"placement": "top", "trigger": "hover", "showArrow": false, "offset": [0, -10]}
        """

        overflowTagPopoverInCRUD: Optional[Dict[str, Any]]
        """
        - CRUD 顶部内收纳标签的 Popover 配置
        - 默认值：{"placement": "bottom", "trigger": "hover", "showArrow": false, "offset": [0, 10]}
        """

    type: str = "picker"

    options: Optional[Union[List[Dict[str, Any]], List[str]]] = None
    """选项组"""

    source: Optional[Union[str, Dict[str, Any]]] = None
    """动态选项组"""

    multiple: Optional[bool] = None
    """是否为多选"""

    delimiter: Optional[bool] = None
    """
    - 拼接符
    - 默认值：false
    """

    labelField: Optional[bool] = None
    """
    - 选项标签字段
    - 默认值："label"
    """

    valueField: Optional[bool] = None
    """
    - 选项值字段
    - 默认值："value"
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    autoFill: Optional[Dict[str, Any]] = None
    """自动填充"""

    modalTitle: Optional[str] = None
    """
    - 设置模态框的标题
    - 默认值：'请选择'
    """

    modalMode: Optional[Literal['dialog', 'drawer']] = None
    """
    - 设置 dialog 或者 drawer，用来配置弹出方式
    - 默认值："dialog"
    """

    pickerSchema: Optional[Optional[Union[SchemaNode]] ] = None
    """
    - 即用 List 类型的渲染，来展示列表信息，更多配置参考 CRUD
    - 默认值："{mode: 'list', listItem: {title: '${label}'}}"
    """

    embed: Optional[bool] = None
    """
    - 是否使用内嵌模式
    - 默认值：false
    """

    overflowConfig: Optional[OverflowConfig] = None
    """
    - 开启最大标签展示数量的相关配置
    - 版本：3.4.0
    """

    size: Optional[Literal['xs', 'sm', 'md', 'lg', 'xl', 'full']] = None
    """组件大小"""

class Radio(FormItem):
    """
    Radio 单选框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/radio#%E5%B1%9E%E6%80%A7%E8%A1%A8

    """

    type: str = "radio"

    option: Optional[str] = None
    """选项说明"""

    trueValue: Optional[Union[str, int, bool]] = None
    """
    - 标识真值
    - 默认值：true
    """

    falseValue: Optional[Union[str, int, bool]] = None
    """
    - 标识假值
    - 默认值：false
    """

class Radios(FormItem):
    """
    Radios 单选框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/radios#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "radios"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, Any]] = None
    """动态选项组"""

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值：'label'
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值：'value'
    """

    columnsCount: Optional[int] = None
    """
    - 选项按几列显示
    - 默认值：1
    """

    inline: Optional[bool] = None
    """
    - 是否显示为一行
    - 默认值：true
    """

    selectFirst: Optional[bool] = None
    """
    - 是否默认选中第一个
    - 默认值：false
    """

    autoFill: Optional[Dict[str, Any]] = None
    """自动填充"""

class Select(FormItem):
    """
    Select 选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/select#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "select"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[API] = None
    """动态选项组"""

    autoComplete: Optional[API] = None
    """自动提示补全"""

    delimiter: Optional[str] = None
    """
    - 拼接符
    - 默认值：'false'
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值：'label'
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值：'value'
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    checkAll: Optional[bool] = None
    """
    - 是否支持全选
    - 默认值：false
    """

    checkAllLabel: Optional[str] = None
    """
    - 全选的文字
    - 默认值：'全选'
    """

    checkAllBySearch: Optional[bool] = None
    """
    - 有检索时只全选检索命中的项
    - 默认值：true
    """

    defaultCheckAll: Optional[bool] = None
    """
    - 默认是否全选
    - 默认值：false
    """

    creatable: Optional[bool] = None
    """
    - 新增选项
    - 默认值：false
    """

    multiple: Optional[bool] = None
    """
    - 多选
    - 默认值：false
    """

    searchable: Optional[bool] = None
    """
    - 检索
    - 默认值：false
    """

    filterOption: Optional[str] = None
    """控制选项过滤的函数"""

    createBtnLabel: Optional[str] = None
    """
    - 新增选项按钮标签
    - 默认值：'新增选项'
    """

    addControls: Optional[List[FormItem]] = None
    """自定义新增表单项"""

    addApi: Optional[API] = None
    """配置新增选项接口"""

    editable: Optional[bool] = None
    """
    - 编辑选项
    - 默认值：false
    """

    editControls: Optional[List[FormItem]] = None
    """自定义编辑表单项"""

    editApi: Optional[API] = None
    """配置编辑选项接口"""

    removable: Optional[bool] = None
    """
    - 删除选项
    - 默认值：false
    """

    deleteApi: Optional[API] = None
    """配置删除选项接口"""

    autoFill: Optional[Dict[str, Any]] = None
    """自动填充"""

    menuTpl: Optional[str] = None
    """支持配置自定义菜单"""

    clearable: Optional[bool] = None
    """是否展示清空图标"""

    hideSelected: Optional[bool] = None
    """
    - 隐藏已选选项
    - 默认值：false
    """

    mobileClassName: Optional[str] = None
    """移动端浮层类名"""

    selectMode: Optional[str] = None
    """选择模式"""

    searchResultMode: Optional[str] = None
    """搜索结果展示形式"""

    columns: Optional[List[Dict[str, Any]]] = None
    """当展示形式为 table 时配置展示哪些列"""

    leftOptions: Optional[List[Dict[str, Any]]] = None
    """当展示形式为 associated 时配置左边的选项集"""

    leftMode: Optional[str] = None
    """当展示形式为 associated 时配置左边的选择形式"""

    rightMode: Optional[str] = None
    """当展示形式为 associated 时配置右边的选择形式"""

    maxTagCount: Optional[int] = None
    """标签的最大展示数量"""

    overflowTagPopover: Optional[Dict[str, Any]] = None
    """
    - 收纳浮层的配置属性
    - 默认值: {"placement": "top", "trigger": "hover", "showArrow": false, "offset": [0, -10]}
    """

    optionClassName: Optional[str] = None
    """选项 CSS 类名"""

    popOverContainerSelector: Optional[str] = None
    """弹层挂载位置选择器"""

    overlay: Optional[Dict[str, Any]] = None
    """
    - 弹层宽度与对齐方式
    - 类型: { width: string | number, align: "left" | "center" | "right" }
    """

    showInvalidMatch: Optional[bool] = None
    """
    - 选项值与选项组不匹配时选项值是否飘红
    - 默认值：false
    """

class Switch(FormItem):
    """
    Switch 开关

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/switch#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "switch"

    option: Optional[str] = None
    """选项说明"""

    onText: Optional[Union[str, dict, list]] = None
    """开启时开关显示的内容"""

    offText: Optional[Union[str, dict, list]] = None
    """关闭时开关显示的内容"""

    trueValue: Optional[Union[bool, str, int]] = None
    """
    - 标识真值
    - 默认值：true
    """

    falseValue: Optional[Union[bool, str, int]] = None
    """
    - 标识假值
    - 默认值：false
    """

    size: Optional[Literal['sm', 'md']] = None
    """
    - 开关大小
    - 默认值：'md'
    """

    loading: Optional[bool] = None
    """
    - 是否处于加载状态
    - 默认值：false
    """

class Transfer(FormItem):
    """
    Transfer 穿梭器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/transfer#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class PaginationConfig(BaseModel):
        className: Optional[str] = None
        """分页控件 CSS 类名"""

        enable: Optional[bool] = None
        """是否开启分页"""

        layout: Optional[Union[str, List[str]]] = None
        """
        - 分页结构布局
        - 默认值：["pager"]
        """

        perPageAvailable: Optional[List[int]] = None
        """
        - 指定每页可以显示多少条
        - 默认值：[10, 20, 50, 100]
        """

        maxButtons: Optional[int] = None
        """
        - 最多显示多少个分页按钮
        - 默认值：5
        """

        popOverContainerSelector: Optional[str] = None
        """切换每页条数的控件挂载点"""

    type: Literal["transfer", "transfer-picker", "tabs-transfer", "tabs-transfer-picker"] = "transfer"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    delimeter: Optional[str] = None
    """
    - 拼接符
    - 默认值：'false'
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    searchApi: Optional[API] = None
    """接口检索"""

    resultListModeFollowSelect: Optional[bool] = None
    """
    - 结果面板跟随模式
    - 默认值：false
    """

    statistics: Optional[bool] = None
    """
    - 是否显示统计数据
    - 默认值：true
    """

    selectTitle: Optional[str] = None
    """
    - 左侧的标题文字
    - 默认值："请选择"
    """

    resultTitle: Optional[str] = None
    """
    - 右侧结果的标题文字
    - 默认值："当前选择"
    """

    sortable: Optional[bool] = None
    """
    - 结果可以进行拖拽排序
    - 默认值：false
    """

    selectMode: Optional[str] = None
    """
    - 选择模式
    - 默认值：list
    """

    searchResultMode: Optional[str] = None
    """搜索结果展示形式"""

    searchable: Optional[bool] = None
    """
    - 左侧列表搜索功能
    - 默认值：false
    """

    searchPlaceholder: Optional[str] = None
    """左侧列表搜索框提示"""

    columns: Optional[List[Dict[str, Any]]] = None
    """展示哪些列"""

    leftOptions: Optional[List[Dict[str, Any]]] = None
    """左边的选项集"""

    leftMode: Optional[str] = None
    """左边的选择形式"""

    rightMode: Optional[str] = None
    """右边的选择形式"""

    resultSearchable: Optional[bool] = None
    """
    - 结果列表的检索功能
    - 默认值：false
    """

    resultSearchPlaceholder: Optional[str] = None
    """右侧列表搜索框提示"""

    menuTpl: Optional[Union[str, SchemaNode]] = None
    """自定义选项展示"""

    valueTpl: Optional[Union[str, SchemaNode]] = None
    """自定义值的展示"""

    itemHeight: Optional[int] = None
    """
    - 每个选项的高度
    - 默认值：38
    """

    virtualThreshold: Optional[int] = None
    """
    - 虚拟渲染的阈值
    - 默认值：100
    """

    pagination: Optional[PaginationConfig] = None
    """分页配置"""

class TabsTransfer(Transfer):
    """
    TabsTransfer 组合穿梭器

    在穿梭器（Transfer）的基础上扩充了左边的展示形式，
    支持 Tabs 的形式展示。对应的 options 的顶级数据，
    顶层 options 的成员支持 selectMode 配置这个 tab 下面的选项怎么展示。
    title 可以配置 tab 的标题。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/tabs-transfer#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "tabs-transfer"

class TabsTransferPicker(Transfer):
    """
    TabsTransferPicker 穿梭选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/tabs-transfer-picker#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "tabs-transfer-picker"

class Textarea(FormItem):
    """
    Textarea 多行文本输入框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/textarea#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "textarea"

    minRows: Optional[int] = None
    """
    - 最小行数
    - 默认值：3
    """

    maxRows: Optional[int] = None
    """
    - 最大行数
    - 默认值：20
    """

    trimContents: Optional[bool] = None
    """
    - 是否去除首尾空白文本
    - 默认值：true
    """

    readOnly: Optional[bool] = None
    """
    - 是否只读
    - 默认值：false
    """

    showCounter: Optional[bool] = None
    """
    - 是否显示计数器
    - 默认值：false
    """

    maxLength: Optional[int] = None
    """限制最大字数"""

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：false
    """

    resetValue: Optional[str] = None
    """
    - 清除后设置此配置项给定的值
    - 默认值：""
    """

class TransferPicker(Transfer):
    """
    TransferPicker 穿梭选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/transfer-picker#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "transfer-picker"

    borderMode: Optional[Literal['full', 'half', 'none']] = None
    """边框模式"""

    pickerSize: Optional[Literal['xs','sm', 'md', 'lg', 'xl', 'full']] = None
    """弹窗大小"""

class TreeSelect(InputTree):
    """
    TreeSelect 树形选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/treeselect#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "tree-select"

    hideNodePathLabel: Optional[bool] = None
    """
    - 是否隐藏选择框中已选择节点的路径 label 信息
    - 默认值：false
    """

    onlyLeaf: Optional[bool] = None
    """
    - 只允许选择叶子节点
    - 默认值：false
    """

    searchable: Optional[bool] = None
    """
    - 是否可检索
    - 默认值：false
    - 仅在 type 为 tree-select 的时候生效
    """

# ==================== 数据展示 ====================

class BarCode(AmisNode):

    type: str = "property"

    className: Optional[str] = None
    """外层 CSS 类名"""

    value: Optional[str] = None
    """显示的颜色值"""

    name: Optional[str] = None
    """在其他组件中，用作变量映射"""

class Calendar(AmisNode):
    """
    Calendar 日历日程

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/calendar#calendar-%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    class Schedule(AmisNode):
        startTime: str
        endTime: str
        content: Union[str, int, dict, None] = None
        className: Optional[str] = None

    type: str = "calendar"

    schedules: Union[List[Schedule], str, None] = None
    """日历中展示日程，可设置静态数据或从上下文中取数据，startTime 和 endTime 格式参考文档，className 参考背景色"""

    scheduleClassNames: Optional[List[str]] = None
    """
    - 日历中展示日程的颜色，参考背景色
    - 默认值：['bg-warning', 'bg-danger', 'bg-success', 'bg-info', 'bg-secondary']
    """

    scheduleAction: Optional[SchemaNode] = None
    """自定义日程展示"""

    largeMode: Optional[bool] = None
    """
    - 放大模式
    - 默认值：false
    """

    todayActiveStyle: Union[str, dict, None] = None
    """今日激活时的自定义样式"""

class Card(AmisNode):
    """
    Card 卡片

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/card
    """

    class Header(AmisNode):
        className: Optional[str] = None
        """头部类名"""

        title: Optional[Optional[Template]] = None
        """标题"""

        titleClassName: Optional[str] = None
        """标题类名"""

        subTitle: Optional[Template] = None
        """	副标题"""

        subTitleClassName: Optional[str] = None
        """副标题类名"""

        subTitlePlaceholder: Optional[str] = None
        """	副标题占位"""

        description: Optional[Template] = None
        """描述"""

        descriptionClassName: Optional[str] = None
        """描述类名"""

        descriptionPlaceholder: Optional[str] = None
        """描述占位"""

        avatar: Optional[Template] = None
        """图片"""

        avatarClassName: Optional[str] = None
        """
        - 图片包括层类名
        - 默认值：'pull-left thumb avatar b-3x m-r'
        """

        imageClassName: Optional[str] = None
        """图片类名"""

        avatarText: Optional[Template] = None
        """如果不配置图片，则会在图片处显示该文本"""

        avatarTextBackground: Optional[str] = None
        """设置文本背景色，它会根据数据分配一个颜色"""

        avatarTextClassName: Optional[str] = None
        """图片文本类名"""

        highlight: Optional[bool] = None
        """
        - 是否显示激活样式
        - 默认值：false
        """

        highlightClassName: Optional[str] = None
        """激活样式类名"""

        href: Optional[Template] = None
        """点击卡片跳转的链接地址"""

        blank: Optional[bool] = None
        """
        - 是否新窗口打开
        - 默认值：false
        """

    class Media(AmisNode):
        type: Optional[Literal['image', 'video']] = 'image'
        """
        - 多媒体类型
        - 默认值：'image'
        """

        url: Optional[str] = None
        """图片/视频链接"""

        position: Optional[Literal['left', 'right', 'top', 'bottom']] = None
        """
        - 多媒体位置
        - 默认值：'left'
        """

        className: Optional[str] = None
        """
        - 多媒体类名
        - 默认值：'w-44 h-28'
        """

        isLive: Optional[bool] = None
        """
        - 视频是否为直播
        - 默认值：false
        """

        autoPlay: Optional[bool] = None
        """
        - 视频是否自动播放
        - 默认值：false
        """

        poster: Union[bool, str, None] = None
        """
        - 视频封面
        - 默认值：false
        """

    type: str = "card"
    """指定为 Card 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    href: Optional[Template] = None
    """外部链接"""

    header: Optional[Union[Header, Dict]] = None
    """Card 头部内容设置"""

    body: Optional[SchemaNode] = None
    """内容容器，主要用来放置非表单项组件"""

    bodyClassName: Optional[str] = None
    """内容区域类名"""

    actions: Optional[List[Action]] = None
    """配置按钮集合"""

    actionsCount: Optional[int] = None
    """
    - 按钮集合每行个数
    - 默认值：4
    """

    itemAction: Optional[Action] = None
    """点击卡片的行为"""

    media: Optional[Media] = None
    """Card 多媒体部内容设置"""

    secondary: Optional[Template] = None
    """次要说明"""

    toolbar: Optional[List[Action]] = None
    """工具栏按钮"""

    dragging: Optional[bool] = None
    """
    - 是否显示拖拽图标
    - 默认值：false
    """

    selectable: Optional[bool] = None
    """
    - 卡片是否可选
    - 默认值：false
    """

    checkable: Optional[bool] = None
    """
    - 卡片选择按钮是否禁用
    - 默认值：true
    """

    selected: Optional[bool] = None
    """
    - 卡片选择按钮是否选中
    - 默认值：false
    """

    hideCheckToggler: Optional[bool] = None
    """
    - 卡片选择按钮是否隐藏
    - 默认值：false
    """

    multiple: Optional[bool] = None
    """
    - 卡片是否为多选
    - 默认值：false
    """

    useCardLabel: Optional[bool] = None
    """
    - 卡片内容区的表单项 label 是否使用 Card 内部的样式
    - 默认值：true
    """

class Cards(AmisNode):
    """
    Cards 卡片组

    卡片展示，不支持配置初始化接口初始化数据域，
    所以需要搭配类似像Service这样的，
    具有配置接口初始化数据域功能的组件，
    或者手动进行数据域初始化，
    然后通过source属性，
    获取数据链中的数据，完成数据展示。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/cards?page=1#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "cards"
    """cards 指定为卡片组"""

    title: Optional[Optional[str]] = None
    """标题"""

    source: Optional[DataMapping] = None
    """
    - 数据源, 获取当前数据域中的变量
    - 默认值：${items}
    """

    placeholder: Optional[str] = None
    """
    - 当没数据的时候的文字提示
    - 默认值：'暂无数据'
    """

    className: Optional[str] = None
    """外层 CSS 类名"""

    headerClassName: Optional[str] = None
    """
    - 顶部外层 CSS 类名
    - 默认值：'amis-grid-header'
    """

    footerClassName: Optional[str] = None
    """
    - 底部外层 CSS 类名
    - 默认值：'amis-grid-footer'
    """

    itemClassName: Optional[str] = None
    """
    - 卡片 CSS 类名
    - 默认值：'col-sm-4 col-md-3'
    """

    card: Optional[Card] = None
    """配置卡片信息"""

    selectable: Optional[bool] = None
    """
    - 卡片组是否可选
    - 默认值：false
    """

    multiple: Optional[bool] = None
    """
    - 卡片组是否为多选
    - 默认值：true
    """

    checkOnItemClick: Optional[bool] = None
    """点选卡片内容是否选中卡片"""

class Carousel(AmisNode):
    """
    Carousel 轮播图

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/carousel#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Option(AmisNode):
        image: Optional[str] = None
        """图片链接"""

        href: Optional[str] = None
        """图片打开网址的链接"""

        imageClassName: Optional[str] = None
        """图片类名"""

        title: Optional[Optional[str]] = None
        """图片标题"""

        titleClassName: Optional[str] = None
        """图片标题类名"""

        description: Optional[str] = None
        """图片描述"""

        descriptionClassName: Optional[str] = None
        """图片描述类名"""

        html: Optional[str] = None
        """HTML 自定义，同Tpl一致"""

    type: str = "carousel"
    """指定为 Carousel 渲染器"""

    className: Optional[str] = None
    """
    - 外层 Dom 的类名
    - 默认值：'panel-default'
    """

    options: Optional[List[Option]] = None
    """轮播面板数据"""

    itemSchema: Optional[dict] = None
    """自定义schema来展示数据"""

    auto: Optional[bool] = None
    """
    - 是否自动轮播
    - 默认值：true
    """

    interval: Optional[str] = None
    """
    - 切换动画间隔
    - 默认值：'5s'
    """

    duration: Optional[int] = None
    """
    - 切换动画间隔
    - 默认值：500
    """

    width: Optional[str] = None
    """
    - 宽度
    - 默认值：'auto'
    """

    height: Optional[str] = None
    """
    - 高度
    - 默认值：'200px'
    """

    controls: Optional[List[str]] = None
    """
    - 显示左右箭头、底部圆点索引
    - 默认值：['dots', 'arrows']
    """
    controlsTheme: Optional[Literal['light', 'dark']] = None
    """
    - 左右箭头、底部圆点索引颜色
    - 默认值：'light'
    """

    animation: Optional[Literal['fade', 'slide']] = None
    """
    - 切换动画效果
    - 默认值：'fade'
    """

    thumbMode: Optional[str] = None
    """

    - 图片默认缩放模式
    - 默认值：'"cover" | "contain"'
    """

    multiple: Optional[dict] = None
    """
    - 多图展示，count 表示展示的数量
    - 默认值：{count: 1}
    """

    alwaysShowArrow: Optional[bool] = None
    """
    - 是否一直显示箭头，为 false 时鼠标 hover 才会显示
    - 默认值：false
    """

    icons: Optional[dict] = None
    """
    - 自定义箭头图标
    - 默认值：false
    """

class Chart(AmisNode):
    """
    Chart 图表

    图表渲染器，采用 echarts 渲染，配置格式跟 echarts 相同，echarts 配置文档

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/chart#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "chart"
    """指定为 chart 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    body: Optional[SchemaNode] = None
    """内容容器"""

    api: Optional[API] = None
    """配置项接口地址"""

    source: Optional[DataMapping] = None
    """通过数据映射获取数据链中变量值作为配置"""

    initFetch: Optional[bool] = None
    """组件初始化时，是否请求接口"""

    interval: Optional[int] = None
    """刷新时间(最小 1000)"""

    config: Union[dict, str, None] = None
    """设置 eschars 的配置项,当为string的时候可以设置 function 等配置项"""

    style: Optional[dict] = None
    """设置根元素的 style"""

    width: Optional[str] = None
    """设置根元素的宽度"""

    height: Optional[str] = None
    """设置根元素的高度"""

    replaceChartOption: Optional[bool] = None
    """
    - 每次更新是完全覆盖配置项还是追加？
    - 默认值：false
    """

    trackExpression: Optional[str] = None
    """当这个表达式的值有变化时更新图表"""

    dataFilter: Optional[str] = None
    """
    自定义 echart config 转换，函数签名：function(config, echarts, data) {return config;} 
    配置时直接写函数体。其中 config 是当前 echart 配置，echarts 就是 echarts 对象，data 为上下文数据。
    """

    mapURL: Optional[API] = None
    """地图 geo json 地址"""

    mapName: Optional[str] = None
    """地图名称"""

    loadBaiduMap: Optional[str] = None
    """加载百度地图"""

class Code(AmisNode):
    """
    Code 代码高亮

    使用代码高亮的方式来显示一段代码

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/code#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "code"
    """指定为 code 渲染器"""

    className: Optional[str] = None
    """外层 CSS 类名"""

    value: Optional[str] = None
    """显示的颜色值"""

    name: Optional[str] = None
    """在其他组件中，时，用作变量映射"""

    language: Optional[str] = None
    """
    - 所使用的高亮语言
    - 默认值：plaintext
    """

    tabSize: Optional[int] = None
    """
    - 默认 tab 大小
    - 默认值：4
    """

    editorTheme: Optional[str] = None
    """
    - 主题，还有 'vs-dark'
    - 默认值：'vs'
    """

    wordWrap: Optional[bool] = None
    """
    - 是否折行
    - 默认值：true
    """

    maxHeight: Optional[Union[str, int]] = None
    """最大高度"""

class Color(AmisNode):
    type: Literal["color", "static-color"] = "color"
    """如果在 Table、Card 和 List 中，为"color"；在 Form 中用作静态展示，为"static-color"""

    className: Optional[str] = None
    """外层 CSS 类名 """

    value: Optional[str] = None
    """显示的颜色值"""

    name: Optional[str] = None
    """在其他组件中，时，用作变量映射"""

    defaultColor: Optional[str] = None
    """默认颜色值"""

    showValue: Optional[bool] = None
    """
    - 是否显示右边的颜色值
    - 默认值：true
    """

    popOverContainerSelector: Optional[bool] = None
    """弹层挂载位置选择器，会通过querySelector获取，版本 6.4.2"""

class CRUD(AmisNode):
    """
    CRUD 增删改查

    CRUD，即增删改查组件，主要用来展现数据列表，并支持各类【增】【删】【改】【查】等操作。

    注意 CRUD 所需的数据必须放 items 中，因此如果只是想显示表格类型的数据没有分页，请使用 Table。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/crud#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Messages(BaseAmisModel):
        fetchFailed: Optional[str] = None
        """获取失败时提示"""

        saveOrderFailed: Optional[str] = None
        """保存顺序失败提示"""

        saveOrderSuccess: Optional[str] = None
        """保存顺序成功提示"""

        quickSaveFailed: Optional[str] = None
        """快速保存失败提示"""

        quickSaveSuccess: Optional[str] = None
        """快速保存成功提示"""

    type: str ='crud'

    mode: Optional[Literal['table', 'cards', 'list']] = None
    """
    - 模式
    - 默认值：'table'
    """

    title: Optional[str] = None
    """
    - 可设置成空，当设置成空时，没有标题栏
    - 默认值：""
    """

    className: Optional[str] = None
    """表格外层 Dom 的类名"""

    api: Optional[API] = None
    """CRUD 用来获取列表数据的 api。"""

    deferApi: Optional[API] = None
    """当行数据中有 defer 属性时，用此接口进一步加载内容"""

    loadDataOnce: Optional[bool] = None
    """是否一次性加载所有数据（前端分页）"""

    loadDataOnceFetchOnFilter: Optional[bool] = None
    """
    - 在开启 loadDataOnce 时，filter 时是否去重新请求 api
    - 默认值：true
    """

    source: Optional[str] = None
    """数据映射接口返回某字段的值，不设置会默认使用接口返回的${items}或者${rows}，也可以设置成上层数据源的内容"""

    filter: Optional[Union[SchemaNode, Form]] = None
    """设置过滤器，当该表单提交后，会把数据带给当前 mode 刷新列表"""

    filterTogglable: Optional[Union[bool, Dict[str, str]]] = None
    """
    - 是否可显隐过滤器
    - 类型：boolean | {label: string; icon: string; activeLabel: string; activeIcon?: stirng;}
    - 默认值：false
    """

    filterDefaultVisible: Optional[bool] = None
    """
    - 设置过滤器默认是否可见。
    - 默认值：true
    """

    initFetch: Optional[bool] = None
    """
    - 是否初始化的时候拉取数据
    - 默认值：true
    """

    interval: Optional[int] = None
    """
    - 刷新时间(最低 1000)
    - 默认值：3000
    """

    silentPolling: Optional[bool] = None
    """
    - 配置刷新时是否隐藏加载动画
    - 默认值：false
    """

    stopAutoRefreshWhen: Optional[str] = None
    """通过表达式来配置停止刷新的条件"""

    stopAutoRefreshWhenModalIsOpen: Optional[bool] = None
    """
    - 当有弹框时关闭自动刷新
    - 默认值：false
    """

    syncLocation: Optional[bool] = None
    """
    - 是否将过滤条件的参数同步到地址栏
    - 默认值：true
    """

    draggable: Optional[bool] = None
    """
    - 是否可通过拖拽排序
    - 默认值：false
    """

    resizable: Optional[bool] = None
    """
    - 是否可以调整列宽度
    - 默认值：true
    """

    itemDraggableOn: Optional[bool] = None
    """用表达式来配置是否可拖拽排序"""

    saveOrderApi: Optional[API] = None
    """保存排序的 api。"""

    quickSaveApi: Optional[API] = None
    """快速编辑后用来批量保存的 API。"""

    quickSaveItemApi: Optional[API] = None
    """快速编辑配置成及时保存时使用的 API。"""

    bulkActions: Optional[List[Action]] = None
    """批量操作列表"""

    messages: Optional[Messages] = None
    """覆盖消息提示"""

    primaryField: Optional[str] = None
    """
    - 设置 ID 字段名。
    - 默认值："id"
    """

    perPage: Optional[int] = None
    """
    - 设置一页显示多少条数据。
    - 默认值：10
    """

    orderBy: Optional[str] = None
    """默认排序字段"""

    orderDir: Optional[str] = None
    """排序方向"""

    defaultParams: Optional[Dict[str, Any]] = None
    """设置默认 filter 默认参数"""

    pageField: Optional[str] = None
    """
    - 设置分页页码字段名。
    - 默认值："page"
    """

    perPageField: Optional[str] = None
    """
    - 设置分页一页显示的多少条数据的字段名。
    - 默认值："perPage"
    """

    pageDirectionField: Optional[str] = None
    """
    - 分页方向字段名
    - 默认值："pageDir"
    """

    perPageAvailable: Optional[List[int]] = None
    """
    - 设置一页显示多少条数据下拉框可选条数。
    - 默认值：[5, 10, 20, 50, 100]
    """

    orderField: Optional[str] = None
    """设置用来确定位置的字段名"""

    hideQuickSaveBtn: Optional[bool] = None
    """
    - 隐藏顶部快速保存提示
    - 默认值：false
    """

    autoJumpToTopOnPagerChange: Optional[bool] = None
    """
    - 当切分页的时候，是否自动跳顶部。
    - 默认值：false
    """

    syncResponse2Query: Optional[bool] = None
    """
    - 将返回数据同步到过滤器上。
    - 默认值：true
    """

    keepItemSelectionOnPageChange: Optional[bool] = None
    """
    - 保留条目选择
    - 默认值：true
    """

    labelTpl: Optional[str] = None
    """单条描述模板"""

    maxKeepItemSelectionLength: Optional[int] = None
    """限制最大勾选数"""

    maxItemSelectionLength: Optional[int] = None
    """限制当前页的最大勾选数"""

    headerToolbar: Optional[List[str]] = None
    """
    - 顶部工具栏配置
    - 默认值：['bulkActions', 'pagination']
    """

    footerToolbar: Optional[List[str]] = None
    """
    - 底部工具栏配置
    - 默认值：['statistics', 'pagination']
    """

    alwaysShowPagination: Optional[bool] = None
    """
    - 是否总是显示分页
    - 默认值：false
    """

    affixHeader: Optional[bool] = None
    """
    - 是否固定表头
    - 默认值：true
    """

    affixFooter: Optional[bool] = None
    """
    - 是否固定表格底部工具栏
    - 默认值：false
    """

    autoGenerateFilter: Optional[Union[Dict[str, Any], bool]] = None
    """是否开启查询区域"""

    resetPageAfterAjaxItemAction: Optional[bool] = None
    """
    - 单条数据 ajax 操作后是否重置页码为第一页
    - 默认值：false
    """

    autoFillHeight: Optional[Union[bool, Dict[str, int]]] = None
    """
    - 内容区域自适应高度
    - 类型：boolean 丨 {height: number}
    """

    canAccessSuperData: Optional[bool] = None
    """
    - 是否可以自动获取上层的数据并映射到表格行数据上
    - 默认值：true
    """

    matchFunc: Optional[str] = None
    """自定义匹配函数"""

    parsePrimitiveQuery: Optional[Any] = None
    """
    - 是否开启 Query 信息转换
    - 默认值：true
    """

    itemAction: Optional[Action] = None
    """点击一行后实现自定义动作，支持所有配置在操作中"""

class Date(AmisNode):
    """
    Date 日期时间

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/date?page=1#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Literal['date', 'static-date'] = "date"
    """如果在 Table、Card 和 List 中，为"date"；在 Form 中用作静态展示，为"static-date"""

    className: Optional[str] = None
    """外层 CSS 类名"""

    value: Optional[str] = None
    """显示的日期数值"""

    name: Optional[str] = None
    """在其他组件中，时，用作变量映射"""

    placeholder: Optional[str] = None
    """
    - 占位内容
    - 默认值：'-'
    """

    displayFormat: Optional[str] = None
    """
    - 展示格式, 更多格式类型请参考 文档，版本号 3.4.0 及以上支持
    - 默认值：'YYYY-MM-DD'
    """

    valueFormat: Optional[str] = None
    """
    - 数据格式，默认为时间戳。更多格式类型请参考 文档
    - 默认值：'X'
    """

    fromNow: Optional[bool] = None
    """
    - 是否显示相对当前的时间描述，比如: 11 小时前、3 天前、1 年前等，fromNow 为 true 时，format 不生效。
    - 默认值：false
    """

    updateFrequency: Optional[int] = None
    """
    - 更新频率， 默认为 1 分钟
    - 默认值：60000
    """

    displayTimeZone: Optional[str] = None
    """设置日期展示时区，可设置清单参考：https://gist.github.com/diogocapela/12c6617fc87607d11fd62d2a4f42b02a"""

class EachLoop(AmisNode):
    """
    Each 循环渲染器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/each#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "each"
    """指定为 Each 组件"""

    value: Optional[list] = None
    """用于循环的值"""

    name: Optional[str] = None
    """获取数据域中变量"""

    source: Optional[DataMapping] = None
    """获取数据域中变量， 支持 数据映射"""

    items: Optional[dict] = None
    """使用value中的数据，循环输出渲染器"""

    placeholder: Optional[str] = None
    """当 value 值不存在或为空数组时的占位文本"""

    itemKeyName: Optional[str] = None
    """
    - 获取循环当前数组成员
    - 默认值：'item'
    """

    indexKeyName: Optional[str] = None
    """
    - 获取循环当前索引
    - 默认值：index
    """

class GridNav(AmisNode):
    """
    GridNav 宫格导航

    宫格菜单导航，不支持配置初始化接口初始化数据域，
    所以需要搭配类似像Service、Form或CRUD这样的，
    具有配置接口初始化数据域功能的组件，或者手动进行数据域初始化，
    然后通过source属性，获取数据链中的数据，完成菜单展示。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/grid-nav#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Option(AmisNode):
        icon: Optional[str] = None
        """列表项图标"""

        text: Optional[str] = None
        """列表项文案"""

        badge: Optional['Badge'] = None
        """列表项角标，详见 Badge"""

        link: Optional[str] = None
        """内部页面路径或外部跳转 URL 地址，优先级高于 clickAction"""

        blank: Optional[bool] = None
        """是否新页面打开，link 为 url 时有效"""

        clickAction: Optional[Action] = None
        """列表项点击交互 详见 Action"""

    type: str = "grid-nav"

    className: Optional[str] = None
    """外层 CSS 类名"""

    itemClassName: Optional[str] = None
    """列表项 css 类名"""

    contentClassName: Optional[str] = None
    """列表项内容 css 类名"""

    value: Optional[List] = None
    """图片数组"""

    source: Optional[str] = None
    """数据源"""

    square: Optional[bool] = None
    """是否将列表项固定为正方形"""

    center: Optional[bool] = None
    """
    - 是否将列表项内容居中显示
    - 默认值：true
    """

    border: Optional[bool] = None
    """
    - 是否显示列表项边框
    - 默认值：true
    """

    gutter: Optional[int] = None
    """列表项之间的间距，默认单位为px"""

    reverse: Optional[bool] = None
    """是否调换图标和文本的位置"""

    iconRatio: Optional[int] = None
    """
    - 图标宽度占比，单位%
    - 默认值：60
    """

    direction: Optional[Literal["horizontal", "vertical"]] = None
    """
    - 列表项内容排列的方向
    - 默认值：'vertical'
    """

    columnNum: Optional[int] = None
    """
    - 列数
    - 默认值：4
    """

    options: Optional[List[Option]] = None
    """选项"""

class Html(AmisNode):
    """
    HTML 渲染

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/html
    """

    type: str = "html"
    """指定为 HTML 组件"""

    html: str
    """html 当你需要在 data 字段中获取变量时，请使用 Tpl"""

class Icon(AmisNode):
    """
    Icon 图标

    在 React 项目中使用 Icon 需要引入 @fortawesome/fontawesome-free，
    然后在代码中 import '@fortawesome/fontawesome-free/css/all.css'，
    还有相关的 webpack 配置，具体请参考 amis-react-starter 里的配置。

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/icon#%E4%BA%8B%E4%BB%B6%E8%A1%A8
    """

    type: str = "icon"
    """指定组件类型"""

    className: Optional[str] = None
    """外层 CSS 类名"""

    icon: Optional[Template] = None
    """icon 名称，支持 fontawesome v4 或 通过 registerIcon 注册的 icon、或使用 url"""

    vendor: Optional[str] = None
    """icon 类型，默认为fa, 表示 fontawesome v4。也支持 iconfont, 如果是 fontawesome v5 以上版本或者其他框架可以设置为空字符串"""

class Iframe(AmisNode):
    """
    Iframe

    内嵌外部站点，可用 iframe 来实现。

    参考：https://baidu.github.io/amis/zh-CN/components/iframe#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "iframe"
    """指定为 iFrame 渲染器"""

    className: Optional[str] = None
    """iFrame 的类名"""

    frameBorder: Optional[list] = None
    """frameBorder"""

    style: Optional[dict] = None
    """样式对象"""

    src: Optional[str] = None
    """iframe 地址"""

    allow: Optional[str] = None
    """	allow 配置"""

    sandbox: Optional[str] = None
    """sandbox 配置"""

    referrerpolicy: Optional[str] = None
    """referrerpolicy 配置"""

    height: Optional[Union[int, str]] = None
    """
    - iframe 高度
    - 默认值：100%
    """

    width: Optional[Union[int, str]] = None
    """
    - iframe 宽度
    - 默认值：100%
    """

class Image(AmisNode):
    """
    Image 图片

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/image#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Literal['image', 'static-image'] = "image"
    """如果在 Table、Card 和 List 中，为'image'；在 Form 中用作静态展示，为'static-image'"""

    className: Optional[str] = None
    """外部 CSS 类名"""

    innerClassName: Optional[str] = None
    """组件内层 CSS 类名"""

    imageClassName: Optional[str] = None
    """图像 CSS 类名"""

    thumbClassName: Optional[str] = None
    """图片缩率图 CSS 类名"""

    height: Optional[int] = None
    """图片缩率高度"""

    width: Optional[int] = None
    """图片缩率宽度"""

    title: Optional[Optional[str]] = None
    """标题"""

    imageCaption: Optional[str] = None
    """描述"""

    placeholder: Optional[str] = None
    """占位文本"""

    defaultImage: Optional[str] = None
    """无数据时显示的图片"""

    src: Optional[str] = None
    """缩略图地址"""

    href: Optional[Template] = None
    """外部链接地址"""

    originalSrc: Optional[str] = None
    """原图地址"""

    enlargeAble: Optional[bool] = None
    """支持放大预览"""

    enlargeTitle: Optional[str] = None
    """放大预览的标题"""

    enlargeCaption: Optional[str] = None
    """放大预览的描述"""

    enlargeWithGallary: Optional[str] = None
    """
    - 在表格中，图片的放大功能会默认展示所有图片信息，设置为false将关闭放大模式下图片集列表的展示
    - 默认值：true
    """

    thumbMode: Optional[Literal["w-full", "h-full", "contain", "cover"]] = None
    """
    - 预览图模式
    - 默认值：'contain'
    """

    thumbRatio: Optional[Literal["1:1", "4:3", "16:9"]] = None
    """
    - 预览图比例
    - 默认值：'1:1'
    """

    imageMode: Optional[Literal['thumb', 'original']] = None
    """
    - 图片展示模式，缩略图模式 或者 原图模式
    - 默认值：'thumb'
    """
    showToolbar: Optional[bool] = None
    """放大模式下是否展示图片的工具栏，版本号 2.2.0 以上"""

    toolbarActions: Optional[list['ImageAction']] = None
    """图片工具栏，支持旋转，缩放，默认操作全部开启，版本号 2.2.0 以上"""

    maxScale: Optional[Union[int, Template]] = None
    """执行调整图片比例动作时的最大百分比，版本号 3.4.4 以上"""

    minScale: Optional[Union[int, Template]] = None
    """执行调整图片比例动作时的最小百分比，版本号 3.4.4 以上"""

class ImageAction(AmisNode):
    key: Literal['rotateRight', 'rotateLeft', 'zoomIn', 'zoomOut', 'scaleOrigin']
    """操作key"""

    label: Optional[str] = None
    """动作名称"""

    icon: Optional[str] = None
    """动作icon"""

    iconClassName: Optional[str] = None
    """动作自定义CSS类"""

    disabled: Optional[bool] = None
    """动作是否禁用"""

class Images(AmisNode):
    """
    Images 图片集

    图片集展示，不支持配置初始化接口初始化数据域，
    所以需要搭配类似像Service、Form或CRUD这样的，
    具有配置接口初始化数据域功能的组件，或者手动进行数据域初始化，
    然后通过source属性，获取数据链中的数据，完成数据展示。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/images#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Literal['images', 'static-images'] = 'images'
    """如果在 Table、Card 和 List 中，为'images'；在 Form 中用作静态展示，为'static-images'"""

    className: Optional[str] = None
    """	外层 CSS 类名"""

    defaultImage: Optional[str] = None
    """默认展示图片"""

    value: Union[str, List[str], List[dict], None] = None
    """图片数组"""

    options: Optional[list['ImageData']] = None
    """数据源"""

    source: Optional[str] = None
    """数据源"""

    delimiter: Optional[str] = None
    """
    - 分隔符，当 value 为字符串时，用该值进行分隔拆分
    - 默认值：','
    """

    src: Optional[str] = None
    """预览图地址，支持数据映射获取对象中图片变量"""

    originalSrc: Optional[DataMapping] = None
    """原图地址，支持数据映射获取对象中图片变量"""

    enlargeAble: Optional[bool] = None
    """支持放大预览"""

    enlargeWithGallary: Optional[bool] = None
    """默认在放大功能展示图片集的所有图片信息；表格中使用时，设置为true将展示所有行的图片信息；设置为false将关闭放大模式下图片集列表的展示"""

    thumbMode: Optional[Literal["w-full", "h-full", "contain", "cover"]] = None
    """
    - 预览图模式
    - 默认值：'contain'
    """

    thumbRatio: Optional[Literal["1:1", "4:3", "16:9"]] = None
    """
    - 预览图比例
    - 默认值：'1:1'
    """

    showToolbar: Optional[bool] = None
    """放大模式下是否展示图片的工具栏，版本号 2.2.0 以上"""

    toolbarActions: Optional[list[ImageAction]] = None
    """图片工具栏，支持旋转，缩放，默认操作全部开启，版本号 2.2.0 以上"""

class ImageData(AmisNode):
    image: str
    """小图，预览图"""

    src: Optional[str] = None
    """原图"""

    title: Optional[str] = None
    """标题"""

    description: Optional[str] = None
    """描述"""

class JSON(AmisNode):
    """
    JSON 展示组件

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/json#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Literal['json', 'static-json'] = 'json'
    """如果在 Table、Card 和 List 中，为'json'；在 Form 中用作静态展示，为'static-json'"""

    className: Optional[str] = None
    """外层 CSS 类名"""

    value: Optional[Union[dict, str]]= None
    """json 值，如果是 string 会自动 parse"""

    source: Optional[str] = None
    """json 值，如果是 string 会自动 parse"""

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'-'
    """

    levelExpand: Optional[int] = None
    """
    - 默认展开的层级
    - 默认值：1
    """

    jsonTheme: Optional[Literal['twilight', 'eighties']] = None
    """
    - 主题
    - 默认值：'twilight'
    """

    mutable: Optional[bool] = None
    """
    - 是否可修改
    - 默认值：false
    """

    displayDataTypes: Optional[bool] = None
    """
    - 是否显示数据类型
    - 默认值：false
    """

    ellipsisThreshold: Optional[Union[int, bool]] = None
    """
    - 设置字符串的最大展示长度，点击字符串可以切换全量/部分展示方式，默认展示全量字符串
    - 默认值：false
    """

class Link(AmisNode):
    """
    Link 链接

    参数：https://aisuda.bce.baidu.com/amis/zh-CN/components/link#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = 'link'
    """如果在 Table、Card 和 List 中，为"link"；在 Form 中用作静态展示，为"static-link" """

    body: Optional[str] = None
    """标签内文本"""

    href: Optional[str] = None
    """链接地址"""

    blank: Optional[bool] = None
    """是否在新标签页打开"""

    htmlTarget: Optional[str] = None
    """a 标签的 target，优先于 blank 属性"""

    title: Optional[str] = None
    """a 标签的 title"""

    disabled: Optional[bool] = None
    """禁用超链接"""

    icon: Optional[str] = None
    """超链接图标，以加强显示"""

    rightIcon: Optional[str] = None
    """右侧图标"""

class Lists(AmisNode):

    class ListItem(BaseAmisModel):
        title: Optional[str] = None
        """标题模板"""

        titleClassName: Optional[str] = None
        """
        - 标题 CSS 类名
        - 默认值：h5
        """

        subTitle: Optional[str] = None
        """副标题模板"""

        avatar: Optional[str] = None
        """图片地址模板"""

        avatarClassName: Optional[str] = None
        """
        - 图片 CSS 类名
        - 默认值：thumb-sm avatar m-r
        """

        desc: Optional[str] = None
        """描述模板"""

        body: Optional[List[Dict[str, Any]]] = None
        """内容容器"""

        actions: Optional[List[Action]] = None
        """按钮区域"""

        actionsPosition: Optional[str] = None
        """
        - 按钮位置
        - 可选：'left' or 'right'
        - 默认值：右侧
        """

    type: str= 'list'
    """指定为列表展示，默认值：'list'"""

    title: Optional[str] = None
    """标题"""

    source: Optional[str] = None
    """
    - 数据源
    - 默认值：${items}
    """

    placeholder: Optional[str] = None
    """
    - 当没数据的时候的文字提示
    - 默认值：‘暂无数据’
    """

    selectable: Optional[bool] = None
    """
    - 列表是否可选
    - 默认值：false
    """

    multiple: Optional[bool] = None
    """
    - 列表是否为多选
    - 默认值：true
    """

    className: Optional[str] = None
    """外层 CSS 类名"""

    headerClassName: Optional[str] = None
    """
    - 顶部外层 CSS 类名
    - 默认值：amis-list-header
    """

    footerClassName: Optional[str] = None
    """
    - 底部外层 CSS 类名
    - 默认值：amis-list-footer
    """

    listItem: Optional[List[ListItem]] = None
    """配置单条信息"""

class Log(AmisNode):
    """
    source 支持高级配置

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/log#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "log"

    height: Optional[int] = None
    """
    - 展示区域高度
    - 默认值：500
    """

    className: Optional[str] = None
    """外层 CSS 类名"""

    autoScroll: Optional[bool] = None
    """
    - 是否自动滚动
    - 默认值：true
    """

    disableColor: Optional[bool] = None
    """
    - 是否禁用 ansi 颜色支持
    - 默认值：false
    """

    placeholder: Optional[str] = None
    """加载中的文字"""

    encoding: Optional[str] = None
    """
    - 返回内容的字符编码
    - 默认值：utf-8
    """

    source: Optional[API] = None
    """接口"""

    credentials: Optional[str] = None
    """
    - fetch 的 credentials 设置
    - 默认值：'include'
    """

    rowHeight: Optional[int] = None
    """设置每行高度，将会开启虚拟渲染"""

    maxLength: Optional[int] = None
    """最大显示行数"""

    operation: Optional[List[str]] = None
    """
    - 可选日志操作
    - 默认值：['stop','restart','clear','showLineNumber','filter']
    """

class Mapping(AmisNode):
    """
    Mapping 映射

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/mapping#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "mapping"

    className: Optional[str] = None
    """外层 CSS 类名"""

    placeholder: Optional[str] = None
    """占位文本"""

    map: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
    """映射配置"""

    source: Optional[Union[str, Any]] = None
    """API 或 数据映射"""

    valueField: Optional[str] = None
    """
    - 用来匹配映射的字段名
    - 默认值：value
    - 版本：2.5.2
    """

    labelField: Optional[str] = None
    """
    - 用来展示的字段名
    - 默认值：label
    - 版本：2.5.2
    """

    itemSchema: Optional[API] = None
    """
    - 自定义渲染模板，支持html或schemaNode
    - 版本：2.5.2
    - 使用说明：

      - 当映射值是非object时，可使用${item}获取映射值

      - 当映射值是object时，可使用映射语法: ${xxx}获取object的值

      - 可使用数据映射语法：${xxx}获取数据域中变量值
    """

class Markdown(AmisNode):
    """
    Markdown 渲染

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/markdown#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "markdown"

    name: Optional[str] = None
    """名称"""

    value: Optional[str] = None
    """静态值"""

    className: Optional[str] = None
    """类名"""

    src: Optional[API] = None
    """外部地址"""

    options: Optional[dict] = None
    """
    - 有以下配置
     - html，是否支持 html 标签，默认 false
     - linkify，是否自动识别链接，默认值是 true
     - breaks，是否回车就是换行，默认 false
    """

class Number(AmisNode):
    """
    Number 数字展示

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/number#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = 'number'
    """如果在 Table、Card 和 List 中，为"number"；在 Form 中用作静态展示，为"static-number" 或者 input-number 配置 static 属性"""

    className: Optional[str] = None
    """外层 CSS 类名"""

    value: Optional[str] = None
    """数值"""

    name: Optional[str] = None
    """在其他组件中，用作变量映射"""

    placeholder: Optional[str] = None
    """占位内容"""

    kilobitSeparator: Optional[bool] = None
    """
    - 是否千分位展示
    - 默认值：true
    """

    precision: Optional[int] = None
    """用来控制小数点位数"""

    percent: Optional[Union[bool, int]] = None
    """是否用百分比展示，如果是数字，还可以控制百分比小数点位数"""

    prefix: Optional[str] = None
    """前缀"""

    affix: Optional[str] = None
    """后缀"""

class OfficeViewer(AmisNode):
    """
    Office Viewer

    - 参考：
     - https://aisuda.bce.baidu.com/amis/zh-CN/components/office-viewer#%E5%B1%9E%E6%80%A7%E8%A1%A8
     - https://aisuda.bce.baidu.com/amis/zh-CN/components/office-viewer-excel#%E9%85%8D%E7%BD%AE%E9%A1%B9
    """

    type: str = "office-viewer"

    classPrefix: Optional[str] = None
    """
    - 渲染的 class 类前缀
    - 默认值：'docx-viewer'
    """

    ignoreWidth: Optional[bool] = None
    """
    - 忽略文档里的宽度设置，用于更好嵌入到页面里，但会减低还原度
    - 默认值：false
    """

    padding: Optional[str] = None
    """设置页面间距，忽略文档中的设置"""

    bulletUseFont: Optional[bool] = None
    """
    - 列表使用字体渲染
    - 默认值：true
    """

    fontMapping: Optional[Dict[str, str]] = None
    """字体映射，是个键值对，用于替换文档中的字体"""

    forceLineHeight: Optional[str] = None
    """设置段落行高，忽略文档中的设置"""

    enableVar: Optional[bool] = None
    """
    - 是否开启变量替换功能
    - 默认值：true
    """

    printOptions: Optional[Dict[str, Any]] = None
    """针对打印的特殊设置，可以覆盖其它所有设置项"""

    src: Optional[API] = None  # Document address
    """文件地址"""

    showFormulaBar: Optional[bool] = None
    """
    - 是否显示公式栏
    - 默认值：true
    """

    showSheetTabBar: Optional[bool] = None
    """
    - 是否显示底部 sheet 切换
    - 默认值：true
    """

    fontURL: Optional[Dict[str, str]] = None
    """字体地址，参考下面的说明"""

class PDFViewer(AmisNode):
    """
    PDF Viewer

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/pdf-viewer#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "pdf-viewer"

    src: Optional[str] = None
    """文档地址"""

    width: Optional[int] = None
    """宽度"""

    height: Optional[int] = None
    """高度"""

    background: Optional[str] = None
    """
    - PDF 背景色
    - 默认值：#fff
    """

class Progress(AmisNode):
    """
    Progress 进度条

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/progress#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Literal["progress", 'static-progress'] = 'progress'

    mode: Optional[Literal['line', 'circle', 'dashboard']] = None
    """
    - 进度「条」的类型
    - 可选：line, circle, dashboard
    - 默认值：line
    """

    className: Optional[str] = None
    """外层 CSS 类名"""

    value: Optional[str] = None
    """进度值"""

    placeholder: Optional[str] = None
    """占位文本"""

    showLabel: Optional[bool] = None
    """
    - 是否展示进度文本
    - 默认值：true
    """

    stripe: Optional[bool] = None
    """
    - 背景是否显示条纹
    - 默认值：false
    """

    animate: Optional[bool] = None
    """
    - type 为 line，可支持动画
    - 默认值：false
    """

    map: Optional[Union[str, List[Union[str, Dict[str, Union[int, str]]]]]] = None
    """
    - 进度颜色映射
    - 默认值：['bg-danger', 'bg-warning', 'bg-info', 'bg-success', 'bg-success']
    """

    threshold: Optional[Union[Dict[str, str], List[Dict[str, str]]]] = None
    """阈值（刻度）"""

    showThresholdText: Optional[bool] = None
    """
    - 是否显示阈值（刻度）数值
    - 默认值：false
    """

    valueTpl: Optional[str] = None
    """
    - 自定义格式化内容
    - 默认值：${value}%
    """

    strokeWidth: Optional[int] = None
    """
    - 进度条线宽度
    - 默认值：line 类型为10，circle、dashboard 类型为6
    """

    gapDegree: Optional[int] = None
    """
    - 仪表盘缺角角度
    - 可取值 0 ~ 295
    - 默认值：75
    """

    gapPosition: Optional[str] = None
    """
    - 仪表盘进度条缺口位置
    - 可选：top, bottom, left, right
    - 默认值：bottom
    """

class Property(AmisNode):
    """
    Property 属性表

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/property#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Item(AmisNode):
        label: Optional[Template] = None
        """属性名"""

        content: Optional[Template] = None
        """属性值"""

        span: Optional[int] = None
        """属性值跨几列"""

        visibleOn: Optional[Expression] = None
        """显示表达式"""

        hiddenOn: Optional[Expression] = None
        """隐藏表达式"""

    type: str = "property"

    className: Optional[str] = None
    """外层 dom 的类名"""

    style: Optional[Dict[str, Any]] = None
    """外层 dom 的样式"""

    labelStyle: Optional[Dict[str, Any]] = None
    """属性名的样式"""

    contentStyle: Optional[Dict[str, Any]] = None
    """属性值的样式"""

    column: Optional[int] = None
    """
    - 每行几列
    - 默认值：3
    """

    mode: Optional[str] = None
    """
    - 显示模式
    - 可选：'table', 'simple'
    - 默认值：'table'
    """

    separator: Optional[str] = None
    """
    - 'simple' 模式下属性名和值之间的分隔符
    - 默认值：','
    """

    title: Optional[str] = None
    """标题"""

    source: Optional[str] = None
    """数据源"""

    items: Optional[List[Item]] = None
    """配置单条信息"""

class QRCode(AmisNode):
    """
    QRCode 二维码

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/qrcode#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class ImageSettings(AmisNode):
        src: Optional[str] = None
        """图片链接地址"""

        width: Optional[int] = None
        """图片宽度，默认为 codeSize 的 10%"""

        height: Optional[int] = None
        """图片高度，默认为 codeSize 的 10%"""

        x: Optional[int] = None
        """图片水平方向偏移量，默认水平居中"""

        y: Optional[int] = None
        """图片垂直方向偏移量，默认垂直居中"""

        excavate: Optional[bool] = None
        """
        - 图片是否挖孔嵌入
        - 默认值：false
        """

    type: str = 'qr-code'

    className: Optional[str] = None
    """外层 Dom 的类名"""

    qrcodeClassName: Optional[str] = None
    """二维码的类名"""

    codeSize: Optional[int] = None
    """
    二维码的宽高大小
    - 默认值：128
    """

    backgroundColor: Optional[str] = None
    """
    二维码背景色
    - 默认值：'#fff'
    """

    foregroundColor: Optional[str] = None
    """
    二维码前景色
    - 默认值：'#000'
    """

    level: Optional[str] = None
    """
    - 二维码复杂级别
    - 默认值：'L'
    """

    value: Optional[Template] = None
    """
    - 扫描二维码后显示的文本，如果要显示某个页面请输入完整 url（"http://..."或"https://..."开头），支持使用模板
    - 默认值：'https://www.baidu.com'
    """

    imageSettings: Optional[ImageSettings] = None
    """QRCode 图片配置"""

class Remark(AmisNode):
    """
    Remark 标记

    用于展示提示文本，和表单项中的 remark 属性类型。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/remark#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "remark"

    className: Optional[str] = None
    """外层 CSS 类名"""

    content: Optional[str] = None
    """提示文本"""

    placement: Optional[str] = None
    """弹出位置"""

    trigger: Optional[str] = None
    """触发条件, 默认: ['hover', 'focus']"""

    icon: Optional[str] = None
    """图标: fa fa-question-circle"""

    shape: Optional[str] = None
    """	图标形状"""

class SearchBox(AmisNode):
    """
    Search Box 搜索框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/search-box#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "search-box"

    className: Optional[str] = None
    """外层 CSS 类名"""

    mini: Optional[bool] = None
    """是否为 mini 模式"""

    searchImediately: Optional[bool] = None
    """是否立即搜索"""

    clearAndSubmit: Optional[bool] = None
    """
    - 清空搜索框内容后立即执行搜索
    - 版本：2.8.0
    """

    disabled: Optional[bool] = None
    """
    - 是否为禁用状态
    - 默认值：false
    - 版本：6.0.0
    """

    loading: Optional[bool] = None
    """
    - 是否处于加载状态
    - 默认值：false
    - 版本：6.0.0
    """

class Sparkline(AmisNode):
    """
    Sparkline 走势图

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/sparkline#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "sparkline"

    name: Optional[str] = None
    """关联的变量"""

    width: Optional[int] = None
    """宽度"""

    height: Optional[int] = None
    """高度"""

    placeholder: Optional[str] = None
    """数据为空时显示的内容"""

    value: Optional[List[Union[int, float]]] = None
    """值"""

    clickAction: Optional[Action] = None
    """单击时的操作"""

class Status(AmisNode):
    """
    Status 状态

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/status#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Source(BaseModel):
        label: Optional[str] = None
        """
        - 映射文本
        - 版本：2.8.0
        """

        icon: Optional[str] = None
        """
        - 映射图标
        - 版本：2.8.0
        """

        color: Optional[str] = None
        """
        - 映射状态颜色
        - 版本：2.8.0
        """

        className: Optional[str] = None
        """
        - 映射状态的独立 CSS 类名
        - 版本：2.8.0
        """

    type: str = "status"  # Specify as Status renderer

    className: Optional[str] = None
    """外层 Dom 的 CSS 类名"""

    placeholder: Optional[str] = None
    """占位文本"""

    map: Optional[Dict[str, str]] = None
    """
    - 映射图标
    - 版本：2.3.0
    """

    labelMap: Optional[Dict[str, str]] = None
    """
    - 映射文本
    - 版本：2.3.0
    """

    source: Optional[Union[DataMapping, Source]] = None
    """
    - 自定义映射状态，支持数据映射
    - 版本：2.8.0
    """

class Steps(AmisNode):
    """
    Steps 步骤条

    步骤条组件

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/steps#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """


    class Step(AmisNode):
        title: Optional[SchemaNode] = None
        """标题"""

        subTitle: Optional[SchemaNode] = None
        """子标题"""

        description: Optional[SchemaNode] = None
        """详细描述"""

        icon: Optional[str] = None
        """icon 名，支持 fontawesome v4 或使用 url"""

        value: Optional[str] = None
        """步骤值"""

        className: Optional[str] = None
        """自定义 CSS 类名称"""

    type: str = "steps"

    steps: Optional[List[Step]] = None
    """
    - 数组，配置步骤信息
    - 默认值：[]
    """

    source: Optional[API] = None
    """选项组源，可通过数据映射获取当前数据域变量、或者配置 API 对象"""

    name: Optional[str] = None
    """关联上下文变量"""

    value: Optional[Union[str, int]] = None
    """设置默认值，注意不支持表达式"""

    status: Optional[Union[str, Dict[str, str]]] = None
    """状态"""

    className: Optional[str] = None
    """自定义类名"""

    mode: Optional[Literal['horizontal', 'vertical', 'simple']] = None
    """
    - 指定步骤条模式
    - 默认值：'horizontal'
    """

    labelPlacement: Optional[Literal['horizontal', 'vertical']] = None
    """
    - 指定标签放置位置
    - 默认值：'horizontal'
    """

    progressDot: Optional[bool] = None
    """
    - 点状步骤条
    - 默认值：false
    """

class Table(AmisNode):
    """
    Table 表格

    表格展示，不支持配置初始化接口初始化数据域，
    所以需要搭配类似像Service这样的，
    具有配置接口初始化数据域功能的组件，
    或者手动进行数据域初始化，然后通过source属性，
    获取数据链中的数据，完成数据展示。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "table"
    """"type" 指定为 table 渲染器"""

    title: Optional[str] = None
    """标题"""

    source: Optional[str] = None
    """
    - 数据源, 绑定当前环境变量
    - 默认值：${items}
    """

    deferApi: Optional[API] = None
    """当行数据中有 defer 属性时，用此接口进一步加载内容"""

    affixHeader: Optional[bool] = None
    """
    - 是否固定表头
    - 默认值：true
    """

    affixFooter: Optional[bool] = None
    """
    - 是否固定表格底部工具栏
    - 默认值：false
    """

    columnsTogglable: Union[bool, str, None] = None
    """
    - 展示列显示开关, 自动即：列数量大于或等于 5 个时自动开启
    - 默认值：auto
    """

    placeholder: Optional[str] = None
    """
    - 当没数据的时候的文字提示
    - 默认值：'暂无数据'
    """

    className: Optional[str] = None
    """
    - 外层 CSS 类名
    - 默认值：'panel-default'
    """

    tableClassName: Optional[str] = None
    """
    - 表格 CSS 类名
    - 默认值：'table-db table-striped'
    """

    headerClassName: Optional[str] = None
    """
    - 顶部外层 CSS 类名
    - 默认值：'Action.md-table-header'
    """

    footerClassName: Optional[str] = None
    """
    - 底部外层 CSS 类名
    - 默认值：'Action.md-table-footer'
    """

    toolbarClassName: Optional[str] = None
    """ 
    - 工具栏 CSS 类名	
    - 默认值：'Action.md-table-toolbar'
    """

    columns: Optional[List[Union["TableColumn", SchemaNode]]] = None
    """用来设置列信息"""

    combineNum: Optional[int] = None
    """自动合并单元格"""

    itemActions: Optional[List[Action]] = None
    """悬浮行操作按钮组"""

    itemCheckableOn: Optional[Expression] = None
    """配置当前行是否可勾选的条件，要用 表达式"""

    itemDraggableOn: Optional[Expression] = None
    """配置当前行是否可拖拽的条件，要用 表达式"""

    checkOnItemClick: Optional[bool] = None
    """
    - 点击数据行是否可以勾选当前行
    - 默认值：false
    """

    rowClassName: Optional[str] = None
    """给行添加 CSS 类名"""

    rowClassNameExpr: Optional[Template] = None
    """通过模板给行添加 CSS 类名"""

    prefixRow: Optional[list] = None
    """顶部总结行"""

    affixRow: Optional[list] = None
    """底部总结行"""

    itemBadge: Optional["Badge"] = None
    """行角标配置"""

    autoFillHeight: Optional[bool] = None
    """内容区域自适应高度，可选择自适应、固定高度和最大高度"""

    resizable: Optional[bool] = None
    """
    - 列宽度是否支持调整
    - 默认值：true
    """

    selectable: Optional[bool] = None
    """
    - 支持勾选
    - 默认值：false
    """

    multiple: Optional[bool] = None
    """
    - 勾选 icon 是否为多选样式checkbox， 默认为radio	
    - 默认值：false
    """

    lazyRenderAfter: Optional[int] = None
    """
    - 用来控制从第几行开始懒渲染行，用来渲染大表格时有用
    - 默认值：100
    """

    tableLayout: Optional[Literal['auto', 'fixed']] = None
    """
    - 当配置为 fixed 时，内容将不会撑开表格，自动换行
    - 默认值：'auto'
    """

    footable: Union[bool, dict, None] = None
    """是否开启底部展示功能，适合移动端展示"""

class TableColumn(AmisNode):
    """
    列配置属性表
    """
    type: Optional[str] = None
    """Literal['text','audio','image','link','tpl','mapping','carousel','date', 'progress','status','switch','list','json','operation','tag']"""

    label: Optional[Template] = None
    """标题文本内容"""

    name: Optional[str] = None
    """按名称关联数据"""

    width: Optional[Union[int, str]] = None
    """默认值：列宽"""

    remark: Optional[RemarkT] = None
    """提示消息"""

    fixed: Optional[Literal['left','right']] = None
    """是否修复当前列"""

    popOver: Optional[Union[str, 'PopOver']] = None
    """弹出框"""

    copyable: Optional[Union[bool, dict]] = None
    """
    - 是否可复制
    - 默认值：{icon: string, content:string}
    """

    style: Optional[str] = None
    """单元格自定义样式"""

    innerStyle: Optional[str] = None
    """单元格内部组件自定义样式"""

class Table2(AmisNode):
    """
    Table2 表格

    表格展示，不支持配置初始化接口初始化数据域，
    所以需要搭配类似像Service这样的，
    具有配置接口初始化数据域功能的组件，
    或者手动进行数据域初始化，然后通过source属性，
    获取数据链中的数据，完成数据展示。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E8%A1%8C%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "table"
    """"type" 指定为 table 渲染器"""

    title: Optional[str] = None
    """标题"""

    source: Optional[str] = None
    """
    - 数据源, 绑定当前环境变量
    - 默认值：${items}
    """

    sticky: Optional[bool] = None
    """
    - 是否粘性头部
    - 默认值：false
    """

    footer: Optional[Union[str, SchemaNode]] = None
    """表格尾部"""

    loading: Optional[bool] = None
    """表格是否加载中"""

    columnsTogglable: Optional[Union[Literal['auto'], bool]] = None
    """
    - 展示列显示开关, 自动即：列数量大于或等于 5 个时自动开启
    - 默认值：'auto'
    """

    placeholder: Optional[Union[str, SchemaNode]] = None
    """
    - 当没数据的时候的文字提示
    - 默认值：暂无数据
    """

    rowSelection: Optional["TableSelections2"] = None
    """行相关配置"""

    rowClassNameExpr: Optional[Union[str, Template]] = None
    """行 CSS 类名，支持模版语法"""

    expandable: Optional["TableExpandable2"] = None
    """展开行配置"""

    lineHeight: Optional[Union[Literal['large', 'middle']]] = None
    """行高设置"""

    footerClassName: Optional[str] = None
    """
    - 底部外层 CSS 类名
    - 默认值：'Action.md-table-footer'
    """

    toolbarClassName: Optional[str] = None
    """
    - 工具栏 CSS 类名
    - 默认值：'Action.md-table-toolbar'
    """

    columns:  Optional[List[Union["TableColumn2", SchemaNode]]] = None
    """用来设置列信息"""

    combineNum: Optional[int] = None
    """自动合并单元格"""

    itemActions: Optional[List[Action]] = None
    """悬浮行操作按钮组"""

    itemCheckableOn: Optional[Expression] = None
    """配置当前行是否可勾选的条件，要用 表达式"""

    itemDraggableOn: Optional[Expression] = None
    """配置当前行是否可拖拽的条件，要用 表达式"""

    checkOnItemClick: Optional[bool] = None
    """
    - 点击数据行是否可以勾选当前行
    - 默认值：false
    """

    rowClassName: Optional[str] = None
    """给行添加 CSS 类名"""

    prefixRow: Optional[list] = None
    """顶部总结行"""

    affixRow: Optional[list] = None
    """底部总结行"""

    itemBadge: Optional["Badge"] = None
    """行角标配置"""

    autoFillHeight: Optional[Union[bool, dict]] = None
    """内容区域自适应高度，可选择自适应、固定高度和最大高度"""

    lazyRenderAfter: Optional[int] = None
    """
    - 默认数据超过 100 条启动懒加载提升渲染性能，也可通过自定义该属性调整数值
    - 默认值：100
    """

class TableRow2(AmisNode):
    """
    行配置属性表

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E8%A1%8C%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Optional[Literal['checkbox', 'radio']] = None
    """
    - 指定单选还是多选
    - 默认值：'checkbox'
    """

    fixed: Optional[Literal['left','right']] = None
    """选择列是否固定，只能左侧固定"""

    keyField: Optional[str] = None
    """
    - 对应数据源的 key 值，默认是key，可指定为id、shortId等
    - 默认值：'key'
    """

    disableOn: Optional[str] = None
    """当前行是否可选择条件，要用 表达式"""

    selections: Optional["TableSelections2"] = None
    """自定义筛选菜单，内置all（全选）、invert（反选）、none（取消选择）、odd（选择奇数项）、even（选择偶数项）"""

    selectedRowKeys: Optional[Union[list[int], list[str]]] = None
    """已选择项"""

    selectedRowKeysExpr: Optional[str] = None
    """已选择项正则表达式"""

    columnWidth: Optional[int] = None
    """自定义选择列列宽"""

    rowClick:  Optional[bool] = None
    """单条任意区域选中"""

class TableSelections2(AmisNode):
    """
    展开行配置属性表

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E5%B1%95%E5%BC%80%E8%A1%8C%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    key: Optional[Literal['all','invert', 'none','odd', 'even']] = None
    """
    - 菜单类型，内置全选、反选、取消选择、选择奇数项、选择偶数项
    - 默认值：'all'
    """

    text: Optional[str] = None
    """自定义菜单项文本"""

class TableExpandable2(AmisNode):
    """
    展开行配置属性表

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E5%B1%95%E5%BC%80%E8%A1%8C%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    expandableOn: Optional[str] = None
    """指定可展开的行，要用 表达式"""

    keyField: Optional[str] = None
    """
    - 对应数据源的 key 值，默认是key，可指定为id、shortId等
    - 默认值：'key'
    """

    disableOn: Optional[str] = None
    """当前行是否可选择条件，要用 表达式"""

    selections: Optional[TableSelections2] = None
    """自定义筛选菜单，内置all（全选）、invert（反选）、none（取消选择）、odd（选择奇数项）、even（选择偶数项）"""

    selectedRowKeys: Optional[Union[list[int], list[str]]] = None
    """已选择项"""

    selectedRowKeysExpr: Optional[str] = None
    """已选择项正则表达式"""

    columnWidth: Optional[int] = None
    """自定义选择列列宽"""

class TableColumn2(AmisNode):
    """
    列配置属性表

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E5%88%97%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: Optional[str] = None
    """Literal['text','audio','image','link','tpl','mapping','carousel','date', 'progress','status','switch','list','json','operation','tag']"""

    label: Optional[Template] = None
    """标题文本内容"""

    name: Optional[str] = None
    """按名称关联数据"""

    fixed: Optional[Literal['left','right']] = None
    """是否修复当前列"""

    popOver: Optional[Union[bool, dict]] = None
    """弹出框"""

    quickEdit: Optional[Union[bool, dict]] = None
    """快速编辑"""

    copyable: Optional[Union[bool, dict]] = None
    """
    - 是否可复制
    - 默认值：{icon: string, content:string}
    """
    sortable: Optional[bool] = None
    """
    - 是否可排序
    - 默认值：False 
    """

    searchable: Optional[Union[bool, SchemaNode]] = None
    """
    - 是否快速搜索 boolean|图式
    - 默认值：False 
    """

    width: Optional[Union[int, str]] = None
    """默认值：列宽"""

    remark: Optional[RemarkT] = None
    """提示消息"""

class TableView(AmisNode):
    """
    Table View 表格展现

    - 1.2.0 及以上版本才有此功能
    - 数据源要求不同
        - table 的数据源需要是多行的数据，最典型的就是来自某个数据库的表
        - table view 的数据源可以来自各种固定的数据，比如单元格的某一列是来自某个变量
    - 功能不同
        - table 只能用来做数据表的展现
        - table view 除了展现复杂的报表，还能用来进行布局
    - 合并单元格方式不同
        - table 的合并单元格需要依赖数据
        - table view 的合并单元格是手动指定的，因此可以支持不规则的数据格式

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table-view#%E8%A1%A8%E6%A0%BC%E8%AE%BE%E7%BD%AE%E9%A1%B9
    """

    type: str = "table-view"
    """指定组件类型"""

    width: Optional[Union[int, str]] = None
    """
      - 宽度
      - 默认值：'100%'
    """

    padding: Optional[Union[int, str]] = None
    """
      - 单元格默认内间距
      - 默认值：'var(--TableCell-paddingY) var(--TableCell-paddingX)'
    """

    border: Optional[bool] = None
    """
      - 是否显示边框
      - 默认值：true
    """

    borderColor: Optional[str] = None
    """
      - 边框颜色
      - 默认值：'var(--borderColor)'
    """

    trs: Optional['TableViewRow'] = None
    """参考的行设置 """

    cols: Optional['TableViewCols'] = None

    caption: Optional[str] = None
    """
    - 标题设置
    - 可以通过 caption 来添加段标题文本，并通过 captionSide 来控制显示在底部还是顶部。
    """

    captionSide: Optional[Literal['top', 'bottom']] = None
    """显示在底部还是顶部"""

class TableViewRow(AmisNode):
    """
    行设置

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table-view#%E8%A1%8C%E8%AE%BE%E7%BD%AE
    """
    height: Optional[Union[int, str]] = None
    """行高度"""

    background: Optional[str] = None
    """行背景色"""

    tds: Optional['TableViewTds'] = None
    """参考单元格设置"""

class TableViewTds(AmisNode):
    """
    单元格设置

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table-view#%E5%8D%95%E5%85%83%E6%A0%BC%E8%AE%BE%E7%BD%AE
    """

    background: Optional[str] = None
    """单元格背景色"""

    color: Optional[str] = None
    """单元格文字颜色"""

    bold: Optional[bool] = None
    """
    - 单元格文字是否加粗
    - 默认值：false
    """

    width: Optional[Union[int, str]] = None
    """单元格宽度，只需要设置第一行"""

    padding: Optional[Union[int, str]] = None
    """
    - 单元格内间距
    - 默认值：'集成表格的设置'
    """

    align: Optional[Literal['left', 'center', 'right']] = None
    """
    - 单元格内的水平对齐
    - 默认值：'left'
    """

    valign: Optional[Literal['top', 'middle', 'bottom', 'baseline']] = None
    """
    - 单元格内的垂直对齐
    - 默认值：'middle'
    """

    colspan: Optional[int] = None
    """单元格水平跨几行"""

    rowspan: Optional[int] = None
    """单元格垂直跨几列"""

    body: Optional[Union[AmisNode, list[AmisNode]]] = None
    """其它 amis 设置"""

class TableViewCols(AmisNode):
    """
    列设置项

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table-view#%E5%88%97%E8%AE%BE%E7%BD%AE%E9%A1%B9
    """
    span: Optional[int] = None
    """这是个跨几列的设置项"""

    style: Optional[dict] = None
    """列样式"""

class Tag(AmisNode):
    type: str = "tag"

    displayMode: Optional[Literal['normal', 'rounded', 'status']] = None
    """
    - 展现模式
    - 默认值：'normal'
    """

    color: Optional[Union[Literal['active', 'inactive', 'error', 'success', 'processing', 'warning'], str]] = None
    """颜色主题，提供默认主题，并支持自定义颜色值"""

    label: Optional[str] = None
    """标签内容"""

    icon: Optional[Icon] = None
    """status 模式下的前置图标"""

    className: Optional[str] = None
    """自定义 CSS 样式类名"""

    style: Optional[Dict[str, Any]] = None
    """自定义样式（行内样式），优先级最高"""

    closable: Optional[bool] = None
    """
    - 是否展示关闭按钮
    - 默认值：false
    """

class Timeline(AmisNode):
    """
    Timeline 时间轴

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/timeline#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class TimelineItem(AmisNode):
        time: Optional[str] = None
        """节点时间"""

        title: Optional[Union[str, 'SchemaNode']] = None
        """节点标题"""

        detail: Optional[str] = None
        """节点详细描述（折叠）"""

        detailCollapsedText: Optional[str] = "展开"
        """详细内容折叠时按钮文案"""

        detailExpandedText: Optional[str] = "折叠"
        """详细内容展开时按钮文案"""

        color: Optional[Union[str, Literal['info', 'success', 'warning', 'danger']]] = None
        """
        - 时间轴节点颜色
        - 默认值：'#DADBDD'
        """

        icon: Optional[str] = None
        """icon 名，支持 fontawesome v4 或使用 url（优先级高于 color）"""

        iconClassName: Optional[str] = None
        """
        节点图标的 CSS 类名
        - 优先级高于统一配置的 iconClassName
        - 3.4.0 版本支持
        """

        timeClassName: Optional[str] = None
        """
        节点时间的 CSS 类名
        - 优先级高于统一配置的 timeClassName
        - 3.4.0 版本支持
        """

        titleClassName: Optional[str] = None
        """
        节点标题的 CSS 类名
        - 优先级高于统一配置的 titleClassName
        - 3.4.0 版本支持
        """

        detailClassName: Optional[str] = None
        """
        节点详情的 CSS 类名
        - 优先级高于统一配置的 detailClassName
        - 3.4.0 版本支持
        """

    type: Optional[str] = "timeline"


    items: Optional[List[TimelineItem]] = []
    """配置节点数据"""

    source: Optional[Union[str, Dict]] = None
    """数据源，可通过数据映射获取当前数据域变量、或者配置 API 对象"""

    mode: Optional[str] = "right"
    """
    指定文字相对于时间轴的位置
    - 仅 direction=vertical 时支持
    """

    direction: Optional[str] = None
    """
    - 时间轴方向
    - 默认值：'vertical'
    """

    reverse: Optional[bool] = None
    """
    根据时间倒序显示
    - 默认值：false
    """

    iconClassName: Optional[str] = None
    """
    统一配置的节点图标 CSS 类名
    - 3.4.0 版本支持
    """

    timeClassName: Optional[str] = None
    """
    统一配置的节点时间 CSS 类名
    - 3.4.0 版本支持
    """

    titleClassName: Optional[str] = None
    """
    统一配置的节点标题 CSS 类名
    - 3.4.0 版本支持
    """

    detailClassName: Optional[str] = None
    """
    统一配置的节点详情 CSS 类名
    - 3.4.0 版本支持
    """

class Video(AmisNode):
    """
    Video 视频

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/video#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "video"

    className: Optional[str] = None
    """外层 Dom 的类名"""

    src: Optional[str] = None
    """视频地址"""

    isLive: Optional[bool] = None
    """
    - 是否为直播
    - 默认值：false
    """

    videoType: Optional[str] = None
    """指定直播视频格式"""

    poster: Optional[str] = None
    """视频封面地址"""

    muted: Optional[bool] = None
    """是否静音"""

    loop: Optional[bool] = None
    """是否循环播放"""

    autoPlay: Optional[bool] = None
    """是否自动播放"""

    rates: Optional[List[float]] = None
    """倍数，格式为[1.0, 1.5, 2.0]"""

    frames: Optional[Dict[str, Any]] = None
    """时刻信息，value 可以设置为图片地址"""

    jumpBufferDuration: Optional[bool] = None
    """点击帧时提前跳转的秒数"""

    stopOnNextFrame: Optional[bool] = None
    """到了下一帧自动停止"""

# ==================== 反馈 ====================

class Alert(AmisNode):
    """
    Alert 提示

    用来做文字特殊提示，分为四类：提示类、成功类、警告类和危险类。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/alert#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "alert"

    title: Optional[str] = None
    """alert 标题"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    level: Optional[Literal['info', 'success', 'warning', 'danger']] = None
    """
    - 级别
    - 默认值：'info'
    """

    body: Optional[Union[List[SchemaNode], SchemaNode]] = None
    """显示内容"""

    showCloseButton: Optional[bool] = None
    """
    - 是否显示关闭按钮
    - 默认值：false
    """

    closeButtonClassName: Optional[str] = None
    """关闭按钮的 CSS 类名"""

    showIcon: Optional[bool] = None
    """
    - 是否显示 icon
    - 默认值：false
    """

    icon: Optional[str] = None
    """自定义 icon"""

    iconClassName: Optional[str] = None
    """icon 的 CSS 类名"""

    actions: Optional[Union[List[SchemaNode], SchemaNode]] = None
    """
    - 操作区域
    - 版本：3.6.0
    """

class Dialog(AmisNode):
    """
    Dialog 对话框

    Dialog 弹框 主要由 Action 触发，主要展示一个对话框以供用户操作。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/dialog#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "dialog"

    title: Optional[SchemaNode] = None
    """弹出层标题"""

    body: Optional[SchemaNode] = None
    """往 Dialog 内容区加内容"""

    size: Optional[Literal['xs', 'sm', 'md', 'lg', 'xl', 'full']] = None
    """指定 dialog 大小，支持: xs、sm、md、lg、xl、full"""

    bodyClassName: Optional[str] = None
    """
    - Dialog body 区域的样式类名
    - 默认值：'modal-body'
    """

    closeOnEsc: Optional[bool] = None
    """
    - 是否支持按 Esc 关闭 Dialog
    - 默认值：false
    """

    showCloseButton: Optional[bool] = None
    """
    - 是否显示右上角的关闭按钮
    - 默认值：true
    """

    showErrorMsg: Optional[bool] = None
    """
    - 是否在弹框左下角显示报错信息
    - 默认值：true
    """

    showLoading: Optional[bool] = None
    """
    - 是否在弹框左下角显示 loading 动画
    - 默认值：true
    """

    disabled: Optional[bool] = None
    """
    - 如果设置此属性，则该 Dialog 只读没有提交操作。
    - 默认值：false
    """

    actions: Optional[List[Action]] = None
    """如果想不显示底部按钮，可以配置：[]"""

    data: Optional[Dict] = None
    """支持数据映射，如果不设定将默认将触发按钮的上下文中继承数据。"""

class Drawer(AmisNode):
    """
    Drawer 抽屉

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/drawer#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "drawer"

    title: Optional[SchemaNode] = None
    """弹出层标题"""

    body: Optional[SchemaNode] = None
    """往 Drawer 内容区加内容"""

    size: Optional[Literal['xs', 'sm','md','lg','xl']] = None
    """指定 Drawer 大小"""

    position: Optional[Literal['left', 'right', 'top', 'bottom']] = None
    """
    - 指定 Drawer 方向
    - 默认值：'right'
    """

    className: Optional[str] = None
    """Drawer 最外层容器的样式类名"""

    headerClassName: Optional[str] = None
    """Drawer 头部 区域的样式类名"""

    bodyClassName: Optional[str] = None
    """
    - Drawer body 区域的样式类名
    - 默认值：'modal-body'
    """

    footerClassName: Optional[str] = None
    """Drawer 页脚 区域的样式类名"""

    showCloseButton: Optional[bool] = None
    """
    - 是否展示关闭按钮，当值为 false 时，默认开启 closeOnOutside
    - 默认值：true
    """

    closeOnEsc: Optional[bool] = None
    """
    - 是否支持按 Esc 关闭 Drawer
    - 默认值：false
    """

    closeOnOutside: Optional[bool] = None
    """
    - 点击内容区外是否关闭 Drawer
    - 默认值：false
    """

    overlay: Optional[bool] = True
    """
    - 是否显示蒙层
    - 默认值：true
    """

    resizable: Optional[bool] = None
    """
    - 是否可通过拖拽改变 Drawer 大小
    - 默认值：false
    """

    width: Optional[Union[str, int]] = None
    """
    - 容器的宽度，在 position 为 left 或 right 时生效
    - 默认值：'500px'
    """

    height: Optional[Union[str, int]] = None
    """
    - 容器的高度，在 position 为 top 或 bottom 时生效
    - 默认值：'500px'
    """

    actions: Optional[List[Action]] = None
    """可以不设置，默认只有两个按钮。"""

    data: Optional[Dict] = None
    """支持数据映射，如果不设定将默认将触发按钮的上下文中继承数据。"""

class Spinner(AmisNode):
    """
    Spinner 加载中

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/spinner#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "spinner"

    show: Optional[bool] = None
    """
    - 是否显示 spinner 组件
    - 默认值：true
    """

    showOn: Optional[Expression] = None
    """是否显示 spinner 组件的条件"""

    className: Optional[str] = None
    """spinner 图标父级标签的自定义 class"""

    spinnerClassName: Optional[str] = None
    """组件中 icon 所在标签的自定义 class"""

    spinnerWrapClassName: Optional[str] = None
    """作为容器使用时组件最外层标签的自定义 class"""

    size: Optional[Literal['sm', 'lg']] = None
    """组件大小"""

    icon: Optional[str] = None
    """组件图标，可以是内置图标，也可以是字体图标或者网络图片链接"""

    tip: Optional[str] = None
    """配置组件文案，例如加载中..."""

    tipPlacement: Optional[str] = None
    """
    - 配置组件 tip 相对于 icon 的位置
    - 默认值：bottom
    """

    delay: Optional[int] = None
    """
    - 配置组件显示延迟的时间（毫秒）
    - 默认值：0
    """

    overlay: Optional[bool] = None
    """
    - 配置组件显示 spinner 时是否显示遮罩层
    - 默认值：true
    """

    body: Optional[SchemaNode] = None
    """作为容器使用时，被包裹的内容"""

    loadingConfig: Optional[Dict[str, Any]] = None
    """
    - 为 Spinner 指定挂载的容器
    - 开启后，会强制开启属性 overlay=true，并且 icon 会失效
    """

class Toast(Action):
    """
    Toast 轻提示

    参数：https://aisuda.bce.baidu.com/amis/zh-CN/components/toast#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class ToastItem(AmisNode):
        title: Optional[SchemaNode] = None
        """标题"""

        body: Optional[SchemaNode] = None
        """内容"""

        level: Optional[Literal['info','success','error','warning']] = None
        """
        - 展示图标
        - 默认值：'info'
        """

        position: Optional[Literal['top-right','top-center','top-left','bottom-center','bottom-left','bottom-right','center']] = None
        """
        - 提示显示位置
        - 默认值：'top-center'（移动端为 'center'）
        """

        closeButton: Optional[bool] = None
        """
        - 是否展示关闭按钮
        - 默认值：false
        """

        showIcon: Optional[bool] = None
        """
        - 是否展示图标
        - 默认值：true
        """

        timeout: Optional[int] = None
        """
        - 持续时间
        - 默认值：5000（error 类型为 6000，移动端为 3000）
        """

        allowHtml: Optional[bool] = None
        """
        - 是否会被当作 HTML 片段处理
        - 默认值：true
        """

    actionType: Optional[str] = None

    items: Optional[List[ToastItem]] = None
    """
    - 轻提示内容
    - 默认值：[]
    """

    position: Optional[Literal['top-right','top-center','top-left','bottom-center','bottom-left','bottom-right','center']] = None
    """
    - 提示显示位置
    - 默认值：'top-center'（移动端为 'center'）
    """

    closeButton: Optional[bool] = None
    """
    - 是否展示关闭按钮
    - 默认值：false
    - 移动端不展示
    """

    showIcon: Optional[bool] = None
    """
    - 是否展示图标
    - 默认值：true
    """

    timeout: Optional[int] = None
    """
    - 持续时间
    - 默认值：5000（error 类型为 6000，移动端为 3000）
    """

# ==================== 其他 ====================

class Audio(AmisNode):
    """
    Audio 音频

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/audio#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "audio"

    className: Optional[str] = None
    """外层 Dom 的类名"""

    inline: Optional[bool] = None
    """
    - 是否是内联模式
    - 默认值：true
    """

    src: Optional[str] = None
    """音频地址"""

    loop: Optional[bool] = None
    """
    - 是否循环播放
    - 默认值：false
    """

    autoPlay: Optional[bool] = None
    """
    - 是否自动播放
    - 默认值：false
    """

    rates: Optional[List[float]] = None
    """
    - 可配置音频播放倍速
    - 默认值：[]
    """

    controls: Optional[List[str]] = None
    """
    - 内部模块定制化
    - 默认值：['rates', 'play', 'time', 'process', 'volume']
    """

class Avatar(AmisNode):
    """
    Avatar 头像

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/avatar#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "avatar"

    className: Optional[str] = None
    """外层 dom 的类名"""

    style: Optional[Dict] = None
    """外层 dom 的样式"""

    fit: Optional[str] = None
    """
    - 具体细节可以参考 MDN 文档
    - 默认值：'cover'
    """

    src: Optional[str] = None
    """图片地址"""

    defaultAvatar: Optional[str] = None
    """占位图"""

    text: Optional[str] = None
    """文字"""

    icon: Optional[str] = None
    """
    - 图标
    - 默认值：'fa fa-user'
    """

    shape: Optional[str] = None
    """
    - 形状，有三种 'circle'（圆形）、'square'（正方形）、'rounded'（圆角）
    - 默认值：'circle'
    """

    size: Optional[Union[int, str]] = None
    """
    - 'default' | 'normal' | 'small' 三种字符串类型代表不同大小（分别是 48、40、32）
    - 也可以直接数字表示
    - 默认值：'default'
    """

    gap: Optional[int] = None
    """
    - 控制字符类型距离左右两侧边界单位像素
    - 默认值：4
    """

    alt: Optional[str] = None
    """图像无法显示时的替代文本"""

    draggable: Optional[bool] = None
    """图片是否允许拖动"""

    crossOrigin: Optional[str] = None
    """图片的 CORS 属性设置"""

    onError: Optional[str] = None
    """
    图片加载失败的字符串，这个字符串是一个 New Function 内部执行的字符串，参数是 event
    （使用 event.nativeEvent 获取原生 dom 事件），这个字符串需要返回 boolean 值。
    设置 "return true;" 会在图片加载失败后，使用 text 或者 icon 代表的信息来进行替换。
    注意：图片加载失败，不包括获取数据为空情况
    """

class Badge(AmisNode):
    """
    Badge 角标

    部分组件可以设置 badge 属性来显示角标。

    - 1.2.2 及之前版本只支持头像组件

    - 1.2.3 开始支持按钮、链接、模板组件。

    参考： https://baidu.github.io/amis/zh-CN/components/badge#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    mode: str = "dot"
    """角标类型，可以是 dot/text/ribbon"""

    text: Optional[Union[int, str]]= None
    """角标文案，支持字符串和数字，在 mode='dot'下设置无效"""

    size: Optional[int] = None
    """角标大小"""

    level: Optional[str] = None
    """角标级别, 可以是 info/success/warning/danger, 设置之后角标背景颜色不同"""

    overflowCount: Optional[int] = None
    """
    - 设置封顶的数字值
    - 默认值：99
    """

    position: Optional[Literal['top-right','top-left', 'bottom-right', 'bottom-left']] = None
    """
    - 角标位置
    - 默认值：'top-right'
    """

    offset: Optional[list[int]] = None
    """
    - 角标位置，offset 相对于 position 位置进行水平、垂直偏移
    - 默认值：[0, 0]
    """

    className: Optional[str] = None
    """外层 dom 的类名"""

    animation: Optional[bool] = None
    """角标是否显示动画"""

    style: Optional[dict] = None
    """角标的自定义样式"""

    visibleOn: Optional[Expression] = None
    """控制角标的显示隐藏"""

class Tasks(AmisNode):
    """
    Tasks 任务操作集合

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/tasks#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class TaskItem(BaseModel):
        label: Optional[str] = None
        """任务名称"""

        key: Optional[str] = None
        """任务键值，请唯一区分"""

        remark: Optional[str] = None
        """当前任务状态，支持 html"""

        status: Optional[str] = None
        """
        任务状态：
        0: 初始状态，不可操作。
        1: 就绪，可操作状态。
        2: 进行中，还没有结束。
        3: 有错误，不可重试。
        4: 已正常结束。
        5: 有错误，且可以重试。
        """

    type: str = "tasks"  # Specify as Tasks renderer

    className: Optional[str] = None
    """外层 Dom 的类名"""

    tableClassName: Optional[str] = None
    """table Dom 的类名"""

    items: Optional[List[TaskItem]] = None
    """任务列表"""

    checkApi: Optional[Dict] = None
    """返回任务列表，返回的数据请参考 items。"""

    submitApi: Optional[Dict] = None
    """提交任务使用的 API"""

    reSubmitApi: Optional[Dict] = None
    """如果任务失败，且可以重试，提交的时候会使用此 API"""

    interval: Optional[int] = None
    """
    - 当有任务进行中，会每隔一段时间再次检测，而时间间隔就是通过此项配置
    - 默认值：3000
    """

    taskNameLabel: Optional[str] = None
    """任务名称列说明"""

    operationLabel: Optional[str] = None
    """操作列说明"""

    statusLabel: Optional[str] = None
    """状态列说明"""

    remarkLabel: Optional[RemarkT] = None
    """备注列说明"""

    btnText: Optional[str] = None
    """操作按钮文字"""

    retryBtnText: Optional[str] = None
    """重试操作按钮文字"""

    btnClassName: Optional[str] = None
    """
    - 配置容器按钮 className
    - 默认值：'btn-sm btn-default'
    """

    retryBtnClassName: Optional[str] = None
    """
    - 配置容器重试按钮 className
    - 默认值：'btn-sm btn-danger'
    """

    statusLabelMap: Optional[List[str]] = None
    """
    - 状态显示对应的类名配置
    - 默认值：['label-warning', 'label-info', 'label-success', 'label-danger', 'label-default', 'label-danger']
    """

    statusTextMap: Optional[List[str]] = None
    """
    - 状态显示对应的文字显示配置
    - 默认值：['未开始', '就绪', '进行中', '出错', '已完成', '出错']
    """

class WebComponent(AmisNode):
    """
    Web Component

    专门用来渲染 web component 的组件，可以通过这种方式来扩展 amis 组件，比如使用 Angular。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/web-component#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = 'web-component'


    tag: Optional[str] = None
    """具体使用的 web-component 标签"""

    props: Optional[Dict] = None
    """标签上的属性"""

    body: Optional[SchemaNode] = None
    """子节点"""

    style: Optional[Union[str, dict]] = None
    """样式"""

class Wizard(AmisNode):
    """
    Wizard 向导

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/wizard#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Step(BaseModel):
        title: Optional[str] = None
        """步骤标题"""

        mode: Optional[str] = None
        """展示默认，跟 Form 中的模式一样，选择：normal、horizontal 或者 inline。"""

        horizontal: Optional[Dict[str, Any]] = None
        """当为水平模式时，用来控制左右占比"""

        api: Optional[Dict] = None
        """当前步骤保存接口，可以不配置。"""

        initApi: Optional[Dict] = None
        """当前步骤数据初始化接口。"""

        initFetch: Optional[bool] = None
        """当前步骤数据初始化接口是否初始拉取。"""

        initFetchOn: Optional[str] = None
        """当前步骤数据初始化接口是否初始拉取，用表达式来决定。"""

        body:Optional[List[FormItem]] = None
        """当前步骤的表单项集合，请参考 FormItem。"""

        closeDialogOnSubmit: Optional[bool] = None
        """提交的时候是否关闭弹窗。"""

        jumpableOn: Optional[str] = None
        """配置是否可跳转的表达式"""

        actions: Optional[List[SchemaNode]] = None
        """自定义每一步的操作按钮"""

    type: str = "wizard"

    mode: Optional[str] = None
    """
    - 展示模式，选择：horizontal 或者 vertical
    - 默认值：'horizontal'
    """

    api: Optional[API] = None
    """最后一步保存的接口。"""

    initApi: Optional[API] = None
    """初始化数据接口"""

    initFetch: Optional[bool] = None
    """初始是否拉取数据。"""

    initFetchOn: Optional[Expression] = None
    """初始是否拉取数据，通过表达式来配置"""

    actionPrevLabel: Optional[str] = None
    """
    - 上一步按钮文本
    - 默认值：'上一步'
    """

    actionNextLabel: Optional[str] = None
    """
    - 下一步按钮文本
    - 默认值：'下一步'
    """

    actionNextSaveLabel: Optional[str] = None
    """
    - 保存并下一步按钮文本
    - 默认值：'保存并下一步'
    """

    actionFinishLabel: Optional[str] = None
    """
    - 完成按钮文本
    - 默认值：'完成'
    """

    className: Optional[str] = None
    """外层 CSS 类名"""

    actionClassName: Optional[str] = None
    """
    - 按钮 CSS 类名
    - 默认值：'btn-sm btn-default'
    """

    reload: Optional[str] = None
    """操作完后刷新目标对象。"""

    redirect: Optional[Template] = None
    """
    - 操作完后跳转。
    - 默认值：3000
    """

    target: Optional[str] = None
    """可以把数据提交给别的组件而不是自己保存。"""

    steps: Optional[List[Step]] = None
    """数组，配置步骤信息"""

    startStep: Optional[Union[str, int]] = None
    """
    - 起始默认值，从第几步开始。
    - 默认值：'1'
    """