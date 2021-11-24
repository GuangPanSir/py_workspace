f_name = r'E:\py_workspace\casual\file\test.txt'
f = None


def read():
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


def write_tail():
    try:
        f = open(f_name, 'a')
        f.write("\nthat is all")
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


# 在with as 中关闭文件
print("\r\n======在with as中关闭文件======")
with open(f_name) as f:
    content = f.read()
    print(content)

# 复制文件
copy_name = r"E:\py_workspace\casual\file\copy.txt"
print("\r\n======复制文件======")
with open(f_name, 'r') as f:
    lines = f.readlines()
    with open(copy_name, 'w') as copy_f:
        copy_f.writelines(lines)
        print("文件复制成功")

print("\r\n======复制照片======")
pic_name = r'E:\py_workspace\casual\static\images\grass.jpg'
pic_copy_name = r'E:\py_workspace\casual\static\images\copy_grass.jpg'
with open(pic)
