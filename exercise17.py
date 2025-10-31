import time
##Creo la clase VEhicle
class vehicle:
    def __init__(self,fuel_level):
        if fuel_level > 0:
            self.__fuel_level=fuel_level
        raise ValueError ("El valor de fuel_level no puede ser negativo")
    def move(self):
        pass
class Car(vehicle):
    def move(self):
        super().move(self)
        

    def set_fuel_level(self,new_fuel_level):
        if new_fuel_level > 0:
            self.__fuel_level=new_fuel_level
        raise ValueError ("El valor de fuel_level no puede ser negativo")
    def get_fuel_level(self):
        return self.__fuel_level
    