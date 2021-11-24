f_name = 'test.txt'
f = None
try:
    f = open(f_name, 'r+', encoding='utf8')
    f.seek(0)
    print("文件打开成功")
    content = f.read()
    print(type(content))
    print(len(content))

except FileNotFoundError as e:
    print("文件不存在")

except OSError as e:
    print("处理OSError")
finally:
    if f is not None:
        f.close()
        print("文件关闭成功")
