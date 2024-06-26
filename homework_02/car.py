
from base import Vehicle
from engine import Engine

"""
создайте класс `Car`, наследник `Vehicle`.
добавьте атрибут engine классу Car
объявите метод set_engine, который принимает
в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car
"""



class Car(Vehicle):
    def __init__(self, engine, weight=500, started=False, fuel=100,
                 fuel_consumption=20):
        self.engine = engine
        super().__init__(weight, started, fuel, fuel_consumption)

    def set_engine(self, engine: Engine):
        new_car_with_engine = self.engine
        return new_car_with_engine
