import threading
import time

isrunning = True

# 工作线程函数体
def workthread_body():
    while isrunning:   
        # 线程开始工作
        print("工作线程进行中")
        time.sleep(2)

    print("线程结束")

# 控制线程体函数
