# -*- coding: UTF-8 -*-
# !/usr/bin/python

# -----------------------------------------------------------------------
# python3.6
# wgraph.py
# 图的数据结构，以邻接表的方式存储结点
# -----------------------------------------------------------------------

import sys
import stdio
from MYsteam import InStream
from MYsteam import OutStream

MAXL = sys.maxsize


# -----------------------------------------------------------------------
# 无向带权图
class WGraph:

    # 构造函数，从文件或命令行读取边
    def __init__(self, filename=None, delimiter=None):
        self._e = 0  # 边数
        self._adj = dict()  # 顶点,邻接表
        self.lpath = []
        if filename is not None:
            instream = InStream(filename)
            while instream.hasNextLine():
                line = instream.readLine()
                names = line.split(delimiter)  # [点A,点B,距离]
                if len(names) > 0:  # 防止无效的行
                    if names[-1].isdigit():
                        for i in range(1, len(names) - 1):  # 最后一个元素表示边的权值
                            self.addEdge(names[0], names[i], names[-1])
                    else:
                        for i in range(1, len(names)):  # 最后一个元素不是数值表示无权图，默认权为1
                            self.addEdge(names[0], names[i], 1)

    def addEdge(self, v, w, weight):
        if not self.hasVertex(v): self._adj[v] = {}
        if not self.hasVertex(w): self._adj[w] = {}
        if not self.hasEdge(v, w):
            self._e += 1
            self._adj[v][w] = int(weight)
            self._adj[w][v] = int(weight)
            # 创建时,两条边都创建,删除时,两条边都删除

    # 顶点v连接的顶点
    def adjacentTo(self, v):
        return iter(self._adj[v])

    # 获取顶点
    def vertices(self):
        return iter(self._adj)

    # 返回bool,是否有顶点
    def hasVertex(self, v):
        return v in self._adj

    # 返回bool,判断w,v是否相连
    def hasEdge(self, v, w):
        return w in self._adj[v]

    # 返回顶点的数量
    def countV(self):
        return len(self._adj)

    # 返回所有的边数
    def countE(self):
        return self._e

    # 返回顶点V的度，
    def degree(self, v):
        return len(self._adj[v])

    def print_path(self, lis, o):
        for x in lis:
            print("%s -> " % x, end='')
            # o.write("%s -> " % x)
        # print("\n", end='')
        # o.writeln()

    # 回溯输出（A->B）所有的路径
    # 深度优先的搜索方法 回溯法 P132
    # 全局变量 self.lpath
    def allpath(self, start, end, o):
        self.lpath += [start]
        if start == end:
            self.print_path(self.lpath, o)
        else:
            for v in self.adjacentTo(str(start)):  # 遍历起点临界的节点
                if v not in self.lpath:
                    self.allpath(v, end, o)
        self.lpath.pop()

    # 寻找最进的节点
    def __findShorestNode(self, cost, visited):
        minDist = MAXL
        node = None
        for i in self.vertices():
            if (cost[i] < minDist) and (i not in visited):
                minDist = cost[i]
                node = i
        return node

    # 返回从源结点s到所有每个结点的最短路径代价字典cost，和路径指向字典parents
    # cost[i]就是从s到达i的最小代价值，parents[i]存储从s到达i的最短路径上, i的前一个结点
    def dijkstra(self, s):
        cost = {}
        visited = [s]
        parents = {s: None}
        # 初始化cost字典
        for v in self.vertices():
            if self.hasEdge(s, v):
                cost[v] = self._adj[s][v]
            else:
                cost[v] = MAXL
        cost[s] = 0
        # 初始化parents字典
        for i in self.adjacentTo(s):
            parents[i] = s

        node = self.__findShorestNode(cost, visited)
        while node:
            for i in self.adjacentTo(node):  # 所有node结点的邻居结点
                newcost = cost[node] + self._adj[node][i]
                if newcost < cost[i]:
                    parents[i] = node  # 最短路径到达i的路径上，i的上一个结点是node
                    cost[i] = newcost
            visited.append(node)
            node = self.__findShorestNode(cost, visited)

        return cost, parents

    #
    def __str__(self):
        str1 = ''
        for vertex in self.vertices():
            str1 += vertex + '  '
            for w in self.adjacentTo(vertex):
                str1 += w + ' '
            str1 += '\n'
            print(str1)
        return str1


# -----------------------------------------------------------------------
# 返回从图graph中源结点source到目的结点destination的最短路径
# 返回空字典cost和列表spath，表示graph不是一个连通图
def shortestPath(graph, source, destination):
    s = source
    t = destination
    cost = {}
    spath = []
    if graph.hasVertex(s) and graph.hasVertex(t):
        cost, parents = graph.dijkstra(s)
        if MAXL in cost.values():  # graph不是一个连通图(只有一个连通分量)
            return {}, []
        path = []
        p = parents[t]
        while (p):
            path.append(p)
            p = parents[p]
        spath = list(reversed(path)) + [t]
    return cost, spath


#
def main():
    # file = sys.argv[1]
    file1 = r'D:\MyFile\SoftwareFile\PycharmProjects\py_Allstudy\graph\GFmetro.txt'  # 必须是utf-8编码
    outfile = r'D:\MyFile\SoftwareFile\PycharmProjects\py_Allstudy\graph\output.txt'
    graph = WGraph(file1)
    # stdio.writeln(graph)

    outsream = OutStream(outfile)

    start = u"沥滘"
    end = u"广州东站"
    (cost, path) = shortestPath(graph, start, end)
    # print("path from %s to %s: cost=%d"%(start, end, cost[end]))
    if len(cost) > 0 and len(path) > 0:
        stdio.writeln("path from %s to %s: cost=%d" % (start, end, cost[end]))
        stdio.writeln(path)
    else:  # 非连通图，结束程序
        stdio.writeln("the graph is not a fully connected graph")
        return

        # print("all path")
    outsream.writeln("all path from  %s to %s: " % (start, end))
    graph.allpath(start, end)
    stdio.writeln("output to %s .... ok" % outfile)


if __name__ == '__main__':
    main()
