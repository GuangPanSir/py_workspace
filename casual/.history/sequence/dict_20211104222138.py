# {key1: value1, key2: value2}

# 字典的相关操作
print("------字典的相关操作----------")
dict1 = {102: '张三', 105: '李四', 109: '王五'}
# 如果字典中存在此键值，则修改对应的值
# 若不存在，则在字典中加入此键值对
dict1[110] = '董六'
print("字典中不存在，加入键值对 : " + str(dict1))
print("字典中存在，修改键值对 : " + str(dict1))
