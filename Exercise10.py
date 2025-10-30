class User :
    ##Para poder contar los objetos que se creen en una clase 
    # Usamos un contador que se va incrementando 1 dentro de __init__
    user_count=0
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        User.user_count = User.user_count + 1

Usuario1=User("Miguel", 21)
Usuario2=User("David",12)
print(f" Hay {User.user_count} usuarios")