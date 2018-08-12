class Parent:
    def __init__(self, *args):
        self._subconstructor()
        print('parent')

    def _subconstructor(self):
        print('sub_parent')


class Child1(Parent):
    def _subconstructor(self):
        print('sub_child1')


class Child2(Parent):
    def _subconstructor(self):
        super()._subconstructor()
        print('sub_child2')


class Child3(Parent):
    def __init__(self):
        self._subconstructor()
        print('child3')


parent = Parent()
print('-----------------')
child1 = Child1()
print('-----------------')
child2 = Child2()
print('--------------------')
child3 = Child3()