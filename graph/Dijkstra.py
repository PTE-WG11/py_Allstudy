from pythonds.graphs import PriorityQueue, Graph, Vertex

"""

"""

def dijkstra(aGraph, start):
    pd = PriorityQueue()  # 创建一个优先级队列
    start.setDistance(0)  # 设置dist为0
    pd.buildHeap([(v.getDistance(), v) for v in aGraph])  # 顶点
    while not pd.isEmpty():
        currentVert = pd.delMin()  # 删除最小的
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pd.decreaseKey(nextVert, newDist)  # 删除已经走过的点





# dijkstra(aGraph, start)
