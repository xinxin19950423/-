"""
read_db 读操作亚演示
"""
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

#class1中查找性别为m,分数大于80的学生信息
sql="select * from class1 where sex=%s and score>%s;"
print(sql)
cur.execute(sql,['m',80])#执行语句

#获取所以个查询结果
all_row=cur.fetchall()
print(all_row)

#关闭游标和数据库链接
cur.close()
db.close()