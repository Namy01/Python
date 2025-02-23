############################################
#How TO take input from the user or terminal
#############################################

# num1 = input("Enter the number :")
# print("type is:", type(num1))

# num1 = int(input("Enter an integer A : "))
# num2 = int(input("Enter an integer B : "))
# sum = num1 + num2 
# print(f"The sum of two number {num1} and {num2} is : {sum}")

#####################
#CONDITION
#####################


########  if else and elif
# value = input("Enter a number: ")

# if value.isdigit():
#     num = int(value)
#     print(f"Converted to integer :{num}")
# elif '.' in value:
#     num = float(value)
#     print(f"Converted to float :{num}")
# else:
#     print("Invalid number input")

# number = float(input("Enter the number: "))

# if number > 0:
#     print("positive number")
# elif number < 0 :
#     print("negative number")

# elif number == 0 :
#     print("equal number")
# else:
#     print("Invalid")

####################### chained condition
# the following condition run either the currtennt condition fail or success

# x = 10 
# a =0 
# if x > 5:
#     print("x is greater than 5")
# if x > 15:
#     print("x is greater than 15")
# if a == 0 :
#     print("a is 0")

# if x >= 10:
#     print("x is greater than or equal to 10")


# x = int(input("Enter a number: "))
# if x > 5 and x < 15:
#     print("Between 5 and 15")
# else:
#     print(f"not between 5 and 15  tha is : {x}")


# x = input("Enter a number: ")
# if x == "Apple" or x == "banana":
#     print("its either apple or banana")
# else:
#     print(f"Not apple or banana : {x}")

# x = int(input("Enter a number: "))
# if not(x > 5 and x < 15):
#     print(" not Between 5 and 15")
# else:
#     print(f" between 5 and 15  that is : {x}")

# if True:
#     print("always")


##################
#Nested condition
##################

# x = 5
# if x > 0:
#     if x < 10:
#         print("The number is positive and single digit")
#     else:
#         print("he number is positive but not single digit")
# else:
#     print("x is not a positive number")

#############################
#SHORTHAND IF
# if 9 > 8 : print("alone")

#SHORTHAND IF ELSE
# x = int( input(" ENter number:"))
# print(x + 2) if x > 0 else print(x-2)

#Shorthand nested  if else
# a = 10 
# b = 10
# print("A is greater") if a > b else print("A is equal to B") if a == b else print("B is greater")

# simpler form

# if a > b:
#     print("A is greater")
# else:
#     if a == b:
#         print("A is equal to B")
#     else:
#        print("B is greater") 


###### NOT condition
a = 10 
b = 9
if not a > b:
    print("A  is not greater than ")
else:
    print(" A is greater than B")

if not a > b:
    pass
