# map函数对映射表中所有数据进行操作
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f(x):
    return x * 2


*mapped = map(f, data)
mapped = map(f, data)
list = list(mapped)
print(list)
