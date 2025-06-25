class Car():
    def __init__(self,type):
        self.type = type


class SwedishCar(Car):
    def __init__(self,type,country="Sweden"):
        super().__init__(type)
        self.country = country

    def mycar(self):
        return f"This car is {self.type} and made in {self.country}"


x = SwedishCar("Black")
print(x.mycar())




