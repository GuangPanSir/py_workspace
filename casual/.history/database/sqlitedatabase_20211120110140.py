import sqlite3

try:
    con = sqlite3.connect('test.db')
    cursor = con.cursor()
    sql = 'select * from user'
    cursor.execute()
    result_set = cursor.fetchall()
    for row in result_set:
        print('学号:{0} - 姓名:{1}'.format(row[0],row[1]))
    
except sqlite3.Error as e:
    print("数据查询发生错误:{}".format())
