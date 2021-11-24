import datetime

# 报错，超出最大范围值
# d = datetime.datetime(2020, 2, 30)
# print(d)

d = datetime.datetime.today()
print("今天时间:{}".format(d))

d = datetime.datetime.now()
print("现在时间:{}".format(d))

d = datetime.datetime.fromtimestamp(999999999.999)
print("时间戳转时间:{}".format(d))

# data类
# 超出范围，报错
# d = datetime.date(2020, 2, 30)
d = datetime.date(2020, 2, 16)
print("时间赋值:{}".format(d))

print("\r\n------计算时间跨度类------")
d1 = datetime.date.today()
delta = datetime.timedelta(10)
d2 = d1 + delta
print("今天是{0},十天后是：{1}".format(d1, d2))
delta = datetime.timedelta(weeks=5)
d2 = d1 - delta
print("今天是{0},五周前是：{1}".format(d1, d2))

print("\r\n------日期时间与字符串相互转换------")
d = datetime.datetime.today()
# 时间转字符串
str = d.strftime('%Y-%m-%d %H:%M:%S')
print(str)

date = datetime.datetime.strptime(str,
)