import datetime

# 报错，超出最大范围值
# d = datetime.datetime(2020, 2, 30)
# print(d)

d = datetime.datetime.today()
print(d)

d = datetime.datetime.now()
print(d)

d = datetime.datetime(999999999.999)
print(d)