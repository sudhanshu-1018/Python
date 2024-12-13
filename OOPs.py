class person:
    name="sudhanshu"
    occ="software developer"
    netwoth=1000000

    def info (self):
        print(f"{self.name} is a {self.occ}")

a=person()
b=person()
a.name="hari kumar singh"# change name
a.occ="business man"# change occupation
b.name="sohan"# adding new name
b.occ="HR"# adding new occupation
print(a.name,a.occ)
a.info()
b.info()



# Access specifier/modifier in OOPs

# public
class employee:
    def __init__(self) -> None:
        self.name="harry"
a=employee()
print(a.name)


# private
class employee:
    def __init__(self):
        self.__name="sudhanshu" # (__)is used for private
b=employee()
# print(b.__name)
print(b._employee__name) # to unlock private (Name Mangling)


# protected
class employee:
    def __init__(self) -> None:
        self._name="john"   # (_)is used for protection      
c=employee()
print(c._name)        #you can use protected insted of private also

