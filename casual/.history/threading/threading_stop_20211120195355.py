import threading
import time

isrunning = True

# 工作线程函数体
def workthread_body():
    while isrunning:   
        # 线程开始工作
        print(object(s), separator=separator, end=end, file=file, flush=flush)