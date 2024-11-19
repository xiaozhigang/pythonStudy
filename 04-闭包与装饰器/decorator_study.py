
def decorator(func):
    def wrapper(*args, **kwargs):
        print("装饰器")
        return func(*args, **kwargs)
    return wrapper


@decorator
def func(a,b):
    print(a+b)

func(1,2)

