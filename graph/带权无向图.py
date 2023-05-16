# 求两点之间的最短路径长度
# https://blog.csdn.net/QuantCoder/article/details/121162053

n, m = 5, 10  # 5个顶点10条边
road = [[1, 2, 2], [1, 3, 3], [1, 4, 7], [1, 5, 2],
        [2, 3, 4], [2, 4, 9], [2, 5, 5], [3, 4, 4],
        [3, 5, 5], [4, 5, 3]]


def hold(list1, list2):
    jiaoji = list(set(list1) & set(list2))  # list1和list2的交集
    print(jiaoji)
    need = [i for i in set(list1 + list2) if i not in jiaoji]
    print(need)
    need.sort()
    print(need)
    return need


def get(road):
    option = {}
    for i in range(m):
        option[(road[i][0], road[i][1])] = [road[i][2]]
        print(option)
    for i in range(m):
        for j in range(i + 1, m):
            dot = hold(road[i][:2], road[j][:2])
            if len(dot) == 2:
                if (dot[0], dot[1]) in option.keys():
                    option[(dot[0], dot[1])].append(max([road[i][2], road[j][2]]))
                else:
                    option[(dot[0], dot[1])] = []
                    option[(dot[0], dot[1])].append(max([road[i][2], road[j][2]]))
    road_new = []
    for i in option.items():
        road_new.append(list(i[0]) + [min(i[1])])
    if road == road_new:
        print(road_new)
        return road_new
    return get(road_new)



list1, list2 = [2, 3, 4], [2, 4, 9]
# list1,list2=[2, 5, 5], [3, 4, 4]
print(list1[:2], list2[:2])
ed = hold(list1[:2], list2[:2])
print(ed)

# get(road)