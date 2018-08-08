class Foo:

    def __init__(self):
        self.x = 'str'

    def func(self):
        return 'some data'



if __name__ == '__main__':

    hell = Foo

    obj = hell()
    print(obj.func())
    print(type(Foo))
    print(Foo.__class__)