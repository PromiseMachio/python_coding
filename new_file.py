class Person:  # Capitalize class names by convention
    def __init__(self, name, age):  # Ensure proper syntax
        self.name = name
        self.age = age  # Fix: Ensure `self.age = age` has no typos
    def __str__(self):
        return f"Person:{self.name} ({self.age})"
P1 = Person("Harrier", 17)
print(P1)



    
#cars project on init() and str ()
class Cars:
    def __init__(self,model,brand,price):
        self.model = model
        self.brand= brand
        self.price = price
    def __str__(self):
        return f"{self.model},{self.brand} ${self.price}"
    
    car1=("Toyota", "premio",420000 )
    car2=("German Machines", "Mercedes",500000)
    car3=("Us F guzz", "Ferrari", 80000)
    
    print(car1)
    print(car2)
    print(car3)
    
    #class inheritance
    #Class parent
    class Person:
        def __init__(self,fname,lname):
            self.fname = fname
            self.lname = lname
        def printname(self):
            print(self.fname,self.lname)
    x= Person ("john","don")
    x.printname()    
    
    #creating a child class from the above content.
class Student(Person):
    x = Student ("Mike","Whensly")
    x.printname()

        
        
            
            