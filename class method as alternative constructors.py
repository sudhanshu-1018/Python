# check use of split in readline(),writingline()
a="harry sir - 12 - python"
print(a.split("-"))
print(a.split("-")[0])
print(int(a.split("-")[1]))


class employee:
    def __init__(self,name,salary) -> None:
        self.name=name
        self.salary=salary
        
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    
e1=employee("sudhanshu",12000)
print(e1.name)
string="john-1200"

e2=employee.fromstr(string)
print(e2.name)
print(e2.salary)
