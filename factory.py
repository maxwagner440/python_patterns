class Car:
    
    def __init__(self, color):
        self._color = color

    def rev_engine(self):
        return "Vroom!"


class Plane:
    
    def __init__(self, color):
        self._color = color

    def rev_engine(self):
        return "Shrrooooohhhh!"


def get_vehicle(vehicle="car"):
    """ 
    The factory method to create Car 

    Logic can persist in method to create objects
    """

    vehicles = dict(car=Car("blue"), plane=Plane("green"))

    return vehicles[vehicle]

car = get_vehicle("car")
plane = get_vehicle("plane")

print(plane.rev_engine())
print(car.rev_engine())
