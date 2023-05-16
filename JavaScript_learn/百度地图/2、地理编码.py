'''
参考：
https://blog.csdn.net/qq_33356563/article/details/86559720?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164956334716780271523102%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=164956334716780271523102&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-86559720.nonecase&utm_term=%E7%99%BE%E5%BA%A6%E5%9C%B0%E5%9B%BE&spm=1018.2226.3001.4450
'''

# 地理编码
from urllib.parse import quote
from urllib.request import urlopen\
    # , quote
import json
# import coordinateTransform

address = "西安市"
ak = 'XST7XPvm4MfGQsB70o1uFHAAs7y0QKv2'
url = 'http://api.map.baidu.com/geocoder/v2/?address='
output = 'json'
# ak = '你的ak'#需填入自己申请应用后生成的ak
add = quote(address)  # 本文城市变量为中文，为防止乱码，先用quote进行编码
url2 = url + add + '&output=' + output + "&ak=" + ak
req = urlopen(url2)
print(req)
res = req.read().decode()
temp = json.loads(res)
print(temp)
lng = temp['result']['location']['lng']  # 获取经度
lat = temp['result']['location']['lat']  # 获取纬度
list1 = [lng, lat]
print('百度坐标为：', list1)

# 逆编码
# import requests
# address = '39.83637707633588,115.58006911450369'
# # address=str(i[0])+','+str(i[1])
# url = 'http://api.map.baidu.com/geocoder?output=json&key=f247cdb592eb43ebac6ccd27f796e2d2&location=' + str(address)
# response = requests.get(url)
# answer = response.json()
# print(answer)