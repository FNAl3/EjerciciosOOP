import datetime
class Pearson:
    def __init__(self, name, age):
        if name !=" ":
            self.__name=name
        else:
            raise ValueError("EL campo nombre esta vacio")
        if age < 0:
            raise ValueError("La edad no puede ser negativa")
        else:
            self.__age=age
    def set_name(self, new_name):
        if new_name !=" ":
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
    @classmethod
    def from_birth_year(cls,name,birth_year):
        persona1=Pearson("Ager",20)
        nowyear=datetime
    def is_adult(self):
        pass
    