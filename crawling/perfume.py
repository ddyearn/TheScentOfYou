import time
import os
import connectionSetting
import pymysql
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve

setting = connectionSetting.info
# connection setting
conn = pymysql.connect(
    db=setting['db'],
    host=setting['host'],
    user=setting['user'],
    passwd=setting['passwd'],
    port=setting['port'],
    charset=setting['charset']
)

# cursor
cur = conn.cursor()

# Adblock 설치
options = Options()
packed_extension_path = 'C:\webDriver\extensions\gighmmpiobklfepjocnamgkkbiglidom.crx'

options.add_extension(packed_extension_path)
path = "C:\webDriver\chrome\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path, options=options)
url="https://basenotes.com/fragrances/page-18?launch=2021-2022&orderby=added"
driver.get(url)

time.sleep(3)




elements = driver.find_elements_by_css_selector('.bncards > div')

for i in range(8):
    for i in range(0, len(elements)):
        elements = driver.find_elements_by_css_selector('.bncards > div')  
            
        aTag = elements[i].find_element_by_tag_name("a")   

        # 상품 성별
        try:
            el_gender = aTag.find_element_by_css_selector('p > i')
            gender_class = el_gender.get_attribute("class")
            
            perfume_gender=""
            if gender_class in "fas fa-venus":
                perfume_gender="woman"
            elif gender_class in "fas fa-mars":
                perfume_gender="man"
            else:
                perfume_gender="neuter"
        
            aTag.send_keys(Keys.ENTER)
        except:
            continue

        try:
            check = driver.find_element_by_css_selector('ol.fragrancenotes')
        except:
            driver.back()
            continue
            
        
        # 상품 이름
        el_name = driver.find_elements_by_css_selector('div.bnfraginfoheader > h1.font-heavy > span')[0]

        # 상품 이미지
        images = driver.find_elements_by_css_selector("img.bnheroimage")
        img_url = []
         
        for image in images :
            url = image.get_attribute('src')
            img_url.append(url)
        
        
       # 상품 브랜드
        el_brand = driver.find_element_by_xpath("//span[@itemprop='name']")

       #excuteQuery
        sql="INSERT INTO Perfume(perfume_name, perfume_brand, perfume_img, perfume_gender) VALUES(%s, %s, %s, %s)"
        cur.execute(sql, (el_name.text, el_brand.text, img_url, perfume_gender))
        conn.commit()

    

        # Top Middle Base
        try:
            # Top Middle Base 구분 된 경우
            element = driver.find_element_by_css_selector('ol.fragrancenotes > li > h3')
            element_notes = driver.find_elements_by_css_selector('ol.fragrancenotes > li > ul')

            # Top
            top_notes = element_notes[0].find_elements_by_css_selector('li')
            for i in range(0, len(top_notes)):
                try:
                    aTag_top_note = top_notes[i].find_element_by_tag_name("a")
                except NoSuchElementException:
                    aTag_top_note = top_notes[i]
                    
                #excuteQuery
                try:                    
                    cur.execute('INSERT INTO Perfume_Scent(name) VALUES(%s)', aTag_top_note.text)
                    conn.commit()
                except:
                    pass
                
                #excuteQuery              
                sql = "select id from Perfume_Scent where name=%s"
                cur.execute(sql, aTag_top_note.text)
                scent_id = cur.fetchone()
                conn.commit()

                sql = "select perfume_id from Perfume where perfume_name=%s"
                cur.execute(sql, el_name.text)
                perfume_id = cur.fetchone()
                conn.commit()

                sql = "insert into Perfume_Top(Perfume_Scent_id, Perfume_perfume_id) values(%s, %s)"
                cur.execute(sql, (scent_id[0], perfume_id[0]))
                conn.commit()
                

                
            
            # Middle
            middle_notes = element_notes[1].find_elements_by_css_selector('li')
            for i in range(0, len(middle_notes)):
                try:
                    aTag_middle_note = middle_notes[i].find_element_by_tag_name("a")
                except NoSuchElementException:
                    aTag_middle_note = middle_notes[i]

                #excuteQuery
                try:
                    cur.execute('INSERT INTO Perfume_Scent(name) VALUES(%s)', aTag_middle_note.text)
                    conn.commit()
                except:
                    pass

                #excuteQuery
                try:
                    sql = "select id from Perfume_Scent where name=%s"
                    cur.execute(sql, aTag_middle_note.text)
                    scent_id = cur.fetchone()
                    conn.commit()

                    sql = "select perfume_id from Perfume where perfume_name=%s"
                    cur.execute(sql, el_name.text)
                    perfume_id = cur.fetchone()
                    conn.commit()
                
                    sql = "INSERT INTO Perfume_Middle(Perfume_Scent_id, Perfume_perfume_id) VALUES(%s, %s)"
                    cur.execute(sql, (scent_id[0], perfume_id[0]))
                    conn.commit()
                except:
                    pass

            #Base
            base_notes = element_notes[2].find_elements_by_css_selector('li')
            for i in range(0, len(base_notes)):        
                try:
                    aTag_base_note = base_notes[i].find_element_by_tag_name("a")
                except NoSuchElementException:
                    aTag_base_note = base_notes[i]

                #excuteQuery
                try:
                    cur.execute('INSERT INTO Perfume_Scent(name) VALUES(%s)', aTag_base_note.text)
                    conn.commit()
                except:
                    pass

                #excuteQuery
                try:
                    sql = "select id from Perfume_Scent where name=%s"
                    cur.execute(sql, aTag_base_note.text)
                    scent_id = cur.fetchone()
                    conn.commit()

                    sql = "select perfume_id from Perfume where perfume_name=%s"
                    cur.execute(sql, el_name.text)
                    perfume_id = cur.fetchone()
                    conn.commit()
                    
                    sql = "INSERT INTO Perfume_Base(Perfume_Scent_id, Perfume_perfume_id) VALUES(%s, %s)"
                    cur.execute(sql, (scent_id[0], perfume_id[0]))
                    conn.commit()
                except:
                    pass

        except NoSuchElementException:
            element_all_notes = driver.find_elements_by_css_selector('ol.fragrancenotes > li > ul >li')

            # None_Note
            for i in range(0, len(element_all_notes)):
               try:
                   aTag_all_note = element_all_notes[i].find_element_by_tag_name("a")
               except:
                   aTag_all_note = element_all_notes[i]

               #excuteQuery
               try:
                   cur.execute('INSERT INTO Perfume_Scent(name) VALUES(%s)', aTag_all_note.text)
                   conn.commit()
               except:
                   pass

               #excuteQuery
               try:
                   sql = "select id from Perfume_Scent where name=%s"
                   cur.execute(sql, aTag_all_note.text)
                   scent_id = cur.fetchone()
                   conn.commit()

                   sql = "select perfume_id from Perfume where perfume_name=%s"
                   cur.execute(sql, el_name.text)
                   perfume_id = cur.fetchone()
                   conn.commit()

                   sql = "INSERT INTO Perfume_None_Note(Perfume_Scent_id, Perfume_perfume_id) VALUES(%s, %s)"
                   cur.execute(sql, (scent_id[0], perfume_id[0]))
                   conn.commit()
               except:
                   pass              
        driver.back()      
    driver.find_element_by_xpath('//*[@id="top"]/div[2]/div[2]/div[5]/div/div[2]/div[4]/div/div/div[3]/nav/div[1]/a[2]').send_keys(Keys.ENTER)                              
conn.close()
driver.close()


