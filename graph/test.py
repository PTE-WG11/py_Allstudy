# 建立的图模型 如下：
adj = {
    'A': {'B': 1, },
    'B': {'C': 1, 'D': 2},
    'C': {'D': 2},
    'D': {'C': 2},
    'E': {'F': 1},
    'F': {'C': 2},
}

var = adj['C']
i = iter(adj)
print(i)
print(len(adj['B']))
