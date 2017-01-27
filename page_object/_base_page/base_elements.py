
class BaseElements:

    #BUTTONS
    BTN_EDIT = "//img[@alt='Edit']"
    BTN_EDIT_by_text = "//span[text()='Edit']"
    BUTTON_OK = "/*//span[text()='OK']/ancestor::div[contains(@class,'Button')][contains(@id,'VWG_')]"
    BUTTON_Ok = "/*//span[text()='Ok']/ancestor::div[contains(@class,'Button')][contains(@id,'VWG_')]"

   #SYSTEM_BUTTONS
    SYSTEM_BUTTON_CLOSE = "/*//div[@title='Close']"
    POPUP_SYSTEM_BUTTON_CLOSE = "//div[contains(@id,'WRP')][last()]/*//div[@title='Close']"

    _POPUP = "//div[contains(@id,'WRP')][last()]"
    _FIELD = "//input"



