#The function greet takes another function as its argument, fx, and defines a nested function, mfx, inside it.
#The nested function mfx prints “good morning”, then calls the original function fx, and then prints “thanks for using this function”.
#The function greet returns the nested function mfx as its output.

def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thankyou for using this function")
    return mfx

@greet
def hello():
    print("hello world")

hello()


def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("thankyou for using this function")
    return mfx

@greet
def cube(x):
    print(x*x*x)

cube(5)



# import logging
# def func(dx):
#     def mdx(*args,**kwargs):
#         logging.info(f"{dx.__name__} with args={args},kwargs{kwargs}")
#         result=func(*args,**kwargs)
#         logging.info(f"{dx.__name__} returned {result}")
#         return result
#     return mdx

# @func
# def my_function(a):
#     return a
# print(my_function(5))
