# 等待线程结束才开始执行另外一个线程
import threading
import time

# 共享变量
value = []


# 线程体函数
def thread_body():
    print("t1子线程开始")
    for n in range(2):
        print("t1子线程执行")
        value.append(n)

        time.sleep(2)

    print("t1子线程结束")


# 主线程开始
