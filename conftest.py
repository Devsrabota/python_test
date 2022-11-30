from pytest import fixture

from appium import webdriver

    
@fixture()
def driver_mob():
    mobile_driver = webdriver.Remote(command_executor = 'http://127.0.0.1:4723/wd/hub',
     desired_capabilities = {'platformName': 'Android',
     'udid': 'emulator-5554'})
    mobile_driver.implicitly_wait(15)
    yield mobile_driver
    mobile_driver.quit()

@fixture()
def element(driver_mob):
    return driver_mob.find_element