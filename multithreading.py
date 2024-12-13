import threading
import time
def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

# normal code
# func(4)
# func(2)
# func(1)
    
                                 

t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])

time1=time.perf_counter()                               #calculate time period taken by code

t1.start()
t2.start()                                                # start & throw. Not wait for complition(parallel downloading)
t3.start()
time2=time.perf_counter()
print(time2-time1)

time1=time.perf_counter()
t1.join()                                                # cannot join thread before it is start()
t2.join()                                                # wait for complete download(end)
t3.join()
time2=time.perf_counter()
print(time2-time1)



# Current thread in Python refers to the thread of control that is executing the current code.
# To get the current thread, we can use the threading.current_thread() function, which returns a threading.Thread instance.
# This function can also be used to get the main thread,
# which is the thread that started the Python program, by calling it from within the main thread
# import threading
def my_func():
    print("Hello from thread",threading.current_thread().name)
thread=threading.Thread(target=my_func)
thread.start()
thread.join()



# it is also for parellel downloading
import threading
from concurrent.futures import ThreadPoolExecutor


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1=executor.submit(func,3)
        future2=executor.submit(func,2)
        future3=executor.submit(func,1)

        print(future1.result())
        print(future2.result())
        print(future3.result())

# poolingDemo()


        #Threadpooling by map function
        import threading
        l=[1,2,3,5]
        results=executor.map(func,l)
        for result in results:
            print(result)

poolingDemo()