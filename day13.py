######################
#abstraction

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "wolf!"
    
# dog1 = Dog()
# print(dog1.make_sound())


#encapsulation
#access modifier 

# class myclass:
#     def __init__(self,name,age,score):
#         self.name = name
#         self.__age = age
#         self._score = score
    
# class mark_sheet(myclass):
#     def __init__(self, name, age, score):
#         super().__init__(name, age, score)
#     def score_view(self):
#         print(f"Your score is {self._score}")

# cls1 = mark_sheet("hari",23,67)
# cls1.score_view()
# print(cls1.name)


# ####polymerphism can also be shown by the operator + can concate or perform summation.
# #operator overloading

# class A:
#     def plus(self ,a, b ):
#         return a + b
    
# cls1 = A()
# print(cls1.plus(2,3))
# print(cls1.plus("ram ","thapa"))

# #method overriding
# class A:
#     def method_A(self):
#         print("from A")
# class B:
#     def method_A(self):
#         print("from B")

# cla = B()
# cla.method_A()

#duck typing : keep the name sensible and keep method sensible as well

# function inside of the function
# def myfunction():
#     x = 90
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()
# myfunction()

# x = 300 
# def myfunctio():
#     x = 200
#     print(x)
# myfunctio()
# print(x)