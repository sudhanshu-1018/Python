import time
def using_while():     #callable
    i=0
    while i<5000:
        i=i+1
        print(i)
def using_for():       #callable
    for i in range(0,5000):
     print(i)

tt=time.time()
using_for()
t1=time.time()-tt

tt=time.time()
using_while()
t2=time.time()-tt
print(t1)
print(t2)


#time.sleep()
import time
print(4)
time.sleep(3)  #3 second
print("this is printed after 3 seconds")


#time.strftime()
import time
t=time.localtime()
formatted_time=time.strftime("%y-%m-%d %H:%M:%S",t)
print(formatted_time)
