import time

time.sleep(3)
# import sklearn
# 基础语法
print('ssa')

# 缩进四个空格
# for i in range(10):
#     print(i)

# 单行注释  ctrl + /
"""
多行注释
"""

str1 = '12'
str2 = 'ab'
print('str1:{}'.format(str1))
print('str2:%s' % (str2))

stea = 1213.123
print(type(stea))
print(type(str1))

b1, b2, b3 = 1, 2, 3,
print(b1, b2, b3)

list1 = ['sa', 123]
for i in list1:
    print(i)
# len(list1)
# str(list1)
c = '"1+2"'
z=eval(c)
print('z:',z)
# 元组
tup = tuple()
tup2 = (1, 2, 3)
list1[0] = 1
##  tup2[0]=1 错误做法
# list1.append()
# list1.pop()
# ...

dic = {'name': 'WGY', 'age': '18'}  # 字典--数据类型
dic['da'] = 'sada'

for key,value in dic.items():
    # print(key)
    print(key,value)


# 没有++ -- 有+= -=
# not
c = ''
# True False and or
if not c:
    print('zzzzz')

cc = '' + ''