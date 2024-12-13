x=4
print(x)

def hello():
    x=3
    print(f"The local x is {x}")
    print("Hello Everyone")

print(f"Tke global x is {x}")
hello()


y=4
def hii():
    global y
    y=6
    print(y)
    print("hello how are you")

print(y)
hii()