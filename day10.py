#difference between sort and sort = lower

# a = ["banana", "Banana", "orange", "kiwi", "cherry"]
# a.sort()
# print(a)

# a = ["banana", "Banana", "orange", "kiwi", "cherry"]
# a.sort(key = str.lower)
# print(a)

# #############################
# ##******Dict***************

# # key value pair store hunxa 
# # key unique hunu parxa 
# # nested dictionary is possible

# empt = {}

# my_dict = {
#     "name" : "Alice",
#     "age"  : 22,
#     "city" : "New york"

# }
# mixed_dict = {
#     1 : " one",
#     "2" : "two",
#     (1,2) : "tuple"
# }

# print(empt)
# print(my_dict)
# print(mixed_dict)

# print(my_dict["city"])
# print(my_dict.get("age"))
# print(mixed_dict[(1,2)])
# print(mixed_dict.get((1,2)))

# #.get() method doest produce error if used key that not in dictionary
# print(mixed_dict.get((1,2,3)))  #output = # none
# #accept two parameter
# print(mixed_dict.get((1,2,3),"Value not found")) #  #output = Value not found"

# #thos way of accessing produce an error if used key that not in dictionary
# # print(mixed_dict[(1,2,3)])
# 4

# #.keys return the all of the keys in the dictionary
# x = my_dict.keys()
# print(x)
# #this is accessed using for loop
# for i in x:
#     if i == "name":
#         my_dict[i] = "namrata"
# print(my_dict)

# #to add a new key or update key value
# car = {
#     "brand" : "ford",
#     "model" : "mustang",
#     "year"  : 1964
# }
# x = car.keys()

# print(x)
# #adding key
# car["color"] = "white"
# #updating key

# car["year"] = 1992
# print(x)

# y = car.values()
# print(y)
 
#  #.items() method bring both key and value
# i = car.items()
# print(i)

# #accessing by for loop
# for x, y in car.items():
#     print("key",x , ": value", y)

# # to update the dictionary
# car.update({"color" : "red"})
# print(car)

# #remove the item from dictionary
# #pop 
# # car.pop("color")
# # print(car)

# #popitems remove the last elements
# car.popitem()
# print(car)


# del car
# print(car)

# car.clear()
# print(car)


# car = {
#     "brand" : "ford",
#     "model" : "mustang",
#     "year"  : 1964
# }

# #shallow copy
# car2 = car 
# car["color"] = "white"
# print(car)
# print(car2)


# car = {
#     "brand" : "ford",
#     "model" : "mustang",
#     "year"  : 1964
# }

# #deep copy
# car2 = car.copy() 
# car["color"] = "white"
# print(car)
# print(car2)


# #nested dictionary

# mystudent ={
#     "stud1" : {
#         "name" : "Namrata",
#         "score" : [1,2,3,4,5]
#     },

#     "stud2" : {
#         "name" : "Ashmita",
#         "score" : [9,8,3,5,5]
#     }
# }
# # print(mystudent["stud1"]["name"])

# #updating 
# mystudent.update({"stud1" : { "name" : "Namrata", "score" : [9,8,7,6,5]}})
# print(mystudent["stud1"])

# #other way
# mystudent["stud1"]["name"] = "namy"
# print(mystudent["stud1"])

# #otherr way to access 
# print(mystudent.get("stud1").get("score"))

mystudent ={
    "stud1" : {
        "name" : "Namrata",
        "score" : [9,8,3,5,5] 
    },

    "stud2" : {
        "name" : "Ashmita",
        "score" : [1,2,3,4,5]
    }
}

# sum = 0
# for x in mystudent["stud1"]["score"]:
#     sum += x
# print("The sum of score of stud1 is " ,sum)

# sum = 0
# for x in mystudent["stud2"]["score"]:
#     sum += x
# print("The sum of score of stud2 is " ,sum)

mystudent ={
    "stud1" : {
        "name" : "Namrata",
        "score" : [9,8,3,5,5] 
    },

    "stud2" : {
        "name" : "Ashmita",
        "score" : [1,2,3,4,5]
    }
}
sum = 0
keys_name = mystudent.keys()
print(keys_name)
for i in keys_name:
    for j in mystudent[i]["score"]:
      sum += j
    print(f" The name of the {i} is {mystudent[i]["name"]} and the sum of score is" ,sum)