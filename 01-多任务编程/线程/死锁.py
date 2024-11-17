import threading

lock = threading.Lock()

def get_value(index):
    lock.acquire()
    my_list = [1,2,3]
    if index>=len(my_list):
        print("下标越界")
        lock.release()
        return
    value = my_list[index]
    print(value)
    lock.release()

if __name__ == '__main__':
    for i in range(10):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()