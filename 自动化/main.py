import requests
import urllib

place='英雄山'
print()
html = 'https://www.youbianku.com/SearchResults?address=%s' % urllib.parse.quote(place) # 邮编查询
# ht='https://www.meet99.com/lvyou-jinan.html'  # 景点查询
xpath='//*[@id="mw-content-text"]/div[2]/div/ul/div/table/tbody/tr[3]/td/a'
print(html)
kv = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
      # 'referer': 'https://www.mzitu.com/',
      'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
      # 'cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1575636408; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1575636892'
}


from lxml import etree
wb1_data = requests.get(html)
print('wb1_data',wb1_data)
html = etree.HTML(str(wb1_data.text))
print(html)

html_data = html.xpath(xpath+'/text()')
print(html_data)

# result = etree.tostring(html)
# print('------------------------')
# print(result.decode("utf-8"))