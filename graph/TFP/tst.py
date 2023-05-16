# import numpy as np
# dis=np.zeros(0,0)
# print()
# 回溯法求解旅行商问题
import math

n = 4
x = [0, 2, 3, 1, 4]

# 定义图的数组形式
graph = [
    [0, 30, 6, 4, 2],
    [30, 0, 5, 10, 6],
    [6, 5, 0, 20, 6],
    [4, 10, 20, 0, 2],
    [2, 6, 6, 2, 0]
]

# bestcost = 1<<32 # 这里只要是一个很大数就行了 无穷其实也可以
bestcost = math.inf  # 好吧 干脆就无穷好了
nowcost = 0  # 全局变量，现在的花费
vv = []
ii=0

def TSP(graph, n, s):
    global nowcost, bestcost

    # vv=[]
    if s == n:
        if graph[x[n - 1]][x[0]] != 0 and (nowcost + graph[x[n - 1]][x[0]] < bestcost):
            print('best way:', x)
            global vv,ii
            # print('ii',ii)
            vv.append(x)
            bestcost = nowcost + graph[x[n - 1]][x[0]]
            print('bestcost', bestcost)
    else:
        for i in range(s, n):

            # 如果下一节点不是自身 而且 求得的值小于目前的最佳值
            if (graph[x[i - 1]][x[i]] != 0 and nowcost + graph[x[i - 1]][x[i]] < bestcost):
                x[i], x[s] = x[s], x[i]  # 交换一下

                nowcost += graph[x[s - 1]][x[s]]  # 将花费加入
                TSP(graph, n, s + 1)
                nowcost -= graph[x[s - 1]][x[s]]  # 回溯上去还需要减去

                x[i], x[s] = x[s], x[i]  # 别忘记交换回来


c = TSP(graph, n, 4)
# print(c)
print(bestcost)
print(vv)
