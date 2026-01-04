#wrapping data and methods into a single unit (class) and restricting access to some of the object's components.
class BankAccount:
    def __init__(self,name, balance, password):
        self.name = name  #public attribute       
        self._balance = balance #protected attribute
        self.__password = password  #private attribute

    def get_balance(self):
        return self._balance

    def set_balance(self, newBalance):
        self._balance = newBalance


def get_balance(account): #getter method that uses the instance method
    return account.get_balance()

acc1 = BankAccount("Alice", 1000, "secret")

acc1.set_balance(1500)  #modifying protected attribute within the same module
print(acc1.name, get_balance(acc1)) 