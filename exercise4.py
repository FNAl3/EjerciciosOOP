#Creo la clase
class Dog:
    #Metodo Bob (el constructor) para iniciar las variables
    #que conponen el objeto
    def __init__(self, name, age):
        self.name=name
        self.age=age
    #Metodo para poner en texto plano el contenido de las vareiables (creo preguntar) 
    def __str__(self):
        return f"{self.name} tiene {self.age} años"
#construyo los objetos.
nombre=Dog("bobi",1)
#muestra el objeto
print(nombre)