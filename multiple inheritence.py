class employee:
    def __init__(self,name) -> None:
        self.name=name
    def showdetails(self):
        print(f"{self.name} is good boy")

class dancer:
    def __init__(self,dance) -> None:
        self.dance=dance
    def showdetails(self):
        print(f"{self.dance} is his favourite dance")

class employeedancer(dancer,employee):    # here what you put first can matter. If you put dancer then showdetails of dancer will print.    
                                          #  If you put employee first then showdetails of employee will print.
    def __init__(self, name, dance) -> None:
        self.name=name
        self.dance=dance


# a=employee()
# b=dancer()
c=employeedancer("sudhanshu","tandav")
print(c.name)
print(c.dance)
c.showdetails()
print(employeedancer.mro()) #method resolution order
                            # check movement of running code