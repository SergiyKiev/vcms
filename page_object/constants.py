from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class PageConstants(object):

  BUTTON_SIGN_IN                  = "//span[text()='Sign In']"
  FIELD_USERNAME                  = "//input[@type='text']"
  FIELD_PASSWORD                  = "//input[@type='password']"
  FIELD                           = "//input"
  TEXT_GLOBAL_SITE_VIEW           = "//span[contains(text(),'Global Site View')]"
  LABEL_GLOBAL_SITE_VIEW          = "//span[text()='Global Site View']/ancestor::div[@class='TreeView-PaddingContainer']/div[1]/div[contains(@id,'VWGNODE')]"
  TREE_GLOBAL_SITE_VIEW           = "//span[text()='Global Site View']/ancestor::div[@class='TreeView-PaddingContainer']/div[1]/div[contains(@id,'VWGSUBS')]"
  BUTTON_OK                       = "//span[text()='OK']"
  SITE_NAME                       = "1"
  POPUP                           = "//div[contains(@id,'WRP')]"
  TEXT_ERROR                      = "//span[text()='Error']"
  BUTTON_EXIT                     = "//img[@alt='Exit']"
  BUTTON_DEVICES                  = "//div[@title='Devices']"
  BUTTON_NEW_SITE                 = "//img[@alt='New Site']"
  BUTTON_DELETE                   = "//img[@alt='Delete']"
  POPUP_SITE_NAME                 = "//span[text()='Site Name']/ancestor::div[contains(@id,'WRP')]"
  POPUP_ARE_YOU_SURE              = "//span[text()='Are you sure?']/ancestor::div[contains(@id,'WRP')]"
  BUTTON_SYSTEM_CLOSE             = "//div[@title='Close']"
  LABEL_SITE_NAME                 = "//span[text()='" + SITE_NAME + "']"
  LOADING_SCREE_INVISIBLE         = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: none']"
  LOADING_SCREE_VISIBLE           = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: block']"
  LOADING_ANIMATION_BOX           = "VWG_LoadingAnimationBox"
  MENU_DEVICES                    = "//span[text()='Devices']/ancestor::div[contains(@id,'VWG_')]/*//div[contains(@style,'translate3d(0px, 0px, 0px)')]"
  POPUP_SUBSRIPTION_HAS_EXPIRED   = "//span[text()='Manage Subscriptions']/ancestor::div[contains(@id,'WRP')]"
  POPUP_TERMS_AND_CONDITIONS      = "//span[text()='Terms and Conditions']/ancestor::div[contains(@id,'WRP')]"
  BUTTON_I_AGREE                  = "//span[text()='I Agree']"
  POPUP_ERROR                     = POPUP + TEXT_ERROR
  #LOGO          = (By.ID, 'nav-logo')
  #ACCOUNT       = (By.ID, 'nav-link-yourAccount')
  #SIGNUP        = (By.CSS_SELECTOR, '#nav-flyout-ya-newCust > a')
  #LOGIN         = (By.CSS_SELECTOR, '#nav-flyout-ya-signin > a')
  #SEARCH        = (By.ID, 'twotabsearchtextbox')
  #SEARCH_LIST   = (By.ID, 's-results-list-atf')
  #EMAIL         = (By.ID, 'ap_email')
  #PASSWORD      = (By.ID, 'ap_password')
  #SUBMIT        = (By.ID, 'signInSubmit-input')
  #ERROR_MESSAGE = (By.ID, 'message_error')
