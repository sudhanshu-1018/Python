# f=open("myfiles.txt","r")
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)

# j=open("document.txt","w")



k=open('document.txt','r')
i=0
while True:
    i=i+1
    line2=k.readline()
    if not line2:
        break
    m1=int(line2.split(",")[0])
    m2=int(line2.split(",")[1])
    m3=int(line2.split(",")[2])

    print(f"Marks of student{i} in maths is:{m1}")
    print(f"Marks of student{i} in maths is:{m2}")
    print(f"Marks of student{i} in maths is:{m3}")

    print(line2)


#writelines()
d=open('hiifiles.txt','w')
line3=['line1\n','line2\n','line3']
d.writelines(line3)
d.close
