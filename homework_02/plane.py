"""
создайте класс `Plane`, наследник `Vehicle`
"""
from .base import Vehicle

from homework_02 import exceptions



class Plane (Vehicle):
    def __init__(self, cargo, max_cargo, weight, started, fuel,
                 fuel_consumption) -> None:
        
        self.cargo = cargo
        self.max_cargo = max_cargo
        super().__init__(weight, started, fuel, fuel_consumption)

    def load_cargo(self, cargo_weight):
        if self.weight + self.max_cargo <= cargo_weight:
            cargo_weight = self.weight + cargo_weight
            return cargo_weight
        else:
            raise exceptions.CargoOverload
    
    def  remove_all_cargo(self, cargo_weight):
        initial_cargo_weight = cargo_weight-self.weight
        return initial_cargo_weight