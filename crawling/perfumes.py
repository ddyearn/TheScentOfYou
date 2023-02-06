from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

options = Options()
packed_extension_path = 'cfhdojbkjhnklbpkdaibdccddilifddb.crx'
options.add_extension(packed_extension_path)

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.fragrantica.com/search/")
time.sleep(5)

SCROLL_PAUSE_TIME = 1

while True:
    time.sleep(SCROLL_PAUSE_TIME)
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    elem = driver.find_element(By.CSS_SELECTOR, '#main-content > div.grid-x.grid-margin-x > div.small-12.medium-8.large-9.cell > div > div > div > div.off-canvas-content.content1.has-reveal-left > div.grid-x.grid-padding-x.grid-padding-y > div > div:nth-child(3) > div > div > div > div > div > button')
    if(elem.get_property('disabled')):
        break
    else:
        elem.click()

#open the file for write operation
f = open('perfumes.txt' , 'w')

time.sleep(1)
perfumes = driver.find_elements(By.CLASS_NAME, 'card-section')
for perfumes in perfumes:
    try:
        text = perfumes.text
        f.write(text)
        f.write("\n")
    except:
        pass

f.close()
driver.close()
