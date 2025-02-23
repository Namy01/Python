# python is case sensetive language so Name and name are different variable.
name = " hello , world"
Name = " hi world"
print("the value of Name is" , Name)
print("the value of name is" , name)

#snake case
my_variable = 10
total_count = 5
user_name = "John"
print("The value of variable one is", my_variable)
print("The value of variable two is", total_count)
print("The value of variable three is", user_name)

#camel case
myName = "Namrata"
lastName = "Neupane"
print("fullname is", myName, lastName)

#python language is interpreted rather than compiled.
#so variable can be updated

var1 = 5
var1 = 10
print("value of var1 is ",var1) #result is 10

# hash is an comment

# multiple varible can be assigned value at the same time using comma.
rt, st , dt = 7,8,9
print(rt, st, dt)

#########
#OPERATORS
##########

#python -> Arithmetic Operators
num1 = 10
num2 = 9
sum = num1 + num2
print(" the sum of the two number is", sum)
sub = num1 - num2
print(" the subtract of the two number is", sub)
mul = num1 * num2
print(" the mul of the two number is", mul)
div = num1 / num2
print(" the div of the two number is", div)
floor_div = num1 // num2
print(" the floor division of the two number is", floor_div)
expo = num1 ** num2
print(" the exponential of the two number is", expo)
mod = num1 % num2
print(" the modulo of the two number is", mod)

#python -> comparision operators
print("are they equal:", 3 == 4)
print("are they not equal:", 3 != 4)
print("is first num greater:", 3 > 4)
print("is first num smaller:", 3 < 4)
print("is first num smaller or equal:", 3 <= 4)
print("is first num greater or equal:", 3 >= 4)

#python -> assignment operators
a= 0 
a += 100
print("print value of a is",a)
a -= 5
print("print value of a is",a)
a *= 5
print("print value of a is",a)
a /= 5
print("print value of a is",a)
a %= 5
print("print value of a is",a)
a //= 5
print("print value of a is",a)
a **= 5
print("print value of a is",a)
a = int(a)
a &= 5
print("print value of a is",a)

#python -> logical operator

k=9
#and 
print("is it between 3 and 10", k>3 and k <10)
#or
print("is it between 3 and 10", k<13 or k <10)
#not
print("is it between 3 and 10", not(k<3 or k <1))


#python -> membership operator
x = ["apple", "banana"]
#in
print("banana" in x )
# not in
print("banana" not in x )

#python -> identity operator
#is
a=8
b=8
print("are they same", a is b)
#is not
print("are they same", a is not b)

#python -> Built in data types
#inmutable : frozenset, string, tuple
#none type (empty string)
#a = None

# to check a data type 
x = '5.0'
print(type(x))

###########
#DATA TYPES
###########

#string
x = "hello, world"
print("the data type is :", type(x))

#intger
x = 20
print("the data type is :", type(x))

#float
x = 20.2
print("the data type is :", type(x))

#complex
x = 1j
print("the data type is :", type(x))

#list
x = ["apple", "banana" , "cat"]
print("the data type is :", type(x))

#tuple
x = ("apple", "banana" , "cat")
print("the data type is :", type(x))

#tuple (in-mutable)
x = range(8)
print("the data type is :", type(x))

#dict
x = {"name" : "namrata", "age": 22}
print("the data type is :", type(x))

#set
x = {"apple", "banana" , "cat"}
print("the data type is :", type(x))

#frozen set
x = frozenset({"apple", "banana" , "cat"})
print("the data type is :", type(x))

x = None
print("the data type is :", type(x))

x = True
print("the data type is :", type(x))

#########################
#conversion of data type
#########################

#conversion into int
x = int(1)
print("value is ", x)
y = int(3.4)
print("value is ", y)
z = int("3")
print("value is ", z)

#conversion into float
x = float(1)
print("value is ", x)
y = float(3.4)
print("value is ", y)
z = float("3")
print("value is ", z)
k = float("3.4")
print("value is ", k)

#conversion into string
x = str("s1")
print("the value is ", x)
y = str(2)
print("the value is ", y)
z = str(2.0)
print("the value is ", z)



