i = input("请输入数字")
n = 8888
try:
    result = n / int(i)
except:
    print
print(result)
print("{0}除以{1}等于{2}".format(n, i, result))
