import re

# 1、分割字符
names = '关羽; 张飞, 赵云,马超, 黄忠  李逵'
namelst = re.split(r'[;,\s]\s*', names)  # \s表示空白字符 \s*表示不定数量的空格
print(namelst)

# 2、字符串替换
text2 = '''
下面是这学期要学习的课程：
<a href='https://www.bilibili.com/video/av66771949/?p=1' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是牛顿第2运动定律
<a href='https://www.bilibili.com/video/av46349552/?p=125' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是毕达哥拉斯公式
<a href='https://www.bilibili.com/video/av90571967/?p=33' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是切割磁力线
'''
# ##①匹配模式替换 --re.sub方法
# ## 被替换的内容不是固定的，所以没法用 字符串的replace方法。
"""
第一个参数 /av\d+?/ 这个正则表达式，
    表示以 /av 开头，后面是一串数字，再以 / 结尾的 这种特征的字符串 ，是需要被替换的。
第二个参数，这里 是 '/cn345677/' 这个字符串，表示用什么来替换。
第三个参数是 源字符串。"""
newStr = re.sub(r'/av\d+?/', '/cn345677/', text2)
print(newStr)


# ##②指定替换函数sub(正则，替换内容，源文本)
# ##把 sub的第2个参数 指定为一个函数
# 替换函数，参数是 Match对象
def subFunc(match):
    # Match对象 的 group(0) 返回的是整个匹配上的字符串，
    src = match.group(0)
    # print(type(src), end=':')
    # print(src)
    # print(type(match), end=":")
    print('--------')
    print(match)
    print(match.group())
    print(match.group(1))
    # Match对象 的 group(1) 返回的是第一个group分组的内容
    # （若有第二个括号分组就用group（2）调用）
    number = int(match.group(1)) + 6
    dest = f'/av{number}/'

    print(f'{src} 替换为 {dest}')
    print()
    # 返回值就是最终替换的字符串
    return dest

# 匹配的一个字符串(无视分组（包括/av）分组在group用到）调用一次subFunc函数
newStr = re.sub(r'/av(\d+?)/', subFunc, text2)  # ?表示非贪婪模式
print(newStr)