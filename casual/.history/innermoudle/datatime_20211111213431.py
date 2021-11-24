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
d = datetime.date.today()
delta = datetime.timedelta(10)
d += delta
print("今天是{0},十天后是：{1}".format(d1,))