import requests
from lxml import etree
url = 'http://www.66ip.cn/areaindex_35/index.html'

headers = {
    'Host': 'www.66ip.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Referer': 'http://www.66ip.cn/areaindex_35/index.html',
    'Cookie': '__jsluid=5790230d8da115221a1d1a6bb6e5ead8; __jsl_clearance=1562055335.363|0|YSKFMeXeJn0FsCjQBnz5oL6JFVw%3D; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1562055337; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1562055366',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

response = requests.get(url, headers=headers)
# response.encoding = 'utf-8'
# print(response.text)
html = etree.HTML(response.text)
for i in range(1, 18):
    print(html.xpath("//body/div[@class='container']//table//tr//td/text()")[5 * i])

