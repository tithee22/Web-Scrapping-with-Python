from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import io 
from PIL import Image

chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()

driver.get('https://www.daraz.com.bd/products/tp-link-archer-c54-ac1200-wireless-dual-band-router-i188538221-s1135972329.html?')
driver.maximize_window()

#scrolling through the page
height = driver.execute_script('return document.body.scrollHeight')

for i in range(0, height, 30):
    driver.execute_script(f'window.scrollTo(0, {i});')
    time.sleep(0.5)

product_details = {}


#getting Image file
image_url = "https://img.drz.lazcdn.com/static/bd/p/eccac4c30429ed28cff6718ed5b691aa.jpg_200x200q80.jpg_.webp"

#getting image content from the url
image_content = requests.get(image_url).content
# converting content into bytes using bytesIo and saving directly inside memory
image_file = io.BytesIO(image_content)
#now from byte to converting directly in image 
image = Image.open(image_file)
file_path = "" + 'router.jpg'

with open(file_path, "wb") as f:
    image.save(f, 'JPEG')

product_details["image"] = file_path

product_name = driver.find_element(By.XPATH, '//*[@id="module_product_title_1"]/div/div/h1').text
product_details["name"] = product_name

product_price = driver.find_element(By.XPATH,'//*[@id="module_product_price_1"]/div/div/span').text
product_details["price"] = product_price

product_description = driver.find_element(By.XPATH,'//*[@id="module_product_detail"]/div/div/div[1]/div[1]/ul/li[1]').text
product_details["description"] = product_description

product_comments = driver.find_elements(By.CLASS_NAME, 'content')

for comment in product_comments:
    product_details['comments'] = comment.text

print(f'Here Is The Details of Product : {product_details}')

time.sleep(20)
driver.quit()