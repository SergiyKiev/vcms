
from _base.base import Base


class BaseElements(Base):

    LOADING_SCREEN = "//div[@id='VWG_LoadingScreen']"
    #BUTTONS
    BUTTON_EDIT = "/*//*[text()='Edit']/ancestor::div[contains(@class,'Button')]"
    BUTTON_NEW = "//span[text()='New']/ancestor::div[contains(@class,'Button')]"
    BUTTON_OK_UPPERCASE = "/*//span[text()='OK']/ancestor::div[contains(@class,'Button')]"
    BUTTON_OK_LOWERCASE = "/*//span[text()='Ok']/ancestor::div[contains(@class,'Button')]"
    BUTTON_CANCEL_UPPERCASE = "/*//span[text()='CANCEL']/ancestor::div[contains(@class,'Button')]"
    BUTTON_CANCEL_LOWERCASE = "/*//span[text()='Cancel']/ancestor::div[contains(@class,'Button')]"
    BUTTON_NEXT = "/*//img[@alt='NEXT']/ancestor::div[contains(@class,'Button')]"
    BUTTON_PREVIOUS = "//span[text()='PREVIOUS']/ancestor::div[contains(@class,'Button')]"
    BUTTON_FINISH = "//span[text()='FINISH']/ancestor::div[contains(@class,'Button')]"
    BUTTON_OPEN = "//span[text()='...']/ancestor::div[contains(@class,'Button')]"
    BUTTON_NO = "/*//span[text()='No']/ancestor::div[contains(@class,'Button')]"
    BUTTON_YES = "/*//span[text()='Yes']/ancestor::div[contains(@class,'Button')]"
    BUTTON_CLOSE = "/*//span[text()='Close']/ancestor::div[contains(@class,'Button')]"
    BUTTON_ARROW_UP = "/*//td[contains(@style,'arrow_up')]/ancestor::div[contains(@class,'Button')]"
    BUTTON_ARROW_DOWN = "/*//td[contains(@style,'arrow_down')]/ancestor::div[contains(@class,'Button')]"
    BUTTON_ADD = "/*//span[text()='Add']/ancestor::div[contains(@class,'Button')]"
    BUTTON_DELETE = "/*//span[text()='Delete']/ancestor::div[contains(@class,'Button')]"
    BUTTON_SELECT_ALL = "/*//*[text()='Select All']/ancestor::div[contains(@class,'Button')]"
    BUTTON_SELECT_NONE = "/*//*[text()='Select None']/ancestor::div[contains(@class,'Button')]"
    TABLE_HEADER = "//*[@class='Common-Unselectable ListView-Control']/*[contains(@id,'HEADER')]"
    TABLE_BODY = "//*[@class='Common-Unselectable ListView-Control']/div/*[contains(@id,'VWGLVBODY')]"

   #SYSTEM_BUTTONS
    SYSTEM_BUTTON_CLOSE = "/*//div[@title='Close'][@onclick]"
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
    DROP_DOWN_LIST          = "/*//div[contains(@class,'ComboBox-Container')]"
    DROP_DOWN_APPLIED_VALUE = "/*//div[contains(@class,'ComboBox-Container')]/*//span[@data-vwg_appliedvalue]"
    GREY_COLOR = "[contains(@style,'#E8E8E8')]"
    WHITE_COLOR = "[contains(@style,'White')]"
    BLACK_COLOR = "[contains(@style,'Black')]"

    #GENERAL ELEMENTS
    POPUP = "//div[contains(@id,'WRP')][last()]"
    POPUP_ERROR = "//span[text()='Error']/ancestor::div[contains(@id,'WRP')][last()]/*//span[contains(@class,'Label-FontData')]"
    FIELD = "/*//input"
    # RIBBON_BAR = "//div[@class='RibbonBarTabControl-Control']"
    RIBBON_BAR = "//div[@class='RibbonBar-Control']"
    LEFT_MENU_HOME = "//td[contains(@style,'Home')]/ancestor::div[@class='Panel-Control']/following-sibling::div[@class='FlowLayoutPanel-Control']"
    PANEL_CONTROL = "//div[@class='Panel-Control']"
    DROP_DOWN_WINDOW = "//div[@class='ComboBox-PopupWindow']"
    TAB_PANEL = "//div[contains(@id,'VWGTCHD_')]"
    TREE_VIEW = "/*//div[@class='Common-Unselectable TreeView-Container']"
    LABEL = "/ancestor::div[contains(@class,'ListItem')]"
    TAB = "/ancestor::div[contains(@class,'TabControl')]"

    #HELP WINDOW
    HELP_WINDOW_BODY = "//title[text()='ConsoleOperationGuide']"
    HELP_FRAME_HEADER = "//*[@id='topic_header_text']"
    HELP_FRAME_HEADER_ERROR = "//body/*[@id='header']/h1"
    HELP_FRAME_MAIN = "//frame[@name='FrameMain']"
    HELP_FRAME_TOC = "//frame[@name='FrameTOC']"
    HELP_FRAME_HEADER_SERVER_ERROR = "//h1[text()='Server Error']"
    HELP_FRAME_HEADER_GETTING_STARTED = "//h1[text()='Getting Started in CMS']"





