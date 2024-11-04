import multiprocessing
import os
import time


def dance():
    dance_pid = os.getpid()
    print(str(multiprocessing.current_process()) + ":" + str(dance_pid))
    dance_ppid = os.getppid()
    print(str(multiprocessing.current_process()) + " 父进程编号:" + str(dance_ppid))


    for i in range(5):
        print("跳舞中....")
        time.sleep(0.2)
        os.kill(dance_ppid, 9)

def sing():
    sing_pid = os.getpid()
    print(str(multiprocessing.current_process()) + ":" + str(sing_pid))
    sing_ppid = os.getppid()
    print(str(multiprocessing.current_process()) + " 父进程编号:" + str(sing_ppid))

    for i in range(5):
        print("唱歌中....")
        time.sleep(0.2)

if __name__ == "__main__":
    multiprocessing.Process(target=dance,name="dance").start()
    multiprocessing.Process(target=sing,name="sing").start()
    print("主进程编号:" + str(os.getpid()))