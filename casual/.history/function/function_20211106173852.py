def rect_area(width, height):
    area = width * height
    return area


def print_area(width, height):
    area = rect_area(width, height)
    print("{0} x {1} 长方形的面积：{2}".format(width, height, area))


print_area(320, 480)
