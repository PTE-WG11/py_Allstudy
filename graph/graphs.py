"""ADT
Graph() 新建一个空图
addVertex(vert)向图中添加一个顶点实例
addEdge(fromVert,toVert)向图中添加一条有向边，用于连接顶点formVert和toVert
addEdge(fromVert,toVert，weight)带权重的有向边
getVertex(vertkey)在图中找到名为vertkey的顶点
getVertices()以列表形式返回图中所有顶点
vertex in graph 判断顶点是否存在

-----邻接表-----
  顶点列表 | 定点对象
0  id = v0 adj={v1:5, v5:2}
1  id = v1 adj={v2:4}
2  id = v2 adj={v3:9}
3  id = v3 adj={v4:7, v5:3}
4  id = v4 adj={v0:1}
5  id = v5 adj={v2:1, v4:0}

"""


class Vertex:
    """
    Vertex类表示图中的每一个顶点
    connectedTo：记录与其相连的每一个顶点，以及每一条边的权重
    """

    def __init__(self, key):
        """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        # 添加从一个顶点到另一个顶点的连接
        self.connectedTo[nbr] = weight

    def __str__(self):
        # 创建对象后返回给对象
        return str(self.id) + 'connectedTo:' \
               + str([x.id for x in self.connectedTo])

    def getConnections(self):
        # 返回邻接表的所有顶点
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        # 返回从当前顶点到以参数传入的顶点之间的边的权重
        return self.connectedTo[nbr]


class Graph:
    """
    包含一个将‘顶点名’映射到‘顶点对象’的 字典。  邻接表实现
    提供了向图中添加顶点和连接不同顶点的方法。

    """

    def __init__(self):
        self.vertList = {}  # 垂直列表
        self.numVertices = 0  # 顶点数量

    def addVertex(self, key):
        # 添加顶点
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)  # 调用并返回__str__
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        # 返回图中所有顶点的名字
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        # 添加新的边
        if f not in self.vertList:  #  如果f、t顶点不在顶点集里就加入
            nv=self.addVertex(t)
        if t not in self.vertList:
            nv=self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)
    def getVertices(self):
        # 获取顶点
        return self.vertList.keys()
    def __iter__(self):
        # 遍历图中所有顶点
        return iter(self.vertList.values())


g=Graph()
for i in range(6):
    g.addVertex(i)
# print(g.vertList)
# g.addEdge(0,1,5)
# g.addEdge(0,5,2)
# g.addEdge(1,2,4)
# g.addEdge(2,3,9)
# g.addEdge(3,4,7)
# g.addEdge(3,5,3)
# g.addEdge(4,0,1)
# g.addEdge(5,4,8)
# g.addEdge(5,2,1)
# for v in g:
#     for w in v.getConnections():
#         print("(%s,%s)"%(v.getId(),w.getId()))
