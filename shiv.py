def calculategmean (a,b):
    mean=(a*b)/(a+b)
    print(mean)

a=8
b=57
if a>b:
    print("first number is greater")
else:
    print("second number is grater or equal")
calculategmean(a,b)


for i in range(15):
    if (i==7):
      print("skip")
      continue
    elif (i==10):
      break
    print(i)


#do while loop emulate
i=0
while True:
   print(i)
   i=i+1
   #1/100=0
   if (i%100==0):
      break
    
    
