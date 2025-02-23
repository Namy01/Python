#########################
#*class
#########################
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def myfun(self):
#         print("Hello my name is ", self.name) 

# p1 = person("Namrata",22) 
# p1.myfun()
# p2 = person("Hari",29) 
# p2.myfun()
# print(p2.name)


#single inheritance
# class Animal:
#     def speak(self):
#         return "Animal Speaks"
    
# class Dog(Animal):
#     def bark(self):
#         return "Dog barks"
    
# my_dog = Dog()
# print(my_dog.speak())
# print(my_dog.bark())

#multiple inheritance
# class A:
#     def method_A(self):
#         return "method A"
    
# class B:
#     def method_B(self):
#         return "method B"
    
# class C(A, B):
#     def method_C(self):
#         return "method C"
    
# C_obj = C()
# print(C_obj.method_A())
# print(C_obj.method_B())
# print(C_obj.method_C())

# class A:
#     def method_A(self):
#         return "method A"
    
# class B:
#     def method_B(self):
#         return "method B"
    
# class C(A, B):
#     def method_C(self):
#         return "method C"
#     def method_A(self):
#         return "form c but A"
    
# C_obj = C()
# print(C_obj.method_A())
# print(C_obj.method_B())
# print(C_obj.method_C())

#multilevel
# class A:
#     def method_A(self):
#         return "method A"
    
# class B(A):
#     def method_B(self):
#         return "method B"
    
    
# class C(B):
#     def method_C(self):
#         return "method C"
    
# C_obj = C()
# print(C_obj.method_A())
# print(C_obj.method_B())
# print(C_obj.method_C())

# class A:
#     def method_A(self):
#         return "method A"
    
# class B(A):
#     def method_B(self):
#         return "method B"
#     def method_A(self):
#         return "class B method A"
    
# class C(B):
#     def method_C(self):
#         return "method C"
    
# C_obj = C()
# print(C_obj.method_A())
# print(C_obj.method_B())
# print(C_obj.method_C())

############################
#Super()

# class Rectangle:
#     def __init__(self, len , bre):
#         self.len = len
#         self.bre = bre

#     def area(self):
#         return self.len*self.bre
    
# class Square(Rectangle):
#     def __init__(self, len):
#         super().__init__(len, len)
    
# rec1 = Rectangle(2,3)
# sq1 = Square(2)

# print("Area of the rectangle:", rec1.area())
# print("Area of the square:", sq1.area())


class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        super(). speak()
        print(f"{self.name} barks")

dog1 = Dog("leo", 5, "pug")       
dog1.speak()