import pymysql
#打开数据库
db = pymysql.connect('localhost', 'root', '123456', 'pymysql')
#创建一个游标对象
curors = db.cursor()
curors.execute("DROP TABLE py")
#创建表
sql = """CREATE TABLE py (
         id  int(20) NOT NULL PRIMARY KEY,
         name  CHAR(20),
         age INT(10),  
         sex CHAR(1),
         incone FLOAT )"""
curors.execute(sql)
curors.close()
