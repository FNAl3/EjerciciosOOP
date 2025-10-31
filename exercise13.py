
#Importo el modulo math que usaremos para realizar ecuaciones matematicas de manera más precisa
#Parece que lo he hecho con ChatGpt pero no he.
import math
##Creo la clase Temeprature
class Temperature:
    def __init__(self, celsius):
        if  -273.15 <= celsius <=1000:
            self.__celsius=celsius
        else:
            ##Pista del Copilot si dice que hay que controlar los rangos en el setter hay que hacerlo 
            #tambien al crear el objeto esto de aqui sirve para parar la ejecucion del objeto si no se cumple
            raise ValueError ("The Values are not in the range")
    def set_celsius(self, new_celsius):
        if  -273.15 <= new_celsius <=1000:
            self.__celsius=new_celsius
        else:
            ##Lo mismo que en el constructor
            raise ValueError ("The Values are not in the range")
    def get_celsius (self):
        return self.__celsius
    def freeze(self):
        if self.__celsius <= 0:
           ##Para que cumpla con los requisitos solo tiene que devolver true o false pero el mensaje es de gratis
           print("The temperature is below 0ºC" )
           return True
        return False
    def boil(self):
        if self.__celsius >=100:
            ##Para que cumpla con los requisitos solo tiene que devolver true o false pero el mensaje es de gratis
            print("The temperartue is above 100ºC")
            return True
        return False
    def to_fahrenheit(self):
        ##Sumamos y redondeamos
        ##math.floor para reondear
        #math.sum para sumar ([numero a sumar,numero a sumar])
        return math.floor(math.fsum([self.__celsius *9/5,32]))
##Creo el eobjeto
termo1=Temperature(-25)
print(f" the temperatue is {termo1.get_celsius()}ºC")
##Cambiamos la temp
termo1.set_celsius(100)
print(f" The temperature changed to {termo1.get_celsius()}ºC")
termo1.freeze()
termo1.boil()
##Tenmperatura de cel a far
print(f" The temperature in fahrenheit is {termo1.to_fahrenheit()}")
