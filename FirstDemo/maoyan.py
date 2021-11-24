import re, requests, random, xlsxwriter, pymysql
import time
import xml.dom.minidom as Dom
import numpy as np
from pandas import DataFrame
from lxml import etree

# 抓取猫眼网站数据并保存到mysql数据库，存储xml，execl文件并统计排分
# 保存100部电影的信息，排名，电影名称，演员，上映时间，评分，画报url
_lData = []
_2Data = [[0] * 3 for m in range(100)]
user_agent = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
]
# 返回每页源码
def getPage(num_retries=3):
    baseUrl = 'https://maoyan.com/board/4'
    for i in range(10):
        data = {
            'offset': str(i * 10)
        }
        headers = {
            'User-Agent': random.choice(user_agent)
        }
        try:
            response = requests.get(baseUrl, headers=headers, params=data)
        except requests.exceptions.ConnectionError as e:
            print('请求失败，url:', baseUrl)
            print('详细错误：', e)
            response = None
        if (response.status_code != 200) and (response is not None):
            if (num_retries > 0):
                print('请求错误，正在重试......')
                num_retries -= 1
                time.sleep(2)
                getPage(num_retries)
        # print('抓取第', str(i + 1), '页数据')
        yield response.text
    pass

# 获取电影详情
def getDetails(i,strPage,num_retries=3):
    k = 10*i
    html = etree.HTML(strPage)
    result = html.xpath("//body/div[@class='container']//dl//dd/a/@href")
    for item in result:
        baseUrl = 'https://maoyan.com'+item
        try:
            response = requests.get(baseUrl)
        except requests.exceptions.ConnectionError as e:
            print('请求失败，url:', baseUrl)
            print('详细错误：', e)
            response = None
        if (response.status_code != 200) and (response is None):
            if (num_retries > 0):
                print('请求错误，正在重试......')
                num_retries -= 1
                time.sleep(2)
                getDetails(i,strPage,num_retries)
        html1 = etree.HTML(response.text)
        # print(etree.tostring(html1))
        result1 = html1.xpath("//body/div[@class='container']//div[@class='mod-content']/span//text()")
        result2 = html1.xpath("//body/div[@class='banner']//div[@class='movie-brief-container']/h3//text()")
        result3 = html1.xpath("//body//div[@class='container']//div[@class='tab-content-container']//ul[@class='award-list']//li//text()")
        result3 = [x.strip() for x in result3 if x.strip() != '']
        prize = " ".join(result3)
        if not prize:
            prize = "未获奖"
        _2Data[k][1] = result1
        _2Data[k][0] = result2
        _2Data[k][2] = prize
        k=k+1
        print(result2)
        print(result1)
        print(prize)
# 提取信息
def getPData(strPageSource):
    result = re.findall(
        '<dd.*?index.*?">(.*?)<.*?title="(.*?)".*?data-src="(.*?)".*?star">(.*?)<.*?time">(.*?)</p.*?integer">(.*?)<.*?fraction">(.*?)<',
        strPageSource, re.S)
    for item in result:
        global _lData
        _lData.append(list(item))
        imgCon = getImg(item[2], item[1])
        _lData[len(_lData)-1][3] = item[3].replace('\n', '').replace(' ', '')
        _lData[len(_lData) - 1][3] = _lData[len(_lData)-1][3][3::]
        _lData[len(_lData)-1].append(imgCon)

# 请求图片
def getImg(imgUrl,strTitle):
    headers = {
        'User_Agent' : random.choice(user_agent)
    }
    res = requests.get(imgUrl, headers = headers)
    strPath = r'E:\Campus\PythonExperiment\maoyan\maoyanImg' + '\\'+ strTitle + '.jpg'
    with open(strPath, 'wb')as fw:
        fw.write(res.content)
    return res.content

# 创建xml文件
def createXml():
    strPath = r'E:\Campus\PythonExperiment\maoyan\maoyan.xml'
    doc = Dom.Document()
    rootNode = doc.createElement('maoyan')
    rootNode.setAttribute('Author', 'mine')
    doc.appendChild(rootNode)
    topNode = doc.createElement('Top')
    rootNode.appendChild(topNode)
    for item,item1 in zip(_lData,_2Data):
        rankNode = doc.createElement('Ranking')
        rankNode.setAttribute('No', item[0])
        topNode.appendChild(rankNode)
        tempNode = doc.createElement('Title')
        tempValue = doc.createTextNode(item[1])
        tempNode.appendChild(tempValue)
        rankNode.appendChild(tempNode)
        tempNode = doc.createElement('performer')
        tempValue = doc.createTextNode(item[3])
        tempNode.appendChild(tempValue)
        rankNode.appendChild(tempNode)
        tempNode = doc.createElement('releaseTime')
        nodeValue = doc.createTextNode(item[4])
        tempNode.appendChild(nodeValue)
        rankNode.appendChild(tempNode)
        tempNode = doc.createElement('score')
        strScore = item[5] + item[6]
        nodeValue = doc.createTextNode(strScore)
        tempNode.appendChild(nodeValue)
        rankNode.appendChild(tempNode)
        tempNode = doc.createElement('简介')
        tempValue = doc.createTextNode(str(item1[1]))
        tempNode.appendChild(tempValue)
        rankNode.appendChild(tempNode)
        tempNode = doc.createElement('奖项')
        tempValue = doc.createTextNode(str(item1[2]))
        tempNode.appendChild(tempValue)
        rankNode.appendChild(tempNode)
    with open(strPath, 'w', encoding='UTF-8') as fw:
        doc.writexml(fw, indent='', addindent='\t', encoding='UTF-8')

# excel 文件
def createXlsx():
    strPath = r'E:\Campus\PythonExperiment\maoyan\猫眼数据.xlsx'
    # 创建xlsx的workbook对象(电子表格工作薄)
    workbook = xlsxwriter.Workbook(strPath)
    # 新建工作表
    worksheet = workbook.add_worksheet('猫眼数据')
    # 设置单元格样式， 包括字体 颜色
    cellF = workbook.add_format({"bold": True})
    cellF.set_font('黑体')
    cellF.set_font_color('blue')
    cellF.set_align('center')
    # 向表中添加表头数据
    worksheet.write(0, 0, '影片排行', cellF)
    worksheet.write(0, 1, '电影名称', cellF)
    worksheet.write(0, 2, '主要演员', cellF)
    worksheet.write(0, 3, '上映时间', cellF)
    worksheet.write(0, 4, '影片评分', cellF)
    worksheet.write(0, 5, '电影封面', cellF)
    # 设置列的宽度
    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 10)
    worksheet.set_column('C:C', 30)
    worksheet.set_column('D:D', 40)
    worksheet.set_column('E:E', 10)
    worksheet.set_column('F:F', 20)
    # 插入数据和图片和数据
    fScore = []#评分列表、为第二页数据做准备
    strActors = []#演员列表，为第三页数据做准备
    for i, item in zip(range(1, len(_lData) + 1), _lData):
        worksheet.write_number(i, 0, int(item[0]))
        worksheet.write_string(i, 1, item[1])
        worksheet.write_string(i, 2, item[3])
        for actor in item[3].split(','):
            strActors.append(actor)
        worksheet.write_string(i, 3, item[4])
        fScore.append(float(item[5] + item[6]))
        worksheet.write_number(i, 4, fScore[i - 1])
        worksheet.insert_image(i, 5, r'E:\Campus\PythonExperiment\maoyan\maoyanImg' + '\\' + item[1] + '.jpg')
    # 数据处理，计算出各分数的影片数量
    npScore = np.array(fScore)
    result, iCount = np.unique(npScore, return_counts=True)
    npActors = np.array(strActors)
    result1, iCount1 = np.unique(npActors, return_counts=True)
    d1 = {'actors': result1, 'count' : iCount1}
    df = DataFrame(d1)
    res = df.sort_values(by="count", ascending=False)

    worksheet1 = workbook.add_worksheet('影片统计')
    worksheet1.write(0, 0, '影片评分', cellF)
    worksheet1.write(0, 1, '影片数量', cellF)
    worksheet1.set_column('A:A', 10)
    worksheet1.set_column('B:B', 10)
    for i, score, count in zip(range(0, len(result)), result, iCount):
        worksheet1.write_number(i + 1, 0, score)
        worksheet1.write_number(i + 1, 1, count)
        # 添加图表（柱状图）
        chart = workbook.add_chart({"type": "column"})
        # 添加图表数据
        chart.add_series(
            {
                'name': '同评分影片数量统计',  # 标题
                'categories': '=影片统计!$A$2:$A$9',
                'values': '=影片统计!$B$2:$B$9',
                'line': {'color': 'black', 'bold': True}
            }
        )
        # 圆形图
        chart1 = workbook.add_chart({"type": "pie"})
        # 添加图表数据
        chart1.add_series(
            {
                'name': '同评分影片数量统计',  # 标题
                'categories': '=影片统计!$A$2:$A$9',
                'values': '=影片统计!$B$2:$B$9',
                'line': {'color': 'black', 'bold': True}
            }
        )
        # 折线图
        chart2 = workbook.add_chart({"type": "line"})
        # 添加图表数据
        chart2.add_series(
            {
                'name': '同评分影片数量统计',  # 标题
                'categories': '=影片统计!$A$2:$A$9',
                'values': '=影片统计!$B$2:$B$9',
                'line': {'color': 'black', 'bold': True}
            }
        )
        # 股票趋势
        chart3 = workbook.add_chart({"type": "doughnut"})
        # 添加图表数据
        chart3.add_series(
            {
                'name': '同评分影片数量统计',  # 标题
                'categories': '=影片统计!$A$2:$A$9',
                'values': '=影片统计!$B$2:$B$9',
                'line': {'color': 'black', 'bold': True}
            }
        )
        worksheet1.insert_chart('D2', chart)
        worksheet1.insert_chart('D17', chart1)
        worksheet1.insert_chart('L17', chart2)
        worksheet1.insert_chart('L2', chart3)

        # 添加演员统计

    npActors = np.array(strActors)
    result2, iCount2 = np.unique(npActors, return_counts=True)
    d2 = {'actor': result2, 'count': iCount2}
    df1 = DataFrame(d2)
    res = df1.sort_values(by="count", ascending=False)

    worksheet2 = workbook.add_worksheet('演员统计')
    worksheet2.write(0, 0, '演员', cellF)
    worksheet2.write(0, 1, '主演影片数目', cellF)
    worksheet2.set_column('A:A', 10)
    worksheet2.set_column('B:B', 15)

    actorCount = [0] * 6
    for j, actor, count in zip(range(0, len(res)), res['actor'], res['count']):
        worksheet2.write(j + 1, 0, actor)
        worksheet2.write_number(j + 1, 1, count)
        actorCount[count-1] = actorCount[count-1]+1
        # 圆形图

    worksheet2.write(18, 3, '演员参演影片数目', cellF)
    worksheet2.write(18, 4, '统计人数', cellF)
    for j in range(19,25):
        worksheet2.write(j, 3, j-18)
        worksheet2.write_number(j, 4, actorCount[j-19])

    chart5 = workbook.add_chart({"type": "pie"})
    # 添加图表数据
    chart5.add_series(
        {
            'name': '参演电影数量统计',  # 标题
            'categories': '=演员统计!$D$20:$D$24',
            'values': '=演员统计!$E$20:$E$24',
            'line': {'color': 'black', 'bold': True}
        }
    )

    chart6 = workbook.add_chart({"type": "column"})
    # 添加图表数据
    chart6.add_series(
        {
            'name': '参演电影数量统计',  # 标题
            'categories': '=演员统计!$D$20:$D$25',
            'values': '=演员统计!$E$20:$E$25',
            'line': {'color': 'black', 'bold': True}
        }
    )
    worksheet2.insert_chart('M2', chart5)
    worksheet2.insert_chart('D2', chart6)

    workbook.close()
    pass

# 保存mysql数据
def saveMySql():
    conn = pymysql.connect(host = 'localhost', user = 'root', password = 'root', db = 'maoyan',port=8086)
    cursor = conn.cursor()
    for item in _lData:
        try:
            strSql = 'insert into maoyan(img, title, actor, date, score) values(%s, %s, %s, %s, %s)'
            cursor.execute(strSql, (item[7], item[1], item[3], item[4], str(item[5] + item[6])))
            conn.commit()
        except:
            conn.rollback()
            print('data1 error!')

    for item2 in _2Data:
        try:
            strSql2 = 'insert into comment(name,comment, prize) values(%s, %s, %s)'
            cursor.execute(strSql2, (item2[0], item2[1], item2[2]))
            conn.commit()

        except:
            conn.rollback()
            print('data2 error!')
    conn.close()
    pass

if __name__ == '__main__':
    i = 0
    for strPage in getPage():
        getPData(strPage)
        getDetails(i,strPage)
        if i is 9:
            break
        else:
            i = i+1
    # createXml()
    # createXlsx()
    # saveMySql()
    # print(_2Data)
    pass
