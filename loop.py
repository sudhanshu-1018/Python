# while True: is indifinite loop used for not end
# (when you run calculator by using while true.after fet the result they do not close they restart from beginning and ask again )
# we use (break) to stop while true loop

name="sudhanshu kumar singh"
for j in name:
    print(j)

colors=['red','blue','green']
for j in colors:
    print(j)
    for k in j:
        print(k)

for p in range(5):
    print(p)
    print(p+1)

for h in range(1,12,2):
    print(h)

i=0
while(i<3):
    print(i)
    i=i+1

i=int(input("enter the value of i:"))
while(i<=35):
    i=int(input("enter the value:"))
    print(i)
    i=i+1
    print("done with loop")
else:
    print("i am in the loop")

# use of else and break in loop 
for i in range (6):
    print(i)
    if i==4:
        break
else:
    print("sorry no i")

for i in range (6):
    print(i)
    if i==4:
        break
    else:
       print("sorry no i")

i=0
while(i<7):
    print(i)
    i=i+1
    if i==4:
        break
else:
    print("sorry no i")

i=0
while(i<7):
    print(i)
    i=i+1
    if i==4:
        break
    else:
        print("sorry no i")

for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("out of loop")