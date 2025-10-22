class student:
    def __init__(self,grade,name):
        self.__name=name
        self.__grade=grade
    def set_grade(self):
        if 0 <= student.__grade <= 10:
            self.__grade
        else:
            print("La nota no esta en el rango permitido")
    def get_grade(self):
        return self.__grade
    def promote (self):
        while student.__grade< 10:
            self.__grade=self.__grade+1


    