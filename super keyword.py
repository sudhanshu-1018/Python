# __init__ take name, id etc from user by class

class parentclass:
    def parent_method(self):
        print("this is the parent method 1")

class childclass(parentclass):
    def parent_method(self):
        print("Harry2")
        super().parent_method()   #this is parent method 1

    def child_method(self):
        print("this is the child method")
        super().parent_method()     #this is a parent method 1


parent_object=parentclass()
parent_object.parent_method()


child_object=childclass()
child_object.child_method()
child_object.parent_method()



# in super keyword you can add in parent function as written below
class employee:
    def __init__(self,name,id) -> None:
        self.name=name
        self.id=id
        print("hello")
    def showdetails(self):
        print(f"this is my {self.name} and my {self.id} number")

class staff(employee):
    def __init__(self, name, id,lang) -> None:
        super().__init__(name, id)
        self.lang=lang
        print(f"i speak {self.lang}")


employee=employee("sudhanshu",6556)
employee.showdetails()

staff=staff("rohan",522,"hindi")
staff.showdetails()
print(staff.name)
print(staff.lang)


