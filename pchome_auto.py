from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import settings #需要的資料放在這

url = settings.url

# 設定此 option 可讓 chrome 記住已登入帳戶，成功後可以省去"#登入帳戶"的程式碼
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\\<chrome 設定檔路徑>")  # 可透過 chrome://version/ 找到

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
driver.set_page_load_timeout(120)

try:
    driver.get(url)

    # 放入購物車
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//li[@id='ButtonContainer']/button"))
    )
    driver.find_element_by_xpath("//li[@id='ButtonContainer']/button").click()

    # 前往購物車
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.ID, "ico_cart"))
    )
    driver.find_element_by_id('ico_cart').click()

    # 登入帳戶
    WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.ID, 'loginAcc'))
    )
    elem = driver.find_element_by_id('loginAcc')
    elem.send_keys(settings.acc)
    elem = driver.find_element_by_id('loginPwd')
    elem.send_keys(settings.pwd)
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.ID, "btnLogin"))
    )
    driver.find_element_by_id('btnLogin').click()

    # 前往結帳 (一次付清)，要使用 JS (execute_script) 點擊
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//li[@class='CC']/a[@class='ui-btn']"))
    )
    button = driver.find_element_by_xpath("//li[@class='CC']/a[@class='ui-btn']")
    driver.execute_script("arguments[0].click();", button)

    # 填入各項資料 (BuyerSSN, BirthYear, BirthMonth, BirthDay, multi_CVV2Num)
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='BuyerSSN']"))
    )
    elem = driver.find_element_by_xpath("//input[@id='BuyerSSN']")
    elem.send_keys(settings.id)

    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='BirthYear']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BirthYear']")
    elem.send_keys(settings.y)

    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='BirthMonth']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BirthMonth']")
    elem.send_keys(settings.m)

    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='BirthDay']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BirthDay']")
    elem.send_keys(settings.d)

    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='multi_CVV2Num']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='multi_CVV2Num']")
    elem.send_keys(settings.vup4m4f83)

    # 勾選同意
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='chk_agree']"))
    )
    driver.find_element_by_xpath("//input[@name='chk_agree']").click()

    # 送出訂單，要使用 JS (execute_script) 點擊
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//a[@id='btnSubmit']"))
    )    
    button = driver.find_element_by_xpath("//a[@id='btnSubmit']")
    driver.execute_script("arguments[0].click();", button)

except Exception as e:
    print(e.__class__.__name__)
