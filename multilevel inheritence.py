class animal:
    def __init__(self,name,species) -> None:
        self.name=name
        self.species=species
    
    def showdetails(self):
        print(f"we called him {self.name}")
        print(f"he is {self.species}")

class dog(animal):
    def __init__(self,name,breed) -> None:
        animal.__init__(self,name,species="dog")
        self.breed=breed

    def showdetails(self):
        animal.showdetails(self)
        print(f"{self.breed}")

class dobberman(dog):
    def __init__(self,name,health) -> None:
        dog.__init__(self,name,breed="dobberman")
        self.health=health

    def showdetails(self):
        dog.showdetails(self)
        print(f"{self.health}")

o=dobberman("Tommy","good")
o.showdetails()

print(dobberman.mro())