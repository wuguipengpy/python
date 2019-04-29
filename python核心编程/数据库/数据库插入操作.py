import pymysql
db = pymysql.connect('localhost', 'root', '123456', 'pymysql')
a = 5
b = 'wuguipeng'
c = 18
d = 'n'
e = 2000
cur = db.cursor()
sql = 'INSERT INTO py VALUES (%s, %s, %s, %s, %s)' % (a, b, c, d, e)

try:
    #执行sql语句
    cur.execute(sql)

    #提交到数据库
    db.commit()
except Exception as e:
    print(e)
db.close()
