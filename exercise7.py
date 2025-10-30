#definimos funcion que se usara para hacer hablar a los diferentes animales (que tengan funcion speak)
def animal_sound(animal):
        animal.speak()
class Perro():
    def speak(self):
        print("Guau")
class Humano():
    def speak(self):
        print("Hola")
#La idea seria llamar en este caso a una funcion definida para algo concreto pero desde diferentes lugares
animal_sound(Perro())
animal_sound(Humano())