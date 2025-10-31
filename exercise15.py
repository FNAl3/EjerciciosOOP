import datetime
class Person:
    def __init__(self, name, age):
        #comprobamos si el contenido de nombre esta vacio
        if name !="":
            self.__name=name
        else:
            raise ValueError("EL campo nombre esta vacio")
        #comprobamos si el contenido de esdad esta vacio
        if age < 0:
            raise ValueError("La edad no puede ser negativa")
        else:
            self.__age=age
    def set_name(self, new_name):
        #comprobamos si el contenido de nombre esta vacio
        if new_name !="":
            self.__name=new_name
        else:
            raise ValueError("EL campo nombre esta vacio")
    def get_name(self):
        return self.__name
    def set_age(self, new_age):
        if new_age < 0:
            raise ValueError("La edad no puede ser negativa")
        else:
            self.__age=new_age
    def get_age(self):
        return self.__age
    @classmethod
    def from_birth_year(cls,name,birth_year):
        año_act=datetime.datetime.now().year
        age=año_act-birth_year
        return cls(name,age)
    def is_adult(self):
        if self.__age>=18:
            return True
        return False
persona1=Person("hola",10)
print(persona1.get_name())
print(persona1.get_age())
persona1.set_name("jaime")
print(persona1.get_name())

persona2=Person.from_birth_year("Sara",2020)
print(persona2.get_age())