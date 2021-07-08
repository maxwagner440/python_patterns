class Car:
    
    def __init__(self, color):
        self._color = color

    def __str__(self):
        return "Car"

    def rev_engine(self):
        return "Vroom!"


class Plane:
    
    def __init__(self, color):
        self._color = color
    
    def __str__(self):
        return "Plane"

    def rev_engine(self):
        return "Shrrooooohhhh!"


class CarFactory:
    """ 
    Concreate Factory
    """

    def get_vehicle(self, color):
        return Car(color)

    def get_fuel(self):
        return "Car Fuel"

class VehicleStore:
    """
    Abstract Factory
    """
    def __init__(self, vehicle_factory=None):
        self._vehicle_factory = vehicle_factory

    def show_vehicle(self):

        vehicle = self._vehicle_factory.get_vehicle("blue")
        fuel = self._vehicle_factory.get_fuel()

        print("Vehicle is: '{}'".format(vehicle))
        print("Vehicle engine sounds like: '{}'".format(vehicle.rev_engine()))
        print("Vehicle fuel: '{}'".format(fuel))


car_factory = CarFactory()

store = VehicleStore(car_factory)

store.show_vehicle()
