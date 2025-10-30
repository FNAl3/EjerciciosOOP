## El anulamiento de metodos es crear en cada una de las subclases 
#el mismo metodo que hay en el principal y sobreescribir con el
# contenido que tenga cada una de las clases es decir ejemplo 
# el animal hace un ruido pero no todos los animales hacen el mismo 
class Animal:
    def speak(self):
        print("sonido del bicho")
class Dog(Animal):
    def speak(self):
        print("El perro dice Guau")
class Cat(Animal):
    def speak(self):
        print("El gato dice Miau")
#Creacion de perro
dog1=Dog()
dog1.speak()
#creacion de Gato
cat1=Cat()
cat1.speak()