import multiprocessing
import time


def task():
    while True:
        print("任务执行中...")
        time.sleep(0.2)


if __name__ == '__main__':
    process = multiprocessing.Process(target=task)
    process.daemon = True
    process.start()
    time.sleep(2)
    print("主进程结束")

    # process = multiprocessing.Process(target=task)
    # process.start()
    # time.sleep(2)
    # process.terminate()
    # print("主进程结束")



