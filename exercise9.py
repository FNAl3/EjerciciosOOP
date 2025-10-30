class Vehicle:
    def __init__(self):
        pass
class Car(Vehicle): 
    def open_trunk(self):
        print(" el coche ha abierto el baúl")
class Motorbike(Vehicle):
    def do_wheelie(self):
        print(" La moto ha hecho un caballito")
coche1=Car()
coche1.open_trunk()

moto1=Motorbike()
moto1.do_wheelie()