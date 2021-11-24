import re
import pymongo

from bs4 import BeautifulSoup
import requests,json

url = 'http://www.caab.gov.bd/aip/amd/amd.html'
response = requests.get(url)
response.encoding = 'utf-8'

print('----------------')
responseStr = response.text

soup = BeautifulSoup(responseStr,'lxml')
# print(soup.prettify())
print('-----------------')
print(soup.find_all(text=re.compile('AIP AMENDMENT 01/18')))
pdf = soup.find_all('font')[3].parent.find_all('a')[0].attrs['href']
# print(pdf)

def getPdf(pfd):
    url = 'http://www.caab.gov.bd/aip/amd/checklist08dec2016.pdf'
    print(url)
    # headers = {
    #     'Host': 'www.caab.gov.bd',
    #     'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64;rv: 67.0) Gecko / 20100101Firefox / 67.0',
    #     'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, * / *;q = 0.8',
    #     'Accept - Language': 'zh - CN, zh;q = 0.8, zh - TW;q = 0.7, zh - HK;q = 0.5, en - US;q = 0.3, en;q = 0.2',
    #     'Accept - Encoding': 'gzip, deflate',
    #     'Connection': 'keep - alive',
    #     'Referer': 'http: // www.caab.gov.bd / aip / amd / amd.html',
    #     'Upgrade - Insecure - Requests': '1',
    #     'Range': 'bytes = 304359 -',
    #     'If - Range': '1a7125-56c22607b9cf8'
    # }
    return requests.get(url).text

if __name__=='__main__':
    print(getPdf(pdf))
    print(type(getPdf(pdf)))
