
import pymysql

#链接数据库
db=pymysql.connect(host="localhost",
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu1',
                   charset='utf8')

#创建游标对象(操作数据库，执行sql语句的)
cur=db.cursor()
#存储图片
with open("/home/tarena/day06#备份/11.png",'rb') as f:
    data=f.read()
try:
    sql="insert into imag values(1,%s,%s);"
    cur.execute(sql,['11.png',data])
    db.commit()
except:
    db.rollback()

#关闭游标和数据库链接
cur.close()
db.close()