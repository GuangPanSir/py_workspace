import pymysql
def insert(row):
    try:
        db = pymysql.connect("localhost", "root", "root", "jiaoyu", 8086)
        cursor = db.cursor()
        # print('连接成功')
    except:
        print("数据库连接失败")

    sql = """insert into xuexiao(bianhao,xiaoming,max,min,ave) values ('{}','{}',{},{},{})"""
    # print('插入成功')
    sql = sql.format(str(row[0]),str(row[1]),float(row[2]),float(row[3]),float(row[4]))
    # print(sql)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print('数据库操作有误')
    # db.close()