#Primero defino la clase
class book:
    #esta funcion se usa como construcor que inicia las variables title y autor 
    def __init__(self, title, author):
        self.title=title
        self.author=author
    #esta funcion se usa para printear los objetos que se crean abajo
    def decirLib(self):
        print(f"El libro creado es {self.title} y el autor es {self.author}")
#Crear Objetos
libro1=book("Prueba1","yo")
libro2=book("Prueba2","tabienYO")
libro1.decirLib()
libro2.decirLib()

