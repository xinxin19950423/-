"""
regex 函数演示1
"""
import re
s="2019年10月1日举行了国庆大阅兵，庆祝建国70周年，祖国万岁！！"
pattern=r"\d+"
#返回匹配结果的迭代器
r=re.finditer(pattern,s)
for i in r:
    print(i.group(),end=" ")

#完全匹配某个字符串
m=re.fullmatch(r".+",s)
print(m.group())

print()
#匹配开始位置
m=re.match(r"\w+",s)
print(m.group())

print()

#匹配第一个
m=re.search(r"\d+",s)
print(m.group())