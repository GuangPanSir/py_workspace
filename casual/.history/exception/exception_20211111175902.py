# 自定义异常类

class MyException(Exception):
    def __init__(self, message):
        super.__init__(message)


i = input("请输入数字: ")
n = 8888
try:
    result = n / int(i)
    print(result)
    print("{0}除以{1}等于{2}".format(n, i, result))
# except ZeroDivisionError as e:
#     print("不能除以0,异常{}".format(e))
# except ValueError as e:
#     print("输入的是无效数字,异常{}".format(e))
# 多重异常捕获
except (ZeroDivisionError, ValueError) as e:
    print("异常发生：{}".format(e))
finally:
    print("释放资源......")

print("\r\n------try-except语句嵌套------")
# try-except语句嵌套
try:
    i2 = int(i)
    try:
        result = n / i2
        print("{0}除以{1}等于{2}".format(n, i2, result))
    except ZeroDivisionError as e:
        #print("不能除以0,异常{}".format(e))
        raise 
except ValueError as e:
    print("输入的是无效数字,异常{}".format(e))
finally:
    print("释放资源......")
