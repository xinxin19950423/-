"""
regex    match函数对象演示2
"""
import re
pattern=r"(ab)cd(?P<pig>ef)"
regex=re.compile(pattern)
obj=regex.search("abcdefghijqostmon",0,17)#match对象
#属性方法
print(obj.span())#获取匹配内容的起止位置
print(obj.start())#获取匹配内容的开始位置
print(obj.end())#获取匹配内容的结束位置
print(obj.groupdict())#获取捕获组字典，组名为键，对应内容为值
print(obj.groups())#获取子组对应内容元祖
print(obj.group())
print(obj.group('pig'))
print(obj.group(1))


