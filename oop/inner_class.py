class Human:

    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()

    class Head:

        def talk(self):
            return 'talking...'

if __name__ == '__main__':
    human = Human()
    print(human.name)
    print(human.head)
    print(human.head.talk())