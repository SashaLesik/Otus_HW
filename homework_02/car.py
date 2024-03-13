"""
создайте класс `Car`, наследник `Vehicle`.
добавьте атрибут engine классу Car
объявите метод set_engine, который принимает
в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, engine, weight, started, fuel, fuel_consumption):
        self.engine = engine
        super().__init__(weight, started, fuel, fuel_consumption)
    
    def set_engine(self, engine: Engine):
        new_car_with_engine = self.engine
        return new_car_with_engine