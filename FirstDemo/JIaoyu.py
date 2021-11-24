# 河北省招生考试信息服务网
# 数据中心---院校查询里的数据  --6.26
# 1.F12开发者模式  --> 2.
import requests,json
import numpy as np

from Sql import insert

baseUrl = 'http://www.hebzhiyuan.com/api/colleges'

def getPgae(num):
    headers = {
    'Accept':'*/*',
    'Accpet-Encoding':'gzip,deflate',
    'Accept-Language':'zh-CN;q=0.9',
    'Authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1Ijoie1wiaWRcIjpcIjEwOTI0MjkwNjI2NDkgXCIsXCJzY29yZXNcIjo1NzAuMCxcIndjXCI6MzMwMjksXCJrbFwiOlwiQlwiLFwicGNcIjpcIjNcIixcInN0YXJ0VHNcIjpcIjIwMTktMDYtMjZUMTU6MTg6MDEuNTEwMDM2NyswODowMFwiLFwidHNcIjoyMDIuMTc5MDAwODU0NDkyMTksXCJwaG9uZVwiOlwiXCIsXCJkVmFsdWVcIjo2OC4wLFwiclwiOlwiUlwifSJ9.ntY35vi4UosM6P1UfZFk_PVbwTZ5me8NXvCJ9qfKO08',
    'Connection':'keep-alive',
    'Content-Length':'59',
    'Content-Type':'application/json' ,
    'Host':'www.hebzhiyuan.com',
    'Orgin':'http://www.hebzhiyuan.com',
    'Referer':'http://www.hebzhiyuan.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
    data = {
    'parameters':{
        # 'is985': 'true',
        # 'is211':'true'
    },
    '_pager':{
        'size':'15',
        'page':str(num)
    }
}
    res = requests.post(baseUrl,headers=headers,data=json.dumps(data))
    # result = res.json()[1]['items'][0][0]
    # print(result)
    # print(res.text)
    return res.json()

def getSecPage(num):
    headers = {
        'Accept': '*/*',
        'Accpet-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN;q=0.9',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1Ijoie1wiaWRcIjpcIjEwOTI0MjkwNjI2NDkgXCIsXCJzY29yZXNcIjo1NzAuMCxcIndjXCI6MzMwMjksXCJrbFwiOlwiQlwiLFwicGNcIjpcIjNcIixcInN0YXJ0VHNcIjpcIjIwMTktMDYtMjZUMTY6MTM6NDYuNTE4OTc1NCswODowMFwiLFwidHNcIjoyNTcuOTI5MTQ5ODMyODI1NDksXCJwaG9uZVwiOlwiXCIsXCJkVmFsdWVcIjo2OC4wLFwiclwiOlwiUlwifSJ9.swvuPB4lJcZHhwdOwlrMsug25otIK6U8WtVBb6JB8U4',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        # 'Content-Type': 'application/json',
        'Host': 'www.hebzhiyuan.com',
        'Orgin': 'http://www.hebzhiyuan.com',
        'Referer': 'http://www.hebzhiyuan.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    strUrl = 'http://www.hebzhiyuan.com/api/colleges/info/'+num
    res = requests.post(strUrl,headers=headers)
    return res.json()

if __name__ == '__main__':
    row = [[0] * 5 for m in range(3000)]
    k=0
    for i in range(1,71): #1,2
        result = getPgae(i)

        for j in range(len(result[1]['items'])):  #列表的长度--每页学校列表  -- j=0
            row[k][0] = result[1]['items'][j][0]
            row[k][1] = result[1]['items'][j][1]

            # print(result[1]['items'][j][0],result[1]['items'][j][1])
            # print(result)
            print('--------')
            result1 = getSecPage(result[1]['items'][j][0])
            if result1[2]:
                if len(result1[2])>=4:
                    try:
                        row[k][2] = result1[2][0]['maxscores']
                        row[k][3] = result1[2][0]['minscores']
                        row[k][4] = result1[2][0]['averagescores']
                    except:
                        print('爬取异常')
                    finally:
                        k += 1
            else:
                row[k][2] = 0
                row[k][3] = 0
                row[k][4] = 0
                k += 1
            print(result1)  #循环 --得到字符串

    l = 0
    for result in row:
        if l != k:
            insert(result)
            print(result[0], result[1], 'maxscores:', result[2], 'minscores:', result[3], 'averagescores:', result[4])
            l += 1
        else:
            break