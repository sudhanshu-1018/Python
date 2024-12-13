class shape:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y
    
class circle(shape):
    def __init__(self,radius) -> None:
        self.radius=radius
        super().__init__(radius,radius)  #super() copy return of shape area  and put it in class circle      #radius = x, radius = y

    def area(self):
        return 3.14 * super().area()                      # radius * radius
    
    # def area(self):
    #     return 3.14 * self.radius * self.radius
    
rec=shape(3,5)
print(rec.area())

c=circle(5)
print(c.area())