import timeit
import random
"""
设计一个性能试验来验证list中检索懿个值，以及dict中检索一个之的计时对比

生成包含连续值的list和包含连续关键码key的dict，用随机数来检验操作符in的耗时
"""
for i in range(100000, 1000001, 20000):

    # 此句 在查找列表和字典用法一样 都用关键字 in
    t = timeit.Timer("random.randrange(%d) in x" % i,
                     "from strc.test2 import random,x")

    x = list(range(i))          # 列表
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}     # 字典循环j{j:None}

    d_time = t.timeit(number=100)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))


"""# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# 
# # data = np.random.randint(0, 255, size=[40, 40, 40])
# y,x1,x2=i,lst_time,d_time
# # x, y, z = data[0], data[1], data[2]
# # ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
# ax=plt.subplot(111,projection='3d')
# # #  将数据点分成三部分画，在颜色上有区分度
# # ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
# # ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
# # ax.scatter(x[30:40], y[30:40], z[30:40], c='g')
# ax.scatter(y,x1,x2,c='x')
# ax.set_zlabel('Z')  # 坐标轴
# ax.set_ylabel('Y')
# # ax.set_xlabel('X')
# plt.show()
"""