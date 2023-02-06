# mySql 연결, 커서 생성
from unittest import result
import pymysql
conn = pymysql.connect(host='mydatabase.cl88hjaqluom.ap-northeast-2.rds.amazonaws.com', user='root', password='dalcteam2', db='mydb', charset='utf8')
cur = conn.cursor()

# 데이터 조회
sql = 'SELECT * FROM User where user_name = %s'
with conn:
    with conn.cursor() as cur:
        cur.execute(sql, ('우영우'))
        result = cur.fetchall()
        for data in result:
            print(data)
