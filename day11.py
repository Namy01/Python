# x = None
# y = None

# print(x is None)
# print(y is None)

# z = 5
# print(z is None)
# ############################
# #****function********#######

# # return type
# def add_function(a,b):
#     sum = a+b
#     return sum
# result = add_function(4,5)
# print("The sum of two num is",result)

# #non return type
# def add_function(a,b):
#     sum = a+b
#     print("The sum of two num is",sum)
    
# add_function(1,5)

# #using tuple
# def get_stats(num):
#     min_val = min(num)
#     max_val = max(num)
#     sum_val = sum(num)
#     return min_val, max_val, sum_val #returning in the form of tuple

# numbers = [1,2,3,4,5]
# min , max, sum = get_stats(numbers) #unpacking

# print("minimum:", min)
# print("maximum:", max)
# print("sum:", sum)

#using list
# def get_stats(num):
#     min_val = min(num)
#     max_val = max(num)
#     sum_val = sum(num)
#     return [min_val, max_val, sum_val] #returning in the form of list

# numbers = [1,2,3,4,5]
# stat = get_stats(numbers) #unpacking

# print("minimum:", stat[0])
# print("maximum:", stat[1])
# print("sum:", stat[2])

#using dictionary

# def get_stats(num):
#     return{
#         'min_val' : min(num),
#         'max_val' : max(num),
#         'sum_val' : sum(num)
#     }
    
#      #returning in the form of dictionary

# numbers = [1,2,3,4,5]
# stat = get_stats(numbers) #unpacking

# print("minimum:", stat['min_val'])
# print("maximum:", stat['max_val'])
# print("sum:", stat['sum_val'])


#default arguement
# def add_function(a,b = 2):
#     sum = a + b
#     return sum
# result = add_function(4,5)
# print("The sum of two num is",result)
# result2 = add_function(4)
# print("The sum of two num is",result2)

# def greet(a,b = "Namy"):
#     print(a,b)
# greet("Hello")

#put default arguement in last

#IN non default arguement  no of paramenter should be equal to no of argurments


#########local variable

# def loc():

#     x = 10 
# loc()
# print(x) ####showss error as x is local variable inside the function

###global variable
# y =10
# def loc():
#      x = 7 
#      print(y,x)
# loc()

####if we want to make global variable inside the function we can do this way
# def glo():
#      global x 
#      x = 7 
#      print(x)
# glo()
# print(x) ##can be accessed from outside

# *args -> tuple (arbitary arguments)
# **kwargs -> dictionary()


# # *args

# def my_fun(*kids):
#      print("The youngest one is", kids[2])
# my_fun("amar", "john" , 'shyam')

# #to print all
# def my_fun(*kids):
#      for x in kids:
#         print(x)
#      print("The youngest one is", kids[2])
# my_fun("amar", "john" , 'shyam')

# # **kwargs
# def my_fun(**kid):
#     print("his last name is", kid['lname'])
# my_fun(fname= "frank",lname = "gozmen")

# #to print all
# def my_fun(**kid):
#     for x,y in kid.items():
#         print(x, y)
    
# my_fun(fname= "frank",lname = "gozmen")

# def my_fun(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key,value in kwargs.items():
#         print(key, ":", value)
# my_fun('apple', 'banana', 'cherry' , color= 'red' , price = 20)


#lambda 
# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b: a * b
# print(x(6 , 7))

# def myfun(n):
#     return lambda a: a *n
# x = myfun(2)
# print(x(4))

#recursion
# def fact(a):
#     if a == 0 or a == 1:
#         return 1
#     else:
#         return a * fact(a-1)
# print(fact(6))

# def fibona(a,b,k):
#     if (b<k):
#         print(b)
#         return fibona(b, b+a, k)
# print(0)
# k = int(input("Enter the number : "))
# fibona(0,1,k)

#lambda function
#square

Square = lambda a : a** 2
k = int(input("Enter a number"))
print(Square(k))

#given num is even or not
Check_even = lambda a : a % 2 == 0
k = int(input("Enter an even number"))
print(Check_even(k))
