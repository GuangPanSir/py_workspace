# 等待线程结束才开始执行另外一个线程
import threading
import time

# 共享变量
value = []

# 线程体函数
def thread_body():
    print("t1子线程那个开始")