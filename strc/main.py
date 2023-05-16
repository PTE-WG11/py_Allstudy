# ##数据类型的性能
# 四种生成前n个证书列表的方法

# 1、循环列表（+）方式生成 --最慢
def test1():
    L = []
    for i in range(1000):
        L = L + [i]


# 2、用append方法添加元素生成
def test2():
    L = []
    for i in range(1000):
        L.append(i)


# 3、列表推导式来做
def test3():
    L = [i for i in range(1000)]
    return None


# 4、range函数调用转成列表-----速度最快
def test4():
    L = list(range(1000))

from timeit import Timer
# 指定反复执行 1000 次，找到时间
# t1=Timer("test1()","from __main__ improt tes1") ## 错误语句
t1=Timer(stmt="test1()",setup="from strc.main import test1")
print("cancat %f seconds\n" % t1.timeit(number=1000))

t2=Timer(stmt="test1()",setup="from strc.main import test1")
print("append %f seconds\n" % t1.timeit(number=1000))

t3=Timer(stmt="test1()",setup="from strc.main import test1")
print("comprehension %f seconds\n" % t1.timeit(number=1000))

t4=Timer(stmt="test1()",setup="from strc.main import test1")
print("list() %f seconds\n" % t1.timeit(number=1000))