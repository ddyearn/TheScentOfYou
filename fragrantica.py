from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.fragrantica.com/notes/")

#open the file for write operation
f = open('notes.txt' , 'w')

time.sleep(5)
notes = driver.find_elements(By.CLASS_NAME, 'notebox')
for note in notes:
    try:
        text = note.text
        f.write(text)
        f.write("\n")
    except:
        pass

f.close()
driver.close()