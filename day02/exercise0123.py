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
list01=[]
def info(id,name,passwd):
    if name not in list01:
        list01.append(name)
        list01.append(id)
        list01.append(passwd)
    sql = 'insert into user (id,name,passwd) values (%s,%s,%s)'
    cur.executemany(sql, list01)
    return db.commit()