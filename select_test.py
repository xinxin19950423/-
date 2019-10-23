"""
select 演示
"""
from select import  select
from socket import *
#第一个IO
s=socket()
s.bind(('127.0.0.1',8888))
s.listen(3)
#第二个IO
f=open("test.txt","w+")

print("监控IO")
# rs, ws, xs=select([s],[],[],3)#timeout 超时时间
rs, ws, xs=select([s],[f],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)



