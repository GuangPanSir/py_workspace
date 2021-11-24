# filter函数起过滤筛选作用
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f(x):
    return x > 6

filtered = filter(f, data)
filtered = filter(lambda a: a > 6, data)
list = list(filtered)
print(list)
