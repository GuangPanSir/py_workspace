# coding=utf-8

i = 0

while i * i < 1000:
    i += 1

#str() 将其他类型转换为字符串
print("i = " + str(i))
print("i * i = " + str(i * i))

print("------------------------")

i = 0

while i * i < 10:
    i += 1
    if i == 3:
        break
    print(str(i) + ' * ' + str(i) + ' =' ,i * i)
else:
    print("While Over!")