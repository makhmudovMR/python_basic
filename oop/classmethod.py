class Foo:

    def __init__(self):
        pass


    @classmethod
    def method(cls):
        return cls

    def display():
        print("This is print")


o = Foo
o2 = o.method()
o2.display()