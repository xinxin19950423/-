"""
flags 扩展标志位演示
"""

import re
s="""Hello
北京
"""
#只能匹配ascii字符(键盘可以打出来的字符)
# regex=re.compile(r"\w+",flags=re.A)
#忽略字母大小写
#regex=re.compile(r"[a-z]+",flags=re.IGNORECASE)
# regex=re.compile(r".+",flags=re.S)
regex=re.compile(r"^北京",flags=re.M)
l=regex.findall(s)
print(l)


