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

# 长字符串    包含排版换行等信息，输出不改变原有样式
# 使用三个单引号或者双引号包围长字符即可
print("\r\n------打印排版字符串------")
s = '''
       《早发白帝城》
朝辞白帝彩云间，千里江陵一日还。
两岸猿声啼不住，轻舟已过万重山。
'''
print(s)

# 字符串与数字之间相互转换
print("\r\n------字符串数字相互转换------")
a = int("80")
print("字符串转整型: \"80\"==>" + str(a))
a = int("AB", 16)
print("字符串转16进制: \"AB\"==>" + str(a))
a = 123
print("a的原始类型: " + str(type(a)))
b = str(a)
print("a的转换类型: " + str(type(b)))

# 格式化字符串
# 要想将表达式的结果插入到字符串中，需要使用占位符{}
print("------使用占位符将结果插入字符串")
i = 32
s = 'i * i = ' + str(i * i)
print("正常打印：" + s)
print("格式化打印: {0} * {0} = {1}".format(i, i * i))
print("参数化打印")