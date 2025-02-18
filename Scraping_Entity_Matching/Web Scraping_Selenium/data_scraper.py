import time
from selenium.webdriver.common.by import By



def scrape_data(driver, start_page, end_page):
    name = []
    shop = []
    address = []
    alert_xpath = '//*[@id="cookie-policy"]/button'

    base_url = "Website URL"

    for page in range(start_page, end_page + 1):
        url = f"{base_url}{page}"
        print("Page:", page)
        driver.get(url)
        time.sleep(3)


        try:
            element = driver.find_element(By.XPATH, alert_xpath)
            element.click()
        except Exception as err:
            pass
        time.sleep(1)

        for i in range(1, 21):
            print("----", i)
            try:
                name_xpath = f'//*[@id="serpspage"]/div/div[1]/div[{i}]/div/div[1]/h3/a'
                elem = driver.find_element(By.XPATH, name_xpath)
                name.append(elem.text)
            except Exception as err:
                name.append(None)

            try:
                farm_xpath = f'//*[@id="serpspage"]/div/div[1]/div[{i}]/div/div[1]/p[1]'
                elem = driver.find_element(By.XPATH, farm_xpath)
                shop.append(elem.text)
            except Exception as err:
                shop.append(None)

            try:
                address_xpath = f'//*[@id="serpspage"]/div/div[1]/div[{i}]/div/div[1]/p[2]'
                elem = driver.find_element(By.XPATH, address_xpath)
                address.append(elem.text)
            except Exception as err:
                address.append(None)

    return name, shop, address
