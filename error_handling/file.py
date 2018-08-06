def f1():
    try:
        print(10 / 0)

    except ZeroDivisionError:
        print('except')


def f2():
    try:
        print(2 + '1')
    except TypeError as e: # except ClassName as object:
        print(e.__doc__)   # use object


def f3():
    try:
        x = int('qwerty')
        print(x)
    except: # all ErrorClass
        print('work')
        print(f3.__class__)


def f4():
    try:
        print(100 / 0) # some error
        print('this is will not to display')
    except BaseException as e:
        print('we are here')
        print(type(e))


f4()