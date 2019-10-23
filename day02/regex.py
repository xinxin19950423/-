"""
regex 函数演示
"""
import re
s='Alex:1995,Sunny:1997'
pattern=r"(\w+):(\d)"
#re模块直接调用
# l=re.findall(pattern,s)
# print(l)

#compile对象调用
regex = re.compile(pattern)
l=regex.findall(s,0,15)
print(l)



#使用正则表达式匹配内容,切割目标字符串
l=re.split(r"[:,]",s,1)
print(l)

#使用一个字符串替换正则表达式匹配到的内容参
s=re.subn(r":",',''---',s,2)
print(s)