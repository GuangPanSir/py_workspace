# set集合是一种可迭代的，无序的，不能包含重复元素的容器类型的数据结构

# 集合的相关操作
print("------集合插入元素---------")
s_set = {'张三', '李四', '王五'}
s_set.add('董六')
print("set集合插入元素 : " + str(s_set))

print("------集合删除元素---------")
s_set.remove('李四')
print("set集合删除元素 : " + str(s_set))
