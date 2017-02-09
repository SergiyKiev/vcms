
class BaseElements:

    LOADING_SCREEN = "//div[@id='VWG_LoadingScreen']"

    #BUTTONS
    BUTTON_EDIT = "/*//img[@alt='Edit']/ancestor::div[contains(@class,'Button')]"
    BUTTON_EDIT_by_text = "/*//*[text()='Edit']"
    # BUTTON_NEW = "//img[@alt='New']/ancestor::div[contains(@class,'Button')]"
    # BUTTON_NEW_by_text = "//span[text()='New']/ancestor::div[contains(@class,'Button')]"
    BUTTON_OK = "/*//span[text()='OK']/ancestor::div[contains(@class,'Button')]"
    BUTTON_Ok = "/*//span[text()='Ok']/ancestor::div[contains(@class,'Button')]"
    BUTTON_CANCEL = "/*//span[text()='Cancel']/ancestor::div[contains(@class,'Button')]"
    BUTTON_NO = "/*//span[text()='No']/ancestor::div[contains(@class,'Button')]"
    BUTTON_YES = "/*//span[text()='Yes']/ancestor::div[contains(@class,'Button')]"
    BUTTON_CLOSE = "/*//span[text()='Close']/ancestor::div[contains(@class,'Button')]"
    BUTTON_RESTORE = "/*//td[contains(@style,'circlex')]/ancestor::div[contains(@class,'Button')]"
    BUTTON_ARROW_UP = "/*//td[contains(@style,'arrow_up')]/ancestor::div[contains(@class,'Button')]"
    BUTTON_ARROW_DOWN = "/*//td[contains(@style,'arrow_down')]/ancestor::div[contains(@class,'Button')]"

   #SYSTEM_BUTTONS
    SYSTEM_BUTTON_CLOSE = "/*//div[@title='Close']"
    SYSTEM_BUTTON_MAXIMIZE = "//div[@title='Maximize']"
    SYS_BUTTON_MINIMIZE = "//div[@title='Minimize']"
    SYS_BUTTON_RESTORE_DOWN = "//div[@title='Restore Down']"
    SYSTEM_BUTTON_DROP_DOWN = "/*//div[@class='ComboBox-Button']"

    #ICONS
    ICON_HELP = "/*//img[contains(@src,'About')]"
    ICON_EXPORT = "/*//img[contains(@src,'212-action2')]"
    ICON_REFRESH = "/*//img[contains(@src,'02-redo.2x')]"
    ICON_SEARCH = "/*//img[contains(@src,'06-magnify.2xw')]"

    #DROP_DOWN
    DROP_DOWN_LIST = "/*//div[contains(@class,'ComboBox-Container')]"
    DROP_DOWN_APPLIED_VALUE = "/*//div[contains(@class,'ComboBox-Container')]/*//span[@data-vwg_appliedvalue]"

    #GENERAL ELEMENTS
    _POPUP = "//div[contains(@id,'WRP')][last()]"
    _FIELD = "/*//input"
    _RIBBON_BAR = "//div[@class='RibbonBarTabControl-Control']"
    _PANEL = "//div[@class='Panel-Control']"
    _DROP_DOWN_LIST = "//div[@class='ComboBox-PopupWindow']"
    _TAB_PANEL = "//div[contains(@id,'VWGTCHD_')]"
    _LOGIN_PAGE_LOGO = "//img[contains(@src,'Images.CMS-Login')]"

    #HELP WINDOW
    HELP_WINDOW_BODY = "//title[text()='ConsoleOperationGuide']"
    HELP_WINDOW_HEADER = "//*[@id='topic_header_text']"
    HELP_FRAME_MAIN = "//frame[@name='FrameMain']"
    HELP_FRAME_TITLE_SERVER_ERROR = "//h1[text()='Server Error']"
    HELP_FRAME_TITLE_GETTING_STARTED = "//h1[text()='Getting Started in CMS']"



