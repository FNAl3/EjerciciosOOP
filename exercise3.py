#Creo la clase

class dog:
    #Metodo Bob (el constructor) para iniciar las variables
    #que conponen el objeto
    def __init__(self, name, age):
        self.name=name
        self.age=age
    #Metodo que en este caso hace ladrar al bobi
    def speak(self, bark):
        print(f"{self.name} dice {bark}")
#construyo los objetos.
nombre=dog("bobi",1)
#boby dice woof y si se crea otro perro podria ladrar diferente
nombre.speak("Woof")