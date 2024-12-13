#dir()
x=[1,2,3]
print(dir(x))

# __dir__
class person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        self.version=1

p=person("john",35)
print(p.__dict__)

#help()
class person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        self.version=1

print(help(person))
print(help(str))