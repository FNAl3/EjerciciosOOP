import math
class MathUtils:
    @staticmethod
    ##Devuelve si un valor es par o no 
    def is_even(number):
        if math.fmod(number,2)==0:
            #lo mismo que la vez anterior
            print("Es par")
            return True
        print("no es par")
        return False
    @staticmethod
    def is_prime(number):
        for num in (2,math.sqrt(number)+1):
            if math.fmod(number,num)==0:
                print(f"No es primo")
                return False
        print("Es primo ")
        return True
    @staticmethod
    ##Devuelve el factorial de un numero
    def factorial(number):
        return math.factorial(number)
    ##Devuelve la secuencia fibonacci
    @staticmethod
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
par=MathUtils.is_even(3)
primo=MathUtils.is_prime(8)
factorial=MathUtils.factorial(8)
print(MathUtils.factorial(3))
print(MathUtils.fibonacci(10)) 