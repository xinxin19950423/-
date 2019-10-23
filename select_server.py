"""
select 实现tcp服务

重点代码
1.所有IO使用select监控
2.每个IO发生时，进行处理，没有发生时，即进入监控状态
3.每个IO不会长期阻塞服务端的执行
"""
from socket import *
from select import select

#创建套接字，作为关注的IO
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

#将关注的IO放入对应的监控类别列表
rlist=[s]
wlist=[]
xlist=[]

#监控IO的发生
while True:
    rs, ws, xs=select(rlist,wlist,xlist)
    #for 循环依次取出就绪IO
    for r in rs:#这的rs是准备好的返回值
        if r is s:#将取出的IO根据情况进行处理
            c,addr=rs[0].accept()
            print("连接的地址:",addr)
            rlist.append(c)#将c加入监控列表
        else:#有客户端发消息
            data=r.recv(1024).decode()
            if not data:
                rlist.remove(r)#对应套接字不再关注
                r.close()
            else:
                print(data)
                # r.send(b"OK")
                wlist.append(r)#将这个IO写入监控

    for w in rs:
        w.send(b"wlist wow")
        wlist.remove(w)#再发下一个消息时，会重复上一个消息，所以得删掉

    for x in rs:
        pass














