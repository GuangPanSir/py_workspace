import threading
import time

t = threading.current_thread()
# 当前线程名
print(t.name)

# 活跃的线程数
print(threading.active_count())

t = threading.main_thread()
# 主线程名
print(t.name)

# 线程体函数
def threa_body():
    t = threading.current_thread()
    for i in range(5):
        print("第{0}次执行线程{1}".format(n,t.name))

        time.sleep(2)

    print("线程{0}执行完毕".format(t.name))

t1 = threading.Thread(target=th)