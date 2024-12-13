# in inharitance you use parent function as it is without any change
# you will only add another def which is written below 

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        print("hello")
    def showdetails(self):
        print(f"the name of employee {self.id} is {self.name}")

class programmer(employee):
    # def __init__(self, car):     # you can not add car or other things. for add you have to create new one
    #     self.car=car
        
    def showlanguage(self):
        print("the default language is pyhton")

e1=employee("sudhanshu kumar singh","18")
e1.showdetails()
e2=programmer("john","55")
e2.showdetails()
e2.showlanguage()
print(e1.name)
print(e2.name)