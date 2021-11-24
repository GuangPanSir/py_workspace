print("-------list追加一个字符--------")
list = [20, 50, 10, 30]
# 追加字符串
list.append(80)
print("追加一个字符" + str(list))

print("\r\n-------list追加多个字符--------")
t = [1, 2, 3]
# 使用+=追加多个字符
list += t
print("使用+=追加多个字符 : " + str(list))

list = [20, 50, 10, 30]
# 使用extend追加多个字符
list.extend(t)
print("使用extend追加多个字符 : " + str(list))

print("\r\n-------list插入元素--------")
list = [20, 50, 10, 30]
# 在索引2的位置插入一个元素，新元素的索引为2
list.insert(2, 80)
print("插入[2, 80] : " + str(list))

print("\r\n-------list替换元素--------")
list = [20, 50, 10, 30]
list[1] = 80
print("list替换元素 : " + str(list))

print("\r\n-------list删除元素--------")
list = [20, 50, 80, 10, 30]
list.remove(80)
print("list删除元素 : " + str(list))
