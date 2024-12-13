# import asyncio
# import time

# async def function1():
#     print("func1")
#     await asyncio.sleep(1)
#     print("hello")
#     return "Harry"

# async def function2():
#     print("func2")
#     await asyncio.sleep(1)

# async def function3():
#     print("func3")
#     await asyncio.sleep(4)

# async def main():

#     l=await asyncio.gather(
#         function1(),
#         function2(),           # print in one time or parallel
#         function3(),
#         )

#     print(l)
# asyncio.run(main())

# async def main():
#     await function1()
#     await function2()           # print one by one
#     await function3()
# asyncio.run(main())
    
# async def main():
#     task=asyncio.create_task(function1)
#     await function2()
#     await function3()
    
# asyncio.run(main())
    



import asyncio
import time
import requests

async def function1():
    print("func1")
    URL="https://www.hotstar.com/in/shows/devon-ke-dev-mahadev/12/shiva-is-angry/1000000234/watch?filters=content_type%3Depisode"
    response=requests.get(URL)
    open("shiva 4k.mp4","wb").write(response.content)
    return "Harry"

async def function2():
    print("func2")
    await asyncio.sleep(1)

async def function3():
    print("func3")
    await asyncio.sleep(4)

async def main():

    l=await asyncio.gather(
        function1(),
        function2(),           # print in one time or parallel
        function3(),
        )

    print(l)
asyncio.run(main())