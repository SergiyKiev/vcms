
from _base_page.base import Base


class BaseElements(Base):

    LOADING_SCREEN = "//div[@id='VWG_LoadingScreen']"

    #BUTTONS
    BUTTON_EDIT = "/*//*[text()='Edit']/ancestor::div[contains(@class,'Button')]"
    BUTTON_NEW = "//span[text()='New']/ancestor::div[contains(@class,'Button')]"
    BUTTON_OK = "/*//span[text()='OK']/ancestor::div[contains(@class,'Button')]"
    BUTTON_Ok = "/*//span[text()='Ok']/ancestor::div[contains(@class,'Button')]"
    BUTTON_CANCEL = "/*//span[text()='Cancel']/ancestor::div[contains(@class,'Button')]"
    BUTTON_NO = "/*//span[text()='No']/ancestor::div[contains(@class,'Button')]"
    BUTTON_YES = "/*//span[text()='Yes']/ancestor::div[contains(@class,'Button')]"
    BUTTON_CLOSE = "/*//span[text()='Close']/ancestor::div[contains(@class,'Button')]"
    BUTTON_ARROW_UP = "/*//td[contains(@style,'arrow_up')]/ancestor::div[contains(@class,'Button')]"
    BUTTON_ARROW_DOWN = "/*//td[contains(@style,'arrow_down')]/ancestor::div[contains(@class,'Button')]"
    BUTTON_ADD = "/*//span[text()='Add']/ancestor::div[contains(@class,'Button')]"
    BUTTON_DELETE = "/*//span[text()='Delete']/ancestor::div[contains(@class,'Button')]"

   #SYSTEM_BUTTONS
    SYSTEM_BUTTON_CLOSE = "/*//div[@title='Close']"
    SYSTEM_BUTTON_MAXIMIZE = "//div[@title='Maximize']"
    SYS_BUTTON_MINIMIZE = "//div[@title='Minimize']"
    SYS_BUTTON_RESTORE_DOWN = "//div[@title='Restore Down']"
    SYSTEM_BUTTON_DROP_DOWN = "/*//div[@class='ComboBox-Button']"

    #ICONS
    ICON_HELP = "/*//img[contains(@src,'About')]"
    ICON_EXPORT = "/*//img[contains(@src,'212-action')]"
    ICON_REFRESH = "/*//img[contains(@src,'02-redo')]"
    ICON_SEARCH = "/*//img[contains(@src,'06-magnify')]"
    ICON_RESTORE = "/*//img[contains(@src,'298-circlex')]"

    #DROP_DOWN
    DROP_DOWN_LIST = "/*//div[contains(@class,'ComboBox-Container')]"
    DROP_DOWN_APPLIED_VALUE = "/*//div[contains(@class,'ComboBox-Container')]/*//span[@data-vwg_appliedvalue]"

    #GENERAL ELEMENTS
    _POPUP = "//div[contains(@id,'WRP')][last()]"
    _FIELD = "/*//input"
    # _RIBBON_BAR = "//div[@class='RibbonBarTabControl-Control']"
    _RIBBON_BAR = "//div[@class='RibbonBar-Control']"
    _LEFT_MENU = "//td[contains(@style,'Home')]/ancestor::div[@class='Panel-Control']/following-sibling::div[@class='FlowLayoutPanel-Control']"
    _PANEL = "//div[@class='Panel-Control']"
    _DROP_DOWN_LIST = "//div[@class='ComboBox-PopupWindow']"
    _TAB_PANEL = "//div[contains(@id,'VWGTCHD_')]"

    #HELP WINDOW
    HELP_WINDOW_BODY = "//title[text()='ConsoleOperationGuide']"
    HELP_FRAME_HEADER = "//*[@id='topic_header_text']"
    HELP_FRAME_MAIN = "//frame[@name='FrameMain']"
    HELP_FRAME_TOC = "//frame[@name='FrameTOC']"
    HELP_FRAME_HEADER_SERVER_ERROR = "//h1[text()='Server Error']"
    HELP_FRAME_HEADER_GETTING_STARTED = "//h1[text()='Getting Started in CMS']"





