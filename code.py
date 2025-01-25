from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() 
#driver.get('https://www.daraz.com.bd/routers/')
#driver.maximize_window()

link_dict = {}

for page_no in range(1, 3):
    driver.get(f'https://www.daraz.com.bd/routers/?page={page_no}')
    driver.maximize_window()
    product = []
    for prod in range(1, 13):
        type_i = str(prod)
        link = driver.find_element(By.CSS_SELECTOR,f'#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child({type_i}) > div > div > div.buTCk > div.RfADt > a').get_attribute('href')
        product.append(link)
    link_dict[page_no] = product


for page, links in link_dict.items():
    print(f"Page {page}: {product} items {links}")

time.sleep(400)
driver.quit()
