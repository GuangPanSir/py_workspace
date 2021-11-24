import pymysql
# import jupyter
for i in range(1, 10, 1):
    for j in range(1, i+1, 1):
        print(j, "*", i, "=", i*j)
    print()
a = "Hello"
a += "Word"

try:
    db = pymysql.connect("localhost", "root", "root", "student", 8086)
    cursor = db.cursor()
except:
    print("数据库连接失败")

sql = "select * from cjb"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        XH = row[0]
        KCH = row[1]
        CJ = row[2]
        print("学号：%s  课程号：%s  成绩：%s" % (XH, KCH, CJ))
except:
    print("出现异常了")
finally:
    print("我是finally块")
