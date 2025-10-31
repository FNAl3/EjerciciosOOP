import random
class Flyable:
    def __init__(self):
        self.__speed=random.randint(1,100)
    def set_speed(self, new_speed):
        if new_speed <= 0:
            raise ValueError ("La velocidad es negativa")
        self.__speed=new_speed
    def get_speed(self):
        return self.__speed
class Swimmable:
    def __init__(self):
        self.__speed=random.randint(1,100)
    def set_speed(self, new_speed):
        if new_speed <= 0:
            raise ValueError ("La velocidad es negativa")
        self.__speed=new_speed
    def get_speed(self):
        return self.__speed
class Duck(Flyable,Swimmable): 
    def __init__(self):
        Flyable.__init__(self)
        Swimmable.__init__(self)
    def race(self,duck2):
        velocidad_pato1_volando=Flyable.get_speed(self)
        velocidad_pato2_volando=Flyable.get_speed(duck2)
        if velocidad_pato1_volando>velocidad_pato2_volando:
            print("El pato1 va más rapido que el pato dos volando")
        else:
            print("el pato2 va más rapido que el pato uno volando")
        ##velocidad nadando
        velocidad_pato1_nado=Swimmable.get_speed(self)
        velocidad_pato2_nado=Swimmable.get_speed(duck2)
        if velocidad_pato1_nado>velocidad_pato2_nado:
            print("El pato1 va más rapido que el pato dos nadando ")
        else:
            print("el pato2 va más rapido que el pato uno bnadando")
##creo dos patos
pato1=Duck()
pato2=Duck()
pato1.race(pato2)
