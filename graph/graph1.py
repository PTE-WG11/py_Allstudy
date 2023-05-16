"""
参考文档：
https://www.python.org/doc/essays/graphs/
"""

# 此有向图 有六个节点 （A-F） 和八个弧
"""
它可以由以下Python数据结构表示：
这是一个字典，其键是图形的节点。
对于每个键，相应的值是一个列表，其中包含由来自此节点的直接连接的节点；即两点直接连接
这很简单（更简单的是，节点可以用数字而不是名称来表示，但名称更方便，可以很容易地携带更多信息，例如城市名称）。
"""
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C'],
}

# 找到一个符合条件的路径
"""让我们编写一个简单的函数来确定两个节点之间的路径。
它采用图形以及开始和结束节点作为 参数。
它将返回包含路径的节点列表（包括开始节点和结束节点）。如果找不到路径，则返回 None。
同一节点在返回的路径上不会出现多次（即它不会包含循环）。
该算法使用了一种称为回溯的重要技术：它依次尝试每种可能性，直到找到解决方案。
"""


def find_path(graph, start, end, path=[]):
    path = path + [start]  # 路径，每一次递归调用时，把当前结点加入已经访问的集合中去
    print("path:%s" % path)
    if start == end:
        return path
    if start not in graph:  # 仅存在此节点 不作为弧头出现，仅作为弧尾[数据结构唐朔飞]
        return None  # 递归结束的条件
    print("graph[{}]:{}".format(start, graph[start]))
    for node in graph[start]:  # 依次访问start的邻接顶点node
        if node not in path:  # 同一节点在返回的路径上不会出现多次
            print("node:{}".format(node))
            newpath = find_path(graph, node, end, path)  # 递归调用时传入参数path
            # print("newpath:{}".format(newpath))
            # newpath=False
            if newpath:
                # print("if--newpath:{}".format(newpath))
                return newpath  # 找到一条路径便结束循环
    return None


"""
更改上函数以返回所有路径的列表（不带循环），而不是它找到的第一个路径
"""


# 找到所有的路径
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)  # 找到的路径加入路径列表
    return paths


# 最短路径
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if shortest is None or len(newpath) < len(shortest):
                # if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

"""
find_shortest_path可以使用BFS[广度优先搜索]在线性时间内完成。
此外，线性BFS更简单
"""

# path = find_path(graph, 'D', 'C')
# print(path)
# #---------------------------
# paths = find_all_paths(graph, 'A', 'C')
# print(paths)
# row = 1
# for path in paths:
#     print(row, end=":")
#     print(path)
#     row = row + 1
# #---------------------------
shortest = find_shortest_path(graph, 'A', 'D')
print(shortest)