

class Constants(object):

    siteName = "New site IK"
    field = "//input"
    fieldUsername = "//input[@type='text']"
    fieldPassword = "//input[@type='password']"
    buttonSignIn = "//span[text()='Sign In']"
    buttonExit = "//img[@alt='Exit']"
    buttonDevices = "//div[@title='Devices']"
    textGlobalSiteView = "//span[contains(text(),'Global Site View')]"
    labelGlobalSiteView = "//span[text()='Global Site View']/ancestor::div[@class='TreeView-PaddingContainer']/div[1]/div[contains(@id,'VWGNODE')]"
    treeGlobalSiteView = "//span[text()='Global Site View']/ancestor::div[@class='TreeView-PaddingContainer']/div[1]/div[contains(@id,'VWGSUBS')]"
    buttonNewSite = "//img[@alt='New Site']"
    buttonOK = "//span[text()='OK']"
    buttonDelete = "//img[@alt='Delete']"
    popupSiteName = "//span[text()='Site Name']/ancestor::div[contains(@id,'WRP')]"
    popupAreYouSure = "//span[text()='Are you sure?']/ancestor::div[contains(@id,'WRP')]"
    popup = "//div[contains(@id,'WRP')]"
    labelSiteName = "//span[text()='" + siteName + "']"
    popupSubscriptionsHasExpired = "//span[text()='Manage Subscriptions']/ancestor::div[contains(@id,'WRP')]"
    buttonSystemClose = "//div[@title='Close']"
    loadingScreenInvisible = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: none']"
    loadingScreenVisible = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: block']"
    loadingAnimationBox = "VWG_LoadingAnimationBox"
    popupTermsAndConditions = "//span[text()='Terms and Conditions']/ancestor::div[contains(@id,'WRP')]"
    buttonIAgree = "//span[text()='I Agree']"
    containerMenuDevices = "//span[text()='Devices']/ancestor::div[contains(@id,'VWG_')]/*//div[contains(@style,'translate3d(0px, 0px, 0px)')]"
