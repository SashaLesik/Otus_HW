"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle

from homework_02 import exceptions



class Plane (Vehicle):
    def __init__(self, cargo, max_cargo, weight=1000, started=False, fuel=50,
                 fuel_consumption=100) -> None:
        
        self.cargo = cargo
        self.max_cargo = max_cargo
        super().__init__(weight, started, fuel, fuel_consumption)

    def load_cargo(self, cargo_weight):
        #  объявите метод load_cargo, который принимает число, проверяет, что в сумме с текущим cargo
        # не будет перегруза, и обновляет значение
        #  , в ином случае выкидывает исключение exceptions.CargoOverload
        if cargo_weight + self.cargo <= self.max_cargo:
            self.cargo = cargo_weight 
            return cargo_weight
        else:
            raise exceptions.CargoOverload
    
    def remove_all_cargo(self, cargo_weight=30):
        initial_cargo_weight = cargo_weight-self.cargo
        return initial_cargo_weight