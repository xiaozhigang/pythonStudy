import multiprocessing
import time

g_list = list()

def add_data():
    for i in range(3):
        g_list.append(i)
        print("add:",i)
        time.sleep(0.2)

    print("添加完成",g_list)

def read_data():
    print("read:",g_list)

if __name__ == "__main__":
    multiprocessing.Process(target=add_data).start()
    time.sleep(2)
    multiprocessing.Process(target=read_data).start()
    print("主进程:",g_list)