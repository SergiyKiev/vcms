from selenium.webdriver.common.by import By
from variables import Variables
# for maintainability we can separate web objects by page name

class Locators:

  #LOADING ANIMATION
  def __init__(self):
    pass

  LOADING_SCREEN_INVISIBLE         = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: none']"
  LOADING_SCREEN_VISIBLE           = "//div[@id='VWG_LoadingAnimationBox'][contains(@style,'display: block']"
  LOADING_ANIMATION_BOX           = "VWG_LoadingAnimationBox"
  #MENU
  MENU_DEVICES                    = "//div[@title='Devices']/ancestor::div[contains(@id,'VWG_')]/*//div[contains(" \
                                                "@style,'translate3d(0px, 0px, 0px)')]"
  #CONTAINERS
  CONTAINER_GLOBAL_SITE_VIEW      = "//span[text()='Global Site View']/ancestor::div[@class='TreeView-PaddingContainer']/div[1]"
  CONTAINER_HEADER_DEVICES_VIEW   = "//span[text()='Devices']/ancestor::div[contains(@style,'85px')]"
  #LABELS
  LABEL_GLOBAL_SITE_VIEW          = CONTAINER_GLOBAL_SITE_VIEW + "/div[contains(@id,'VWGNODE')]"
  #TREES
  TREE_GLOBAL_SITE_VIEW           = CONTAINER_GLOBAL_SITE_VIEW + "/div[contains(@id,'VWGSUBS')]"
  #TEXT
  TEXT_GLOBAL_SITE_VIEW           = "//span[contains(text(),'Global Site View')]"
  TEXT_ERROR                      = "//span[text()='Error']"
  TEXT_SITE_NAME                  = "//span[text()='" + Variables.siteName + "']"
  # TEXT_SITE_NAME                  = "//span[text()='Test IK01']"
  #SITES
  SITE_GLOBAL_SITE_VIEW           = "//span[text()='Global Site View']"
  #FIELDS
  FIELD                           = "//input"
  FIELD_USERNAME                  = "//input[@type='text']"
  FIELD_PASSWORD                  = "//input[@type='password']"
  #BUTTONS
  BUTTON_SIGN_IN                  = "//span[text()='Sign In']"
  BUTTON_EXIT                     = "//img[@alt='Exit']"
  BUTTON_DEVICES                  = "//div[@title='Devices']"
  BUTTON_NEW_SITE                 = "//img[@alt='New Site']"
  BUTTON_DELETE                   = "//img[@alt='Delete']"
  BUTTON_OK                       = "//span[text()='OK']"
  BUTTON_Ok                       = "//span[text()='Ok']"
  BUTTON_CANCEL                   = "//span[text()='Cancel']"
  BUTTON_SYSTEM_CLOSE             = "//div[@title='Close']"
  BUTTON_I_AGREE                  = "//span[text()='I Agree']"
  #POPUPS
  POPUP                           = "//div[contains(@id,'WRP')]"
  POPUP_SITE_NAME                 = "//span[contains(text(),'Site') and contains(text(),'Name')]/ancestor::div[contains(@id,'WRP')]"
  POPUP_ARE_YOU_SURE              = "//span[text()='Are you sure?']/ancestor::div[contains(@id,'WRP')]"
  POPUP_SUBSCRIPTION_HAS_EXPIRED   = "//span[text()='Manage Subscriptions']/ancestor::div[contains(@id,'WRP')]"
  POPUP_TERMS_AND_CONDITIONS      = "//span[text()='Terms and Conditions']/ancestor::div[contains(@id,'WRP')]"
  POPUP_ERROR                     = "//span[text()='Error']/ancestor::div[contains(@id,'WRP')]"
  #ELEMENT STATUS
  SELECTED                        = "[contains(@class,'Selected')]"
  DISABLED                        = "[contains(@class,'Disabled')]"
