import re

# -----------------------------
# #6、? --贪婪模式和非贪婪模式
# ##。
source = '<html><head><title>Title</title>'
p = re.compile(r'<.*>')
print(p.findall(source))
# ##>> ['<html><head><title>Title</title>']

# 非贪婪模式（尽可能少的匹配）
p = re.compile(r'<.*?>')
print(p.findall(source))
# ##>>['<html>', '<head>', '<title>', '</title>']

# -----------------------------
# #7、反斜杠\ ---对元字符的转义
# ##。
text = """
苹果.是绿色的
橙子.是橙色的
香蕉.是黄色的
"""
p = re.compile(r'.*\.')  # 点前面的内容
for one in p.findall(text):
    print(one)

# ### 转义\---匹配某种字符类型
"""
\d 匹配0-9之间任意一个数字字符，等价于表达式 [0-9]

\D 匹配任意一个不是0-9之间的数字字符，等价于表达式 [^0-9]

\s 匹配任意一个空白字符，包括 空格、tab、换行符等，等价于表达式 [\t\n\r\f\v]

\S 匹配任意一个非空白字符，等价于表达式 [^ \t\n\r\f\v]

\w 匹配任意一个文字字符，包括大小写字母、数字、下划线，等价于表达式 [a-zA-Z0-9_]

缺省情况也包括 Unicode文字字符，如果指定 ASCII 码标记，则只包括ASCII字母

\W 匹配任意一个非文字字符，等价于表达式 [^a-zA-Z0-9_]

"""
text = """
王撒旦
五大三
tony
"""
p = re.compile(r'\w{2,4}', re.A)  # ASCII编码的文字字符的英文
# ##>>tony

# -----------------------------
# #8、方括号[] ---匹配几个字符之一
# ##。方括号表示要匹配 指定的几个字符之一 。
text8 = """
王亚辉，13500344799，89
徐志摩，1b900785634，23
周根源，15909875678， 44
周根源，17909875678， 44
郝云摩，05900785634，23
李根源，23909875678，44
"""
# 匹配有效的电话号码
p = re.compile(r'1[3-9]\d{9}')
print(p.findall(text))
# ****一些 元字符 在 方括号内 失去了魔法， 变得和普通字符一样了。
# ##==>> [akm.] 匹配 a k m . 里面任意一个字符

# 如果在方括号中使用 ^ ， 表示 非 方括号里面的字符集合。
# ##==>>[^\d] 表示，选择非数字的字符
content = 'a1b2c3d4e5'
p = re.compile(r'[^\d]')
for one in p.findall(content):
    print(one)

# -----------------------------
# #9、起始、结尾位置 和 单行、多行模式
# ##。 ^ 表示匹配文本的 开头 位置。
# ##。 $ 表示匹配文本的 结尾 位置。
"""
正则表达式可以设定 单行模式 和 多行模式

单行模式，表示匹配 整个文本 的开头位置。

多行模式，表示匹配 文本每行 的开头位置。"""
text9 = """
001-苹果价格-60,
002-橙子价格-70,
003-香蕉价格-80,
"""
p = re.compile(r'^\d+')  # 单行模式（默认）
p = re.compile(r'^\d+', re.M)  # 多行模式
# p = re.compile(r'\d+,$', re.M)  # 结尾$ 多行模式
print(p.findall(text9))
for one in p.findall(text9):
    print(one)

# -----------------------------
# #9、竖线| ---匹配其中之一
# ##。竖线隔开的部分是一个整体
"""竖线隔开的部分是一个整体
"""
text09="""
001-苹果价格-60,
002-橙子价格-70,
003-香蕉价格-80,
"""
p = re.compile(r'/苹果|橙子|香蕉|菠萝/gm')  # 多行模式
print(p.findall(text09))



