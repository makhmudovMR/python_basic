class Human:


    var = "this is war"


    def __init__(self, name, year, height, weight):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight

    def talk(self, word):
        return f"Hello my name is {self.name}"


class Programmer(Human):

    def __init__(self, name, year, height, weight, vector):
        super().__init__(name, year, height, weight)
        self.vector = vector



p = Programmer("magomed", 20, 188, 60, 'web/ai')
