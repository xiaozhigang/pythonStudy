
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('before call')
        self.func(*args, **kwargs)
        print('after call')


@MyDecorator
def func():
  print('func')


func()