import requests

kv = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    # 'referer': 'https://www.mzitu.com/',
    # 'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1575636408; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1575636892'
}
html = requests.get('https://www.meet99.com/lvyou-jinan.html', headers=kv)
with open('jinan.html', "w", encoding='utf-8') as p:
    p.write(html.text)


# print(html.text)

def getInformation(html):
    from lxml import etree

    htmlTree = etree.HTML(str(html.text))
    li_xpath = '/html/body/div[3]/div[1]/ul/li'
    level = htmlTree.xpath(li_xpath)
    print(len(level))
    lisInfo = []
    for num in range(0, len(level)):
        name_xpath = '//*[@id="tiles"]/li[' + str(num) + ']/div[2]/a' + '/text()'
        href_xpath = '//*[@id="tiles"]/li[' + str(num) + ']/div[2]/a' + '/@href'
        level_xpath = '/html/body/div[3]/div[1]/ul/li[' + str(num) + ']/div[3]/div' + '/text()'
        # img_xpath='/html/body/div[3]/div[1]/ul/li['+str(num)+']/div[2]'+'/@style'
        # print(htmlTree)
        name = htmlTree.xpath(name_xpath)
        href = htmlTree.xpath(href_xpath)
        level = htmlTree.xpath(level_xpath)
        # img.get('style')
        # print([name, href, level])
        # print(len(name))
        if len(name) == 0:
            pass
        else:
            lisInfo.append([name, href, level])
        # print(lisInfo)
    return lisInfo


lisInfo = getInformation(html)  # 二维数组 [ [name, href, level],  ]
# with open('info_jingdian.txt'):

with open('info_name_jingdian.txt', 'w+', encoding='utf-8') as f:
    for line in lisInfo:
        # num = 0
        f.write(line[0][0]+'\n')
        # for i in line:
        #     if len(i ) != 0:
        #         f.write(i[0] + ' ')
        #         # num += 1
        #     else:
        #         f.write('NULL')
        #     print(i)
        # f.write('\n')
        print(line[0])

    # lisInfo
