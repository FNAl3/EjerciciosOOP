##Vale para poder crear una clase abstracta hay que eportar la libreria abc
##ABC convierte una clase en abstracta
from abc import ABC, abstractmethod
#ABC es una clase del modulo abc
class Shape(ABC):
    #Y usar el @abstractmethod para indicar que la clase en este caso debe ser abstracto
    #@abstractmethod obliga a las subclases a implementar ese método.
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radio):
        self.radio=radio        
    def area(self):
        pi=3.15
        print(f"El area es del circulo {pi * self.radio**2}")
class Rectangle(Shape):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    def area(self):
        print(f"El area del rectangulo es {self.base * self.altura}")
fig1=Circle(10)
fig1.area()

fig2=Rectangle(10,50)
fig2.area()

#Hacemos una clase abstracta cuando queremos 
#que sirva solo como molde o ejemplo, no para usarla directamente.

#Hacemos una variable o función abstracta 
#cuando queremos obligar a las clases hijas a decir cómo será exactamente 
#esa parte.

