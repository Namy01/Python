###########
#ITERATION
###########

# in python  for and while are only availableie : do while is not available

#for  _ no condition, no of repetation is known 
 # while loop is with condition , used when we dont know how many time we are going to repeate the block of code.

#iterating over the list

# numbers = [1,2,3,4,5]

# for num in numbers:
#     print(num)

# # print only 3

# numbers = [1,2,3,4,5]

# for num in numbers:
#     if num == 3:
#         print(num)
#     else:
#         print("Its not 3")

#Print only odd character:
# numbers = [1,2,3,4,5]
# for num in numbers:
#     if num % 2 != 0:
#         print(f"The given number is odd {num}")
#     else:
#         print("Its even")

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

# for x in "banana":
#     print(x)

# count = 0
# for x in "banana":
#     print(x)
#     if x == "n":
#         count += 1
# print("The number of n in banana:",count)

####################
#THE BREAK STATEMENT
###############3####

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break


# for x in "banana":
#     if x == "n":
#         break
#     print(x)

# for x in "banana":
#     print(x)
#     if x == "n":
#         print("before break")
#         break
#     print("after Break")

   

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)


# num =  [1,2,3,4,5,6,7,8,9,10]
# for x in num:
#     if x == 5:
#         continue
#     elif x == 7:
#         break
#     print("num from 0 to 6 except 5 ", x)

# for x in range(6):
#     print(x)

# mul = 1 
# for x in range(6):
#     if x == 0:
#         continue
#     else:
#         mul *= x
# print(f"the multiple of num of {mul}")

# ####### IN RANGE THE VALUE IS ALWAYS NUMERIC  
# RANGE CAN HAVE 3 PARAMETER 
    # 1ST ------>  DEFINES THE LENGTH  OR STARTING POINT 
    # 2ND ------>  DEFINES THE ENDING POINT 
    # 3RD ------>  DEFINES THE  NUMBER OF DIGIT TO SKIP IF 2 SKIP ONE IF 3 SKIP 2

# for x in range(2,300, 10):
#     print(x)

#range(2,6) mean  2 to 6 except 6

# print("even:")
# for x in range(0,30,2):
#     print(x)

# print("odd:")
# for x in range(1,30,2):
#     print(x)

# we can use else below range but not necessary


############
# Nested loop
############

adj = [ ' red', ' big', 'tasty']
fruits = ['apple', 'banana', 'cherry']

for x in adj:
    for y in fruits:
        print(x, y)