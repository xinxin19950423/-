"""
练习：编写一个函数，传入端口号名称，返回
这个端口号运行情况中所描述
的address地址信息
"""
import re

def get_address(port):
    '''
    :param port: 端口名称
    :return: 端口端口对应的address
    '''
    f=open("/home/tarena/桌面/re/╒²╘≥▒φ┤/exc.txt","rb")
    while True:
        data=' '
        for line in f:
            if line=="\n":
                break
            data+=line
        if not  data:
            return "没有找到！！"
        obj=re.match(r"\S+",data)#使用正则匹配一段的第一个单词
        if port==obj.group():
            pattern=r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            obj=re.search(pattern,data)
            if obj:
                return obj.group()






if __name__=='__main__':
    port =input("端口")
    print(get_address(port))

















