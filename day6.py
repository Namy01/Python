#the string is immutable it gives type error 
#  if we try th o change the letter of string assigning the index 

# s = " hello"
# s[0] = "h" # error

 # to replace h  with H
# s = "hello"
# a = "H" + s[1:]
# print(a)

### string methods 

##############replace()
# s = "Hello, world"
# print(s.replace("world", "Namy")) ##only for run time
# s = s.replace("world", "Namy")
# print(s)

# s = "Hello, world"
# print(s.lower())

# s = "Hello, world"
# print(s.upper())

# s = "Hello, world"
# print(s.title())

### removing white space or other unwanted word fron ends

# s = "     hello   "
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

#to remove any specific character from ends of the string
# s = "#####hello####   "
# print(s.strip("#"))
######### error

#converting the list into string
# s = "Helllo, world"
# # a = list(s)
# # print(a)
# print(s.split())

# #default parameter is space .. we can also use other parameter such
# #  as comma which recognize the char than split the string
# #the split character is not the part of the list 
# print(s.split(","))

#join converts the list into the string
# list1 = ["h","e","l","l","o"]
# print("".join(list1))

#join can also be don using comma or space etc

#make list from bellow string having only hello, world
# name = "##############hello###world#########"
# name = name.strip("#")
# name = name.split("###")
# print(name)

name = "##hello###world####"
org_len = len(name)
name2 = name.rstrip("#")
right_len= org_len - len(name2)
name3 = name.lstrip("#")
left_len= org_len  - len(name3)
name3 = name2.lstrip("#")
name4 = name3.split("###")
name4 = "###".join(name4)
name4 = left_len* "#" + name4 + right_len * "#"
print(name4)











