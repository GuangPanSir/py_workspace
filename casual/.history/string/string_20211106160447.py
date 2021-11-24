print("------Unicode编码------")
s = '\u0048\u0065\u006c\u006c\u006f'
print(s)

'''
常用转义字符
字符表示    Unicode编码    说明
\t         \u0009         水平制表符
\n         \u000a         换行
\r         \u000d         回车
\"         \u0022         双引号
\'         \u0027         单引号
\\         \u005c         反斜线
'''

# 原始字符串，不需要转义    使用r来表明原始字符串
print("\r\n------打印原始字符串------")
s = r"Hello \r\n World"
print(s)

#长字符串    包含排版换行等信息，输出不改变原有样式
print("\r\n------打印排版字符串------")