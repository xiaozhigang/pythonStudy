


def func_out1():
    num = 10
    def func_in(num1):
        result = num * num1
        print(result)
    return func_in

def func_out2(name):

    def func_in(content):
        print(name + ": " +content)
    return func_in

def func_out3():
    num = 10
    def func_in():
        nonlocal num
        num = 20
        result = num * 2
        print(result)

    print("修改前：" ,num)
    func_in()
    print("修改后：" ,num)
    return func_in



if __name__ == '__main__':
    func1 = func_out1()
    func1(3)

    func2 = func_out2("菜鸡")
    func2("我是菜鸡")

    func3 = func_out3()
    func3()
