import threading

g_num = 0
lock = threading.Lock()

def task1(name):
    global g_num

    num = 0
    for i in range(1000000):
        lock.acquire()
        num += 1
        g_num += 1
        lock.release()
    print(name,num)
    print(name,g_num)

def task2(name):
    global g_num
    num = 0
    for i in range(1000000):
        lock.acquire()
        num += 1
        g_num += 1
        lock.release()
    print(name,num)
    print(name,g_num)

if __name__ == '__main__':
    t1 = threading.Thread(target=task1, kwargs={"name": "t1"})
    t2 = threading.Thread(target=task2, kwargs={"name": "t2"})

    t1.start()
    t2.start()

