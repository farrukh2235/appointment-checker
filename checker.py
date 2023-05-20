from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check():
    
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    # print('Driver Started')
    driver.get("https://service2.diplo.de/rktermin/extern/choose_realmList.do?locationCode=isla&request_locale=en")
    # print('Page Fetched')
    try:
        btn1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div[1]/div[3]/a")))
        # print('Btn 1 Fetched')
        driver.execute_script("arguments[0].click();", btn1)
        btn2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[1]/div[1]/div[12]/a")))
        # print('Btn 2 Fetched')
        driver.execute_script("arguments[0].click();", btn2)
        btn3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/h3[2]/a[2]")))
        # print('Btn 3 Fetched')
        driver.execute_script("arguments[0].click();", btn3)
        elem_select = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/fieldset/form/div[8]/div[2]/select")))
        # print('Select Element Fetched')
        
        option_elems = elem_select.find_elements(By.TAG_NAME ,"option")
        # print('Options Fetched')
        active = False
        active_value = ''
        for opt in option_elems:
            opt_value = opt.get_attribute("value")
            if isinstance(opt_value, str) and "phd" in opt_value.lower():
                active = True
                # active_value = opt_value
                break
            
        if active:
            print('ACTIVE')
            driver.quit()
            return (None, True)
            # print(active_value)
        else:
            print('NOT-ACTIVE')
            driver.quit()
            return (None, False)
    except Exception as e:
        print('ERROR')
        driver.quit()
        # print(e)
        return (e, False)

if __name__ == '__main__':
    check()
