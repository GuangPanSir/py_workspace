f_name = r'E:\py_workspace\casual\file\test.txt'
f = None
try:
    f = open(f_name)
    content = f.read()
    print(content)

except FileNotFoundError as e:
    print("文件不存在")

except OSError as e:
    print("处理OSError")
finally:
    if f is not None:
        f.close()
