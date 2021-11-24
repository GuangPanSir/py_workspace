import sqlite3

try:
    con = sqlite3.connect('test.db')
    cursor = con.cursor()
    sql = 'select * from user'
    cursor.execute()
    result_set = cursor.fetchall()
    
