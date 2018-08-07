class Human:

    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()

    class Head:

        def __init__(self):
            self.brain = self.Brain()

        def talk(self):
            return 'talking...'

        class Brain:
            def think(self):
                return 'thinking...'


if __name__ == '__main__':
    human = Human()
    print(human.name)
    print(human.head)
    print(human.head.talk())
    print(human.head.brain)
    print(human.head.brain.think())
