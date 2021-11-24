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
def controlthread_body():
    global isrunning
    while isrunning:
        # 从键盘输入停止指令exit
        command = input('请输入指令')
        if command == 'exit':
            isrunning = False
            print("控制线程结束")

workthread = threading.Thread(target=workthread_body)

work