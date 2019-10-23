"""
write 写操作亚演示
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
#执行各种数据库的写操作
try:
    #执行增删改操作
    # sql='insert into class1 (name,age,score) values ("小新",100,100)'
    # sql="update class1 set sex='m' where name='李新鑫'"
    # sql="delete from class1 where name='李新鑫'"
    # cur.execute(sql)

    #从input输入语句，传给sql
    # name=input("Name:")
    # age=int(input("Age:"))
    # score=float(input("Soore:"))
    # sql = 'insert into class1 (name,age,score) values (%s,%s,%s)'
    # cur.execute(sql,[name,age,score])


    # executemany  多次执行sql
    exe=[]
    for i in range(2):
        name = input("Name:")
        age = int(input("Age:"))
        score = float(input("Soore:"))
        exe.append((name,age,score))
    sql = 'insert into class1 (name,age,score) values (%s,%s,%s)'
    cur.executemany(sql,exe)


    db.commit()#将结果立刻提交




except Exception as e:
    db.rollback()#回滚
    print(e)


#关闭游标和数据库链接
cur.close()
db.close()