import threading
import time

def task1():
    print("Task 1 started")
    time.sleep(2)  # 模拟耗时操作
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(1)  # 模拟耗时操作
    print("Task 2 completed")

# 创建线程对象
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# 启动线程
thread1.start()
thread2.start()

# 等待线程结束
thread1.join()
thread2.join()

print("All tasks completed")
