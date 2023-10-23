class Human:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self, name):
        self.name = name
        self.ps = []

    def add_ps(self, *humans):
        for human in humans:
            self.ps.append(human)

    def print_ps(self):
        if self.ps:
            print(f"Names of passengers in {self.name}:")
            for i in self.ps:
                print(i.name)
        else:
            print(f"There aren't any passengers in {self.name}")


hh1 = input("What is the first passenger's name? - ")
hh2 = input("What is the second passenger's name? - ")

h1 = Human(hh1)
h2 = Human(hh2)

cc = input("What is the car name? - ")

car = Car(cc)
car.add_ps(h1, h2)

car.print_ps()