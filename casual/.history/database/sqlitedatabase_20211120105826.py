import sqlite3

try:
    con = sqlite3.connect('test.db')
    cursor = con.cursor()
    
