import datetime

# 报错，超出最大范围值
# d = datetime.datetime(2020, 2, 30)
# print(d)

d = datetime.datetime.today()
print(d)

d = datetime.datetime.now()
print(d)

d = datetime.datetime.fromtimestamp(999999999.999)
print("时间戳转时间"d)
