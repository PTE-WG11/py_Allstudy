# 本次整体的源代码
AK = "XST7XPvm4MfGQsB70o1uFHAAs7y0QKv2"
# 服务端aK
# 参考 http://www.zzvips.com/article/211912.html

# import pandas as pd
import requests
import json


# 1.获取对应地点的经纬度

def getPosition(address):
    """
    将传入的address通过地点检索服务得到其经纬度，返回值为经纬度对应的字符串值，
    中间以逗号隔开，之后跟一个查询返回状态，如果查询失败，状态值不为0。
    :param address: 传入地址
    :return:
    """
    url = r"http://api.map.baidu.com/place/v2/search?query={}&region=全国&output=json&ak={}".format(
        address,
        AK  # 这里是一开始截图用红色圈起来的部分
    )
    res = requests.get(url)
    json_data = json.loads(res.text)

    if json_data['status'] == 0:
        lat = json_data["results"][0]["location"]["lat"]  # 纬度
        lng = json_data["results"][0]["location"]["lng"]  # 经度
        # print(lat,lng)
    else:
        print("[ERROR] Can not find {}.".format(address))
        return "0,0", json_data["status"]
    return str(lat) + "," + str(lng), json_data["status"]


def getDistance(start, end):
    """
    将传入的两个地点（以经纬度描述）通过批量算路服务得到之间的路线规划距离。
    本范例是以驾车行驶（对应参数为'driving'）的方式来进行计算的。
    :param start: 起始位置的经纬度
    :param end: 目的地的经纬度
    :return:
    """
    url = "http://api.map.baidu.com/routematrix/v2/driving?output=json&origins={}&destinations={}&ak={}".format(
        start,
        end,
        AK  # 这里是一开始截图用红色圈起来的部分
    )
    res = requests.get(url)
    content = res.content
    # print(res.text)
    # print(content)
    jsonv = json.loads(str(content, "utf-8"))
    print(jsonv)
    dist = jsonv["result"][0]["distance"]["value"]
    # duration = jsonv["result"][0]["duration"]["value"]
    # status = jsonv['status']

    # return dist, duration, status
    return dist


def calcDistance(startName, endName):
    start, status1 = getPosition(startName)
    print('start:', start)
    print(type(start))
    print('status1:', status1)
    end, status2 = getPosition(endName)
    if status1 == 0 and status2 == 0:
        return getDistance(start, end)
    else:
        return -1


if __name__ == "__main__":
    # data = pd.read_excel("data.xlsx")
    # res = []
    # for i in range(0, len(data)):
    #     startName = data.iloc[i, 0]
    #     endName = data.iloc[i, 1]
    #     dist = calcDistance(startName, endName)
    #     res.append([startName, endName, dist / 1000])
    # pd.DataFrame(res).to_excel(
    #     "result.xlsx",
    #     header=["起点", "终点", "距离"],
    #     index=None,
    #     encoding="utf-8"
    # )
    res = []
    startName = '济南趵突泉'
    endName = '济南大明湖公园'
    dist = calcDistance(startName, endName)
    res.append([startName, endName, dist / 1000, 'km'])
    print(res)
