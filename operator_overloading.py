class vector:
    def __init__(self,i,j,k) -> None:
        self.i=i
        self.j=j
        self.k=k

    def __str__(self) -> str:
        return f"{self.i}i * {self.j}j * {self.k}k"
    
    def __mul__(self,x):
        return vector(self.i*x.i ,self.j*x.j ,self.k*x.k)      #print(v1 * v2)

v1=vector(3,5,6)
print(v1)

v2=vector(1,2,9)
print(v2)

print()

print(v1*v2)