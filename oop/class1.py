class class1(object):

    def __init__(self, constructor_arg1, constructor_arg2):
        self.arg1 = constructor_arg1
        self.arg2 = constructor_arg2
        self.iterable = 0

    def __str__(self):
        if not isinstance(self.arg1, str.__class__) and not isinstance(self.arg2, str.__class__):
            arg1 = str(self.arg1)
            arg2 = str(self.arg2)
        return arg1 + ' ' + arg2 + ' ' + str(self.iterable)

    def returnobj(self):
        self.iterable += 1
        return self



if __name__ == '__main__':
    obj = class1('arg1', 'arg2')
    print(obj)
    print(obj.returnobj())
    print(obj.returnobj())
    print(obj.returnobj())
    print(obj.returnobj())
    print(obj.returnobj())
    print(obj.returnobj())
    print(obj.returnobj())