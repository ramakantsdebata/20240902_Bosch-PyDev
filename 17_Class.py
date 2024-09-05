class Car:
    count = 0
    def __init__(self, make, model, color, year) -> None:
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.serial = Car.genSerial()
        Car.count += 1

    def __str__(self):
        return f"Car is {self.make}, {self.model}, {self.color}, {self.year}  out of '{Car.count}' cars."
    
    @classmethod
    def GetCarCount(cls):
        return cls.count
    
    @property
    def Make(self):
        return self.make

    @Make.setter
    def Make(self, value):
        self.make = value

    @staticmethod
    def genSerial():
        from random import randint
        return randint(1, 10000)


print("Car count -->", Car.GetCarCount())
c1 = Car("Honda", "Accord", "Black", 2024)
c2 = Car("Hyundai", "Accent", "Blue", 2023)

print(c1.make, c1.model, c1.color, c1.year)
print(c1) # print(str(c1)) --> print(c1.__str__()) --> print(c1.__repr())
print(c1.__str__())
print(c1.__repr__())

# c2.SetMake("Modified")
# print(c2.GetMake())

c2.Make = "Modified"
print(c2.Make)
