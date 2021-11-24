#coding=utf-8

print("------字符串------")
for item in "Hello":
    print(item)

#声明整数列表
numbers = [43,32,55,74]
print("------整数列表------")
for item in numbers:
    print(item)

print("------range循环（break）---------")
# range(10) 0 ~ 10 （包括0不包括10）
for item in range(10):
    if item == 3:
        break
    print(item)
else:
    print("For Over")

print("------range循环(continue)---------")
# range(10) 0 ~ 10 （包括0不包括10）
for item in range(10):
    if item == 3:
        continue
    print(item)
else:
    print("For Over")

print("------计算水仙花数------")
#计算水仙花数
i = 100
r = 0
s = 0
t = 0

while i < 1000:
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i == (r ** 3 + s ** 3 + t ** 3):
        print("i= " + str(i))

    i += 1 