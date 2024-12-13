def double(x):
    return x**2

print(double(5))


double=lambda x:x**2
cube=lambda x:x*x*x
print(double(4))
print(cube(5))


def appl(fx,value):
    return 6+fx(value)

avg=lambda x,y,z:(x+y+z)/3
print(avg(3,6,8))
print(appl(cube,2))
print(appl(lambda x:x*x*x,2))



a=lambda x,y:print(f"{x}*{y}={x*y}")
print(a(3,5))