import re

"""
正则表达式在线验证：  https://regex101.com/

参考文档：https://www.byhy.net/tut/py/extra/regex/
"""
# 一、普通字符
# 二、特殊元字符--术语叫 metacharacters（元字符）
# . * + ? \ [ ] ^ $ { } | ( )
# # 1、点---匹配所有字符
# . 表示要匹配除了 换行符 之外的任何 单个 字符。
text = """
苹果是绿色的
橙子是橙色的
香蕉是黄色的
乌鸦是黑色的
"""
lst = list()
p = re.compile(r'.色')  # r表示禁止python转义
# print(type(p))
# for one in p.findall(text):
#     lst.append(one)
#     print(one)
#     print(lst)

# -----------------------------
# # 2、星---重复匹配任意次    ，.*
# ## * 表示匹配前面的子表达式任意次，包括0次。
content = '''
苹果，是绿色的
橙子，是橙色色色色的
香蕉，是黄色色的
乌鸦，是黑色的
鸭梨，是绿色的
猴子，'''
# #p = re.compile(r'，.*')
p = re.compile(r'，是.色*')
# #p = re.compile(r'.色*')
# for one in p.findall(content):
#     print(one)

# -----------------------------
# #3、加号---重复匹配多次
# ## + 表示匹配前面的子表达式一次或多次，不包括0次。
p = re.compile(r'，是.色+') # 一次或多次颜色的匹配
for one in p.findall(content):
    print(one)

# -----------------------------
# #4、问号---匹配0-1次
# ## ? 表示匹配前面的子表达式0次或1次。

# -----------------------------
# #5、花括号---匹配指定次数
# ## 花括号表示 前面的字符匹配 指定的次数
r'花括号表示 前面的字符匹配 指定的次数 。'
r'油{2,4}' # 油 字 至少2次，至多 4 次
