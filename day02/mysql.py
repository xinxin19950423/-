"""
mysql 擦着数据库流程演示
"""
import pymysql

#链接数据库
db=pymysql.connect(host="localhost",
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')

#创建游标对象(操作数据库，执行sql语句的)
cur=db.cursor()
#执行各种数据库的读写操作

#关闭游标和数据库链接
cur.close()
db.close()