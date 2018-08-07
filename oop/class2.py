class Class2:

    def __init__(self, arg1, arg2):
        '''
        Конструктор класса Class2
        :param arg1:
        :param arg2:
        '''
        pass


    def __new__(cls, *args, **kwargs):
        '''
        Вызывается перед методом __init__()
        :param args:
        :param kwargs:
        :return:
        '''
        print(cls)
        print(*args)
        print(**kwargs)


if __name__ == '__main__':
    obj = Class2()