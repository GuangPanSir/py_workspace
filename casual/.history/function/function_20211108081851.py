def rect_area(width, height):
    area = width * height
    return area

# 带默认参数的函数


def print_area(width=120, height=120):
    area = rect_area(width, height)
    print("{0} x {1} 长方形的面积：{2}".format(width, height, area))


print_area()
print_area(320, 480)

# 基于元组的可变参数


def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print("可变参数求和："+str(sum(10, 20, 30, 40, 50, 60)))

print("\r\n------基于字典的可变参数------")


def show_info(**info):
    print("---show info---")
    for key, value in info.items():
        print("{0:4s} - {1}".format(key, value))


show_info(name='Tony', age=18, set=True)


def show_info(*info):
    print("---show info---")
    for item in in
    for key, value in info.items():
        print("{0:4s} - {1}".format(key, value))


stu_info=[
    {
        name:'Tony',
        age:18,
        set:True
    },
    {
        name:'Hello', 
        age:20, 
        set:False
    }
]

show_info(stu_info)
