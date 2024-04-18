"""
создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle

from . import exceptions


class Plane (Vehicle):
    def __init__(self,  max_cargo=100, cargo=30, weight=1000, started=False,
                 fuel=50, fuel_consumption=100) -> None:
        super().__init__(weight, started, fuel, fuel_consumption)

        self.max_cargo = max_cargo
        self.cargo = cargo

    def load_cargo(self, cargo_weight=10):
        #  объявите метод load_cargo, который принимает число, проверяет, что в сумме с текущим cargo
        # не будет перегруза, и обновляет значение
        #  , в ином случае выкидывает исключение exceptions.CargoOverload
        if cargo_weight + self.cargo <= self.max_cargo:
            self.cargo += cargo_weight
            return self.cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self, cargo_weight=10):
        null_cargo_weight = self.cargo - cargo_weight
        return self.cargo
