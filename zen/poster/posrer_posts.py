from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from time import sleep
import pickle

service = Service("C:\\bin\\chromedriver.exe")
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0")
options.add_argument("--disable-blink-features=AutomationControlled")
driver = Chrome(service=service, options=options)

driver.maximize_window()

# url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
url = "https://zen.yandex.ru/"

login = "elislapina"

password = "k9I8hY6tg"

try:

    # driver.get(url=url)
    # WebDriverWait(driver, timeout=10)
    # sleep(3)
    #
    # driver.find_element(By.LINK_TEXT, "Войти").click()
    # sleep(5)
    #
    # input_login = driver.find_element(By.ID, "passp-field-login")
    # input_login.clear()
    # input_login.send_keys(login)
    # sleep(1)
    # driver.find_element(By.ID, "passp:sign-in").click()
    # sleep(3)
    #
    # input_pass = driver.find_element(By.ID, "passp-field-passwd")
    # input_pass.clear()
    # input_pass.send_keys(password)
    # sleep(1)
    # driver.find_element(By.ID, "passp:sign-in").click()
    # sleep(5)
    #
    # pickle.dump(driver.get_cookies(), open(f"{login}_cookies", "wb"))

    driver.get(url=url)
    WebDriverWait(driver, timeout=10)
    sleep(1)

    for cookie in pickle.load(open(f"{login}_cookies", "rb")):
        driver.add_cookie(cookie)

    sleep(2)
    driver.refresh()
    WebDriverWait(driver, timeout=10)
    sleep(2)
    pickle.dump(driver.get_cookies(), open(f"{login}_cookies", "wb"))

    driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Меню профиля')]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[contains(@href, '/media/zen/new')]").click()
    sleep(2)
    test_old = driver.find_elements(By.CLASS_NAME, "ui-lib-header-item _type_right zen-header__create-post")

    if len(test_old) > 0:
        driver.find_element(By.CLASS_NAME, "ui-lib-header-item _type_right zen-header__create-post").click()
    else:
        driver.find_element(By.XPATH, "//div[contains(@class, 'publications-groups-view__btn-wrapper')]/button").click()

    sleep(2)

    driver.find_element(By.XPATH, "//div[contains(@class, 'ui-lib-context-menu _palette_default new-publication-dropdown')]/button[1]").click()
    sleep(2)

    close_button = driver.find_elements(By.XPATH, "//div[contains(@role, 'button')]")
    if len(close_button) > 0:
        driver.find_element(By.XPATH, "//div[contains(@role, 'button')]").click()

    driver.find_element(By.XPATH, "//div[contains(@class, 'zen-editor')]/div[contains(@class, 'DraftEditor-root')]/div[contains(@class, 'public-DraftEditorPlaceholder-root')]").click()
    sleep(1)
    driver.find_element(By.XPATH, "//div[contains(@class, 'zen-editor')]/div[contains(@class, 'DraftEditor-root')]/div[contains(@class, 'public-DraftStyleDefault-block public-DraftStyleDefault-ltr')]").send_keys("2222222")

except Exception as _ex:
    print(_ex)

finally:
    sleep(5)
    driver.close()
    driver.quit()
