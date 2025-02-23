# ###decorator
# def decorator1(fun):
#     def wrapper():
#         print("before function")
#         fun()
#         print("after function")
#     return wrapper
# @decorator1
# def say_hello():
#     print("hello")
# say_hello()

# #argument function
# def decorator1(fun):
#     def wrapper(*args, **kwargs):
#         print("before function")
#         fun(*args, **kwargs)
#         print("after function")
#     return wrapper
# @decorator1
# def say_hello(a,b):
#     print("Sum :", a+b)
# say_hello(2,3)

# # decorator with arguments
# def greater_decorator1(Greeting):
#     def decorator1(fun):
#      def wrapper(*args, **kwargs):
#         print(f"{Greeting} : before function")
#         fun(*args, **kwargs)
#         print("after function")
#      return wrapper
#     return decorator1
# @greater_decorator1("hello")
# def say_hello(a,b):
#     print("Sum :", a+b)
# say_hello(2,3)

# #multiple decorator
# def decorator1(fun):
#     def wrapper(*args, **kwargs):
#         print("before function")
#         fun(*args, **kwargs)
#         print("after function")
#     return wrapper
# def decorator2(fun):
#     def wrapper(*args, **kwargs):
#         print("its before function")
#         fun(*args, **kwargs)
#         print(" its after function")
#     return wrapper

# @decorator1
# @decorator2
# def say_hello(a,b):
#     print("Sum :", a+b)
# say_hello(2,3)

#multiple function
def decorator2(fun):
    def wrapper(*args, **kwargs):
        print("its before function")
        fun(*args, **kwargs)
        print(" its after function")
    return wrapper


@decorator2
def sum(a,b):
    print("Sum :", a+b)
sum(2,3)
@decorator2
def diff(a,b):
    print("diff :", a-b)
diff(2,3)