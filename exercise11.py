##Creo la clase student
class student:
    #Atributos name y grade rivados
    def __init__(self,grade,name):
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
    def __eq__(self):
        print("")
##creamos los objetos?
