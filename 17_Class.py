class SpeedValueError(ValueError):
    def __init__(self, lineNo, *args: object) -> None:
        super().__init__(*args)
        self.__lineno__ = lineNo

    def __str__(self) -> str:
        return super().__str__() + f" -- {self.__lineno__}"
    
    def __repr__(self) -> str:
        return super().__repr__() + f" -- {self.__lineno__}"

class Car:
    count = 0
    def __init__(self, make, model, color, year) -> None:
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.__speed = 0
        self.serial = Car.genSerial()
        Car.count += 1

    def __str__(self):
        return f"Car [{self.count}] is {self.make}, {self.model}, {self.color}, {self.year}"
    
    @classmethod
    def GetCarCount(cls):
        return cls.count
    
    @property
    def Make(self):
        return self.make

    @Make.setter
    def Make(self, value):
        self.make = value

    @property
    def Speed(self):
        return self.__speed
    
    @Speed.setter
    def Speed(self, val):
        value = int(val)
        if value >= 0 and value < 250:
            self.__speed = value
        else:
            # raise ValueError("Speed out of range.")
            raise SpeedValueError(__file__,  "Speed out of range.")

    @staticmethod
    def genSerial():
        from random import randint
        return randint(1, 10000)

    def __del__(self):
        print(f"Performing cleanup for [{self.__str__()}]")
        Car.count -= 1

###############################################################################

class GearedCar(Car):
    def __init__(self, make, model, color, year, gears) -> None:
        super().__init__(make, model, color, year)
        self.gears = gears

    def __str__(self):
        return super().__str__() + f", {self.gears} gears"

###############################################################################

def Test1():
    print("Car count -->", Car.GetCarCount())
    c1 = Car("Honda", "Accord", "Black", 2024)
    c2 = Car("Hyundai", "Accent", "Blue", 2023)

    print(c1.make, c1.model, c1.color, c1.year)
    print(c1) # print(str(c1)) --> print(c1.__str__()) --> print(c1.__repr())
    print(c1.__str__())
    print(c1.__repr__())

    c1._Car__speed = 50     # Name mangled to suggest using the interface instead of the data directly.
    print(c1.Speed)

    print(c1.__dict__)

    # c2.Speed = 100
    # print(c2.Speed)
    # print(c2._speed)
    # c2._speed = 150
    # print(c2.Speed)

    # c2.SetMake("Modified")
    # print(c2.GetMake())

    c2.Make = "Modified"
    print(c2.Make)

def Test2():
    gc1 = GearedCar("Honda", "Accord", "Black", 2024, 6)
    gc2 = GearedCar("Hyundai", "Accent", "Blue", 2023, 7)

    print(gc1)

    # Explore more to understand the 'super()' mechanism
    # print(gc1.__class__.__mro__)
    # print(gc1.__class__.__bases__)
    # print(GearedCar.__bases__)

    try:
        gc2.Speed = "Fast"
    except ValueError as ex:
        print(f"{ex!r}")

    try:
        gc2.Speed = 2000
    except (TypeError, ValueError, SpeedValueError) as ex:
        print(f"Check the input --> {ex!r}")
        print("[Re-raising the same exception]")
        raise
    except IndexError as ex:
        print(f"Check the no. of items present --> {ex!r}")
    except Exception as ex:
        print(f"Unknown exception occurred --> {ex!r}")
        raise

    print("Resuming normal execution...")
    print(gc2.Speed)

if __name__ == "__main__":
    print("Starting off...")
    try:
        Test2()
    except ValueError as ex:
        print(f"-->{ex}")
        print(f"-->{ex!s}") # print(f"-->{str(ex)}")  --> print(f"-->{ex.__str__()}")
        # O/P: -->Speed out of range.

        print(f"-->{ex!r}") # print(f"-->{repr(ex)}")  --> print(f"-->{ex.__repr__()}")
        # O/P: -->ValueError('Speed out of range.')

    print("Wrapping up!")