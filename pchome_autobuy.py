from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# 欲搶購的連結、登入帳號、登入密碼及其他個資
from settings import URL, DRIVER_PATH, CHROME_PATH, ACC, PWD, BuyerSSN, BirthYear, BirthMonth, BirthDay, multi_CVV2Num

# 設定此 option 可讓 chrome 記住已登入帳戶，成功後可以省去後續"登入帳戶"的程式碼
options = webdriver.ChromeOptions()  
options.add_argument(CHROME_PATH)  

driver = webdriver.Chrome(
    executable_path=DRIVER_PATH, chrome_options=options)
driver.set_page_load_timeout(120)

def login():
    WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.ID, 'loginAcc'))
    )
    elem = driver.find_element_by_id('loginAcc')
    elem.clear()
    elem.send_keys(ACC)
    elem = driver.find_element_by_id('loginPwd')
    elem.clear()
    elem.send_keys(PWD)
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.ID, "btnLogin"))
    )
    driver.find_element_by_id('btnLogin').click()
    print('>>> 成功登入')

try:
    driver.get(URL)

    ### 放入購物車 ###
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//li[@id='ButtonContainer']/button"))
    )
    driver.find_element_by_xpath("//li[@id='ButtonContainer']/button").click()


    ### 前往購物車 ###
    driver.get("https://ecssl.pchome.com.tw/sys/cflow/fsindex/BigCar/BIGCAR/ItemList")

    ### 登入帳戶 ###
    # 若有使用 CHROME_PATH 記住登入資訊
    # 第二次執行時請記得註解掉這行！！
    login()


    ### 前往結帳 (一次付清) ### (要使用 JS 的方式 execute_script 點擊)
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//li[@class='CC']/a[@class='ui-btn']"))
    )
    button = driver.find_element_by_xpath(
        "//li[@class='CC']/a[@class='ui-btn']")
    driver.execute_script("arguments[0].click();", button)

    ### 點擊提示訊息確定 ###
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[@id='warning-timelimit_btn_confirm']"))
    )
    button = driver.find_element_by_xpath("//a[@id='warning-timelimit_btn_confirm']")
    driver.execute_script("arguments[0].click();", button)

    ### 填入各項資料 ### (BuyerSSN, BirthYear, BirthMonth, BirthDay, multi_CVV2Num)
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@id='BuyerSSN']"))
    )
    elem = driver.find_element_by_xpath("//input[@id='BuyerSSN']")
    elem.send_keys(BuyerSSN)

    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='BirthYear']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BirthYear']")
    elem.send_keys(BirthYear)

    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='BirthMonth']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BirthMonth']")
    elem.send_keys(BirthMonth)

    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='BirthDay']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='BirthDay']")
    elem.send_keys(BirthDay)

    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='multi_CVV2Num']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='multi_CVV2Num']")
    elem.send_keys(multi_CVV2Num)


    ### 勾選同意 ###
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//input[@name='chk_agree']"))
    )
    driver.find_element_by_xpath("//input[@name='chk_agree']").click()


    ### 送出訂單 ### (要使用 JS 的方式 execute_script 點擊)
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[@id='btnSubmit']"))
    )
    button = driver.find_element_by_xpath("//a[@id='btnSubmit']")
    driver.execute_script("arguments[0].click();", button)


except Exception as e:
    print(e)
