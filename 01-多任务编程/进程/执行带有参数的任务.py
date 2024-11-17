import multiprocessing


def show_info(name, age):
    print(f"姓名：{name}, 年龄：{age}")

if __name__ == '__main__':
    multiprocessing.Process(target=show_info, args=("张三", 18)).start()
    multiprocessing.Process(target=show_info, kwargs={"age":20, "name" : "李四"}).start()
    multiprocessing.Process(target=show_info, args=("王五",), kwargs={"age": 25}).start()
    