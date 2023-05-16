# 分支限界法求解旅行商问题
import math
from heapq import *

# 定义图的字典形式
G = {
    '1': {'2': 30, '3': 6, '4': 4,'5':10},
    '2': {'1': 30, '3': 5, '4': 10,'5':10},
    '3': {'1': 6, '2': 5, '4': 20,'5':10},
    '4': {'1': 4, '2': 10, '3': 20,'5':10},
    '5':{'1': 10, '2': 10, '3': 10,'5':10}
}

bestcost = math.inf  # 好吧 干脆就无穷好了
nowcost = 0  # 全局变量，现在的花费


# 设置节点类
class Node:
    # 构造函数，现在的花费，到目前的路径
    def __init__(self, w=math.inf, route=[], cost=0):
        self.weight = w
        self.route = route
        self.cost = cost

    # 重载比较，用于堆的排序
    def __lt__(self, other):
        return int(self.weight) < int(other.weight)

    # 打印
    def __str__(self):
        return "节点的权重为" + str(self.weight) + " 节点的路径为" + str(self.route) + " 花费为" + str(self.cost)


def BBTSP(graph, s):
    global bestcost, bestroute
    heap = []

    start = Node(route=[str(s)])

    heap.append(start)

    # 当堆中有数的时候，循环继续
    while heap:
        nownode = heappop(heap)  # 取出权重最大的那个数
        # 生成权重最大的那个数的下结点，并且把下结点加入堆中
        for e in [r for r in graph if r not in nownode.route]:
            node = Node(w=graph[nownode.route[-1]][e], route=nownode.route + [e],
                        cost=nownode.cost + graph[nownode.route[-1]][e])
            # 如果现在的值大于最优值，剪枝操作
            if node.cost >= bestcost:
                continue
            # 如果到了最后一个点，加上回去的路，并计算最小值
            if len(node.route) == 4:
                wholecost = graph[node.route[-1]][s] + node.cost
                if wholecost < bestcost:
                    bestcost = wholecost
                    bestroute = node.route
                    print("最佳花费为:" + str(bestcost))
                    print("最佳路径为:" + str(bestroute))

            heap.append(node)

    return bestcost


BBTSP(G, '1')
print(bestroute)