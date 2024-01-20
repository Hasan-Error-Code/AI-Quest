class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.wheel = 4

    def view(self):
        print(f"The model year of {self.name} is {self.model}.")
        print(f"It is a {self.wheel} wheel's car.")

c1 = Car("Audi", 2015)
c2 = Car("BMW", 2020)

print(c2.view())