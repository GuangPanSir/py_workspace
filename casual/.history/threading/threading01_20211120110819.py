import threading

t = threading.current_thread()
print(t.name)

print(threading.active_count())

t = 