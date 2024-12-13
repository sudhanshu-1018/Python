# A class is a blueprint or template for creating objects in Python.
#  A class defines the attributes and methods that an object can have.

# A constructor is a special method that is used to initialize an object of a class.

class person:
    def __init__(self,n,o):
        print("Hey I am person")
        self.name=n
        self.occ=o

    def info (self):
        print(f"{self.name} is a {self.occ}")

a= person("sudhanshu","developer")
b= person("sohan","HR")
a.info()
b.info()
