class Tanu:
    def __init__(self):
        self.name = input("Enter the name :")
        self.age = int(input("Enter the age :"))
        
    def __str__(self):
        return f"Name:{self.name}, Age:{self.age}"
    
t1 = Tanu()
print(t1)
    
    
