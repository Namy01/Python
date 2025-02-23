# #is digit() is the method that checks is the passed item is digit or not
# s = "1234"
# print(s.isdigit())
# s = "2j"
# print(s.isdigit())
# s = "abc"
# print(s.isdigit())

# s = "ABC"
# print(s.isupper())# checks if all character is upper or not

# s = "abc"
# print(s.islower()) # checks if all character is lower or not

# #.format works as f string 
# s = "hello! {}"
# a = "good morning"
# print(s.format("Namy,"),(a))

# #f string
# a, b = 5 , 8
# s = f"The sum of {a} and {b} is {a+b}"
# print(s)

# # escape character is denoted by the  backslash "\"
# s = "escape character is denoted by the  \"backslash \"  line this "
# print(s)

# #standard delimiter is tab, comma, and pipe "|"

# #carriage return vanya space jastai

# #aru methods 
# # TO count the repeated letter we can use count() method
# s = "ABCAAAcccA"
# print(s.count("A"))

# #to find the index of the certain letter as soon as it is found
# s = "BCAAAcccA"
# print(s.find("A"))

# #to find out if the string end withs specific character  we use "endswith("specific character ") method"
# s = "BCAAAcccA"
# print(s.endswith("A"))

###########################
##########################
#####*****LIST******#######

# list character
# ->mutable ,  can store different data type , use big bracket, item separated by only comma

# numbers = [1,2,3,4,5,6]
# fruits = ['apple', 'banana', 'cherry']
# mixed_list = [10, 2.8 , "banana"]
# print(numbers)
# print(fruits)
# print(mixed_list)
# print(type(mixed_list))

# #accessing the list using index
# print(fruits[2])
# print(fruits[-2]) #access from backward

# #slicing lists
# print(fruits[0:2]) #0 and 1 index is printed
# print(fruits[0:]) #starts from 0 index to all items on the list is printed
# print(fruits[:2]) #all item before index 2 is printed


# fruits = ['apple', 'banana', 'cherry']

# #list is mutable so we can update the list using index 
# fruits[1] = "orange"
# print(fruits)

# #to add item in the list we can use append method 

# fruits.append("strawberry")
# print(fruits)

# #to remove item in the list we can use remove method 

# fruits.remove("cherry")
# print(fruits)

#static
# fruits = ['apple', 'cherry', 'banana']
# for i in range(len(fruits)):
#     if fruits[i] == "cherry":
#         fruits[i] = "Mango"
# print(fruits)

#dynamic
# fruits = ['apple', 'cherry', 'banana']
# name = input("enter value to replaced :")
# for i in range(len(fruits)):
#     if fruits[i] == name:
#         fruits[i] = input("enter value that replace :")
# print(fruits)

# fruits = ['apple', 'cherry', 'banana']
# for i in fruits:
#     print(i)

#######***while loop in list*****########
# fruits = ['apple', 'cherry', 'banana']
# index = 0
# while index < len(fruits):
#     print(fruits[index])
#     index += 1


#Dynamic append
flag=0
fruits = ['apple', 'cherry', 'banana']
print("we have these fruits:", fruits)
name = input("enter fruits to be added in the list : ")
for i in range(len(fruits)):
    if fruits[i] == name:
        print(f"The given fruit is already in the list in index {i}")
        flag = 1
if flag != 1:
    fruits.append(name)
    print(fruits)