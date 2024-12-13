a=(1,)
b=(1)
print(type(a))
print(type(b))

tup=(1,2,3,4,5,6,7)
print(tup[0])
print(tup[1:4])
print(tup[-1])
print(tup[-2])

s=list(tup)
s.append("india")
s.pop(4)
s[2]=9
tup=tuple(s)
print(tup)

tup1=(1,2,3,4,5)
tup2=(6,7,8,9)
y=tup1+tup2
print(y)
