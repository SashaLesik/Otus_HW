from abc import ABC

from . import exceptions


class Vehicle(ABC):
    
    def __init__(self, weight=100, started=False, fuel=100,
                 fuel_consumption=10) -> None:
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    
    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True

            else:
                raise exceptions.LowFuelError
            

    def move(self, distance=100):
        if self.fuel == 0:
            raise exceptions.NotEnoughFuel

        elif self.fuel_consumption <= distance/self.fuel:
            fuel_left = self.fuel - (distance/self.fuel)
            return fuel_left
        else:
            raise exceptions.NotEnoughFuel
