class BankAccount:
    ##Def de la bariable balance en modo privado
    def __init__(self,balance):
        self.__balance=balance
        ##suma al balance
    def deposit(self,agregar):
        self.__balance=self.__balance+agregar
        #Quita al balance
    def withdraw(self,quitar):
        #comprobamos que lo que se quita no sea superior de lo que tiene
        if  quitar <= self.__balance:
            self.__balance=self.__balance-quitar
        else:
            #Print de error so intenta quitar más de lo que tiene
            #nota: no aparece porque el print del get lo machaca revisa pregunta eso
            print("Saldo insuficiente")
    def get_balance(self):
        return self.__balance
##crear objeto
Cuenta1=BankAccount(100)
Cuenta1.deposit(50)
Cuenta1.withdraw(100)
#print que nos dice el balance de la cuenta
print(f"Balance actual {Cuenta1.get_balance()}")
