##Importo la libreria statistics con nombre sta
import statistics as sta
#creo la clasee student
class Student:
    #Atributos name y grade rivados
    def __init__(self,name,grade):
        self.__name=name
        self.__grade=grade
    ##En este seter comprobamos que la nota este entre 0 y 10 
    def set_grade(self,newGrade):
        if 0 <= newGrade <= 10:
            self.__grade=newGrade
        else:
            print( "La nota no esta en el rango permitido")
    def get_grade(self):
        return self.__grade
    def promote (self):
        if self.__grade< 10:
            self.__grade=self.__grade+1
    #Compraramos las notas de los dos estudianes 
    def __eq__(self, other):       
        return self.get_grade() == other.get_grade()
    ##Funcion estatica para sacar el promedio 
    #hya que declararla como estatica
    # Al ser estatico no depende de un objeto concreto 
    #y puede usarse directamente desde la clase
    @staticmethod
    def average_grade(students):
        #creo una lista para sacar las noras
        #por cada objeto que le pasemos luego sacara la nota y la añadira 
        #a la lista
        notas = [student.get_grade() for student in students]
        #hacemos la media
        return sta.mean(notas)
        
##creamos los objetos?
estudiante1=Student("miguel",1)
print(f" La nota de miguel es {estudiante1.get_grade()}")

estudiante2=Student("Alex",10)
estudiante2.promote()
print(f" La nota de Alex es {estudiante2.get_grade()}")

##Se pasa la lista de los estudiantes a comparar
promedio=Student.average_grade([estudiante1,estudiante2])
print(f"el promedio es {promedio}")

##probar el __eq__ 
print(estudiante1 == estudiante2)

##__eq__ sirve para que al usar == entre dos estudiantes se comparen sus notas y no si
#son el mismo objeto.
#@staticmethod se usa para crear una función dentro de la clase que no depende de un objeto
#, como calcular el promedio de varios estudiantes.