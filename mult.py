import multiprocessing
import requests

def downloadfile(url,name):
    print(f"started downloading {name}")

    response=requests.get(url)
    open(f"for/{name}.jpg","wb").write(response.content)

    print(f"finised downloading {name}")

if __name__=="__main__":
    url="https://picsum.photos/2000/3000"
    pros=[]
    for i in range(50):
        p=multiprocessing.Process(target=downloadfile,args=[url,i])

        p.start()
        pros.append(p)

    for p in pros:
        p.join()
print(type(__name__=="__main__"))


# An attempt has been made to start a new process before the
#         current process has finished its bootstrapping phase.

#         This probably means that you are not using fork to start your
#         child processes and you have forgotten to use the proper idiom
#         in the main module:

#             if __name__ == '__main__':
#                 freeze_support()
#                 ...



import requests
import concurrent.futures
import multiprocess

def downloadfile(url,name):
    print(f"started downloading {name}")

    response=requests.get(url)
    open(f"files/{name}.jpg","wb").write(response.content)

    print(f"finised downloading {name}")

url="https://picsum.photos/2000/3000"

if __name__=="__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1=[url for i in range(60)]                                 # url
        l2=[i for i in range(60)]                                   # name

        results=executor.map(downloadfile,l1,l2)
        for r in results:
            print(r)
        