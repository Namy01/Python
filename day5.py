###################
#The While loop
###################

# i = 1
# while i < 6:
#     print(i)
#     i += 1


# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#         i += 1 #### creates an infinit loop

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break #brakes after encountering the 3.
#     i += 1    


# i = 1
# while i < 6:
    
#     if i == 3:
#         continue
#         i += 1
#     print(i)
        

#swapping variable in python 
# x, y = 10, 20
#print(f"x:{x} and y :{y}")
# x, y = y, x
#print(f"x:{x} and y :{y}")

# print(f"x:{x} and y :{y}")
# temp = x
# x = y ### using 3rd variable
# y = temp
# print(f"x:{x} and y :{y}")

# print(f"x:{x} and y :{y}")
# x = x + y #### with out using 3rd variable
# y = x - y
# x=  x - y
# print(f"x:{x} and y :{y}")

###################################
#PYTHON STRING
# string are either in double quote or sinlge quote
# string are immutable


#to assign multiline string we can use """ ........ """ or '''......... '''
# multi_line = """ to assign multiline string we can use 
#   mutiline is a useful thing for us to during multiple things """
# print(multi_line)

""" if multi_line string is not assigned to the variable 
 then its known as doc string. it can be used as the
  comments to define the code  """

################indexing
# s = "hello, world!"
# print(s[0])
# # print(s[14]) # gives index error as there is not 14 indexed letter 
# print(s[-2]) #reads from back ward 

# ############slicing
# #string[start:end] it doesnt take end position
# print(s[0:5])
# print(s[7:12])
# print(s[-6:-1])  # always put left position first than right position

# #if we dont know either ending or starting position than
# print(s[2:]) #dont know ending or want all letter from thr start position
# print(s[:9]) #dont know starting or want all letter before ending position

# #slicing with steps
# print(s[::2]) #3rd parameter is step which skip character and is by default 1....
#  if starting and ending are not given than we assume that we take the whole 

 ########### reversing the string 
# print(s[::-1]) 

###########
#len method --->len()
#len count from 1 where as index start from 0

# print(len("hello, world"))

#To find index position
# s = "hello, world"

# for i in range(len(s)):
#     print(f"the index is {i} of {s[i]}")

#To find index position of w
# s = "hello, world"

# for i in range(len(s)):
#     if s[i] == "w":
#         print(f"the index is {i} of {s[i]}")


s = "hello, World"

for char in s:
    if char.lower() == "w":
        print("The character is either w or W")
        print(char) # the w is lowered in run time so it doesnt effects the orginal variable
    else:
         print(f"The character {char} is not w or W")





