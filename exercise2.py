#paso 1 definimos clase y le metemos attrib si necesita 
class car:
    wheels=4
    #Paso 2 ponemos un construct y metemos los attributos que pida el enek 
    def __init__(self, brand,model):
        self.brand=brand
        self.model=model
    #el paso 3 podemos crear un funcion que printe algo o que haga cosas con 
    #los objetos que creemos de la clase.
    def infoDelCar(self):
        print(f" Brand: {self.brand} Model: {self.model} wheels: {car.wheels}")
##Aqui esta la obra donde se construyen los objetos
coche1=car("Ferrari","488 GT3 EVO")
coche1.infoDelCar()