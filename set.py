# SET
s1={1,2,5,6}
s2={3,6,7}
# print(type(s1))
print(s1.union(s2))
print(s1,s2)
# For Update s1 BY adding s2
s1.update(s2)
print(s1,s2)

#common

print(s1.intersection(s2))


print(s1.symmetric_difference(s2))
print(s1,s2)

print(s1.difference(s2))

print(s1.isdisjoint(s2))

print(s1.issuperset(s2))

print(s2.issubset(s1))

s1.add(8)
print(s1)

s1.remove(8)
print(s1)

# it is also remove but without error
s1.discard(9)
print(s1)

s8=s1.pop()
print(s1)
print(s8)

s3={20,40}
print(s3)
del s3
print(s2)

s4={2,8,9,5}
s4.clear()
print(s4)

if 1 in s1:
    print("1 is present")
else:
    print("1 is absent")

print(s1,s2)

s3={8,2,6}
s1.intersection_update(s3)
print(s1)