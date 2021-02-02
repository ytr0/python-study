
def foo(arg):
    x = 10
    print(locals())
foo(20)

y = 30
print(globals())


#デコレータとは「関数を引数に取り, 引き換えに新たな関数を返すcallable(*)」
def logger(func):
    def inner(*args, **kwargs): #1
        print("Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs) #2
    return inner


@logger
def foo1(x, y=1):
    return x * y


foo1(5,4)


from functools import wraps
import time
def stop_watch(func) :
    @wraps(func)
    def wrapper(*args, **kargs) :
        start = time.time()
        result = func(*args,**kargs)
        elapsed_time =  time.time() - start
        print(f"{func.__name__}は{elapsed_time}秒かかりました")
        return result
    return wrapper


@stop_watch
def func() :
    j=0
    for i in range(9999) :
        j+=i
    print(j)

func()

import functools
def float_args_and_return(function):
    @functools.wraps(function)
    def wrapper(*args, **kargs):
        args = [float(arg) for arg in args]
        return function(*args, **kargs)
    return wrapper

# Decorateされる関数
@float_args_and_return
def mean(first, second, *rest):
    numbers = (first, second) + rest
    return sum(numbers) / len(numbers)

print(mean("0.1", 0.2, "0.3"))

#mean("0.1", 0.2, "0.3") は float_args_and_return(mean)("0.1", 0.2, "0.3")という意味になり、結果としてwrapper関数の中身を先に実現する