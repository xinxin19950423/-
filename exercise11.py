import pymysql
import re
#链接数据库
db=pymysql.connect(host="localhost",
                   port=3306,
                   user='root',
                   password='123456',
                   database='dict',
                   charset='utf8')

cur=db.cursor()
#执行各种数据库的读写操作
f = open("/home/tarena/1908/month02/code3/dict.txt")

args_list=[]
for line in f:
    #获取单纯和解释
    tup=re.findall(r"(\S+)\s+(.*)",line)[0]
    print(tup)
    args_list.append(tup)
f.close()

sql="insert into words (word,mean) values(%s,%s);"
# print(sql)
try:
    cur.executemany(sql,args_list)
    db.commit()
except:
    db.rollback()


#关闭游标和数据库链接
cur.close()
db.close()