print("-------list追加一个字符--------")
list = [20, 50, 10, 30]
# 追加字符串
list.append(80)
print("追加一个字符" + str(list))

print("-------list追加多个字符--------")
t = [1, 2, 3]
# 使用+=追加多个字符
list += t
print("使用+=追加多个字符 : " + str(list))

list = [20, 50, 10, 30]
# 使用extend追加多个字符
list.extend(t)
print("使用extend追加多个字符 : " + str(list))

print("-------list插入元素--------")
list = [20, 50, 10, 30]
p