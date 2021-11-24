f_name = 'test.txt'
f = None
try:
    f = open(f_name)
    print("文件打开成功")
    content = f.read()
    print(content)
except FileNotFoundError as e:
    print("文件不存在")
f.close()
