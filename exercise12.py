from datetime import datetime
#Creamos clase Employee
class Employee:
    #definimos atributos pribados con salary=0 role=intern para pòner valores default hay que ponerlos 
    ##dentro del def defaul(variabledef=0....)
    def __init__(self, name, fecha_ingreso_tex, role="intern", salary=0):
        self.__name=name
        self.__role=role
        self.__salary=salary
        ##Variable para poder sacar la aintiguedad recoge la fecha en texto
        self.fecha_ingreso_tex=fecha_ingreso_tex
    #Definimos el set de salario
    def set_salary(self,new_salary):
        if new_salary >= 0:
            self.__salary=new_salary
        else:
            print("El salario es negativo")
    #definimos el get para salario
    def get_salary(self):
        return self.__salary
    #definimos un get para nombre para poder usarlo en pruebas
    def get_name(self):
        return self.__name
    #establecemos un set para los roles comprobamos primero si el nuevo rol esta dentro del rago 
    ## ponemos los roles en una lista
    def set_role(self,new_role):
        roles=["intern" , "junior", "senior","manager"]
        if new_role in roles:
            self.__role=new_role
        else:
            print("No esta dentro del rango")
    ##definimos el get para los roles
    def get_role(self):
        return self.__role
    ## funcion que sube salario basandose en el porcentaje que se pasa
    #he usado el self no se si esta bie XD
    def give_raise(self,percentage):
        self.__salary=self.__salary * (1+(percentage/100))
    #Para calcular la antiguedad definimos una funcion   
    def antiguedad(self):
        #convertimos el texto que nos han pasado en elemento de tipo fecha
        fecha_ingreso=datetime.strptime(self.fecha_ingreso_tex, "%Y-%m-%d")
        ##Sacamos la fecha actual para poder hacer la difrencia
        fecha_actual=datetime.now()
        ##Calculamos la antiguedad
        antiguedad= fecha_actual.year-fecha_ingreso.year
        print(f"la antiguedad de {self.__name} es {antiguedad} años")
##Creamos Los objetos
empleado1 = Employee("Ana", "2022-05-10", "junior", 1500)
#establecemos un salario
empleado1.set_salary(2000)
##Sacamos el salario del empleado
print(f"{empleado1.get_name()} cobra {empleado1.get_salary()} euros ")
##Sacamos el rol
print(empleado1.get_role())
##Subida en porcentaje
empleado1.give_raise(5)
##Comprobamos la subida
print(empleado1.get_salary())
##Vemos la atiguedad del empleado
empleado1.antiguedad()