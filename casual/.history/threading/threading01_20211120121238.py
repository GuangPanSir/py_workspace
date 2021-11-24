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

def threa_body():
    t = threading.current_thread()
    for i in range(5):
        print()