class vehicle:
    def __init__(self,fuel_level):
        self.__fuel_level=fuel_level
    def move(self):
        pass
class Car(vehicle):
    def move(self):
        return super().move()