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
print("参数化打印: {p1} * {p1} = {p2}".format(p1=i, p2=i * i))


# 格式化控制符
"""
格式控制符  说明
s          字符串
d          十进制整数
f,F        十进制浮点数
g,G        十进制整数或浮点数
e,E        科学计数法表示浮点数
o          八进制整数，符号是小写英文字母o
x,X        十六进制整数，x是小写表示，X是大写表示      
"""

print("------格式化控制符------")
money = 5843.5678
name = 'tony'
print("{0:s}年龄{1:d},工资是{2:0.2f}".format(name, 20, money))
print("十进制{0:d}的八进制表示为{0:o}".format(18))
print("十进制{0:d}的十六进制表示为{0:x}".format(18))

# 字符串的操作
print("\r\n------查找字符串------")
s_str = "Hello World"
# 若查找字符存在且有多个，只返回第一个suoyin
# 若查找字符不存在，返回-1
print("查找字符e所在索引:" + str(s_str.find('e')))
print("区间查找字符l所在索引:" + str(s_str.find('l', 4, 6)))

print("\r\n------替换字符串------")
text = 'AB CD EF GH IJ'
text = text.replace(' ', '|', 2)
print("替换具体数量的字符: " + text)

print("\r\n------分割字符串------")
text = text.replace('|', ' ')
# maxsplit为最大分割次数
print("分割字符串: " + str(text.split(' ', maxsplit=2)))

# 统计单词出现的频数
wordstring = """
i love three things in the world.
sun
moon
and you.
sun for day
moon for night
and you forever.
"""

# 替换标点符号
wordstring = wordstring.replace('.', ' ')
# 以空格分割单词
wordlist = wordstring.split(' ')

wo