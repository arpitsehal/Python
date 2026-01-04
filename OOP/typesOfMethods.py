#it is of 3 types:
#1. instance methods: methods that operate on an instance of the class
#2. class methods: methods that operate on the class itself rather than on instances of the class
#3. static methods: methods that do not operate on an instance or the class itself
class Laptop:
    storage_type = "SSD"  

    def __init__(self, storage, ram):
        self.storage = storage  
        self.ram = ram

    @classmethod
    def get_storage_type(cls): 
        print (f"Storage Type: {cls.storage_type}")

    def get_info(self):  #instance method
        print(f"Laptop with {self.storage} storage and {self.ram} RAM")

    @staticmethod
    def laptop_warranty():  
        print("This laptop comes with a 1-year warranty")
    

l1 = Laptop("1TB", "16GB")
l2 = Laptop("512GB", "8GB")

l1.get_info()
l2.get_info()

l1.get_storage_type()
Laptop.laptop_warranty()