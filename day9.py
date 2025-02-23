####################################
#tuple extracting the vslue in variable and list
# fruits = ("apple", "banana" , "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green )
# print(yellow )
# print(red )

# # *var_name can be kept in any place such as
# fruits = ("apple", "banana" , "cherry", "strawberry", "raspberry")
# (green, *red, yellow) = fruits
# print(green )
# print(yellow )
# print(red )


############################
#********SET****************
############################
#in set there is no duplicate value , and it doesnot have the index

# fruits = {"apple", "banana" , "cherry", "strawberry", "raspberry"}
# for x in fruits:
#     print(x)


# #in set there is no duplicate value true and 1 is the same and 0 and false is same
# fruits = {"apple", "banana" , "cherry", "strawberry", "raspberry",1,True}
# for x in fruits:
#     print(x)
# fruits = {"apple", "banana" , "cherry", "strawberry", "raspberry",0, False}
# for x in fruits:
#     print(x)

# #make empty dist
# new_dist = {}
# #make an empty set
# set_name = set()
# #make empty string
# str_name = ""

# #way to access the set
# fruits = {"apple", "banana" , "cherry", "strawberry", "raspberry"}
# print("apple" in fruits) #return true
# fruits = {"apple", "banana" , "cherry", "strawberry", "raspberry"}
# print("ball" in fruits) #return false

#to add an item to the set we can use add method
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits.add("raspberry")
# print(fruits)

#to add multiple item we can use  update command that is just like extend in list
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"raspberry","strawberry"}
# fruits.update(fruits2)
# print(fruits)

# remove item 
# remove item from set  if the item is not found error is shown
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits.remove("apple")
# print(fruits)
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits.remove("ball") #error
# print(fruits)

#discard
# remove item from set and even though the item is not found error is  not shown
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits.discard("apple")
# print(fruits)
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits.discard("ball") # no error
# print(fruits)

#pop
#pop removes the random item from the set 
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# x = fruits.pop()
# print("The removed  item is ", x)
# print(fruits)

#clear
#clear removes all item from the set 
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits.clear()
# print(fruits)

#del
#delete the set
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# del fruits
# print(fruits) #error


#join set
#union() 
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"raspberry","strawberry"}
# fruit_all = fruits.union(fruits2)
# print(fruit_all)

# and update()
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"raspberry","strawberry"}
# fruits.update(fruits2)
# print(fruits)

#operator for union
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"raspberry","strawberry"}
# fru = fruits | fruits2
# print(fru)

#for multiple set union
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"strawberry", "mango", "pineapple"}
# fruits3 = {"raspberry","strawberry", "tomato"}
# fruit_all = fruits.union(fruits2,fruits3)
# print(fruit_all)

#for multiple set union using operator
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"strawberry", "mango", "pineapple"}
# fruits3 = {"raspberry","strawberry", "tomato"}
# fruit_all =  fruits | fruits2 | fruits3
# print(fruit_all)



# #intersection()
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"raspberry","strawberry"}
# common = fruits.intersection(fruits2)
# print(common)

#intersection_update()
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"raspberry","strawberry"}
# fruits.intersection_update(fruits2)
# print(fruits)

# # intersection for multiple
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"strawberry", "mango", "pineapple"}
# fruits3 = {"raspberry","strawberry", "tomato"}
# common = fruits.intersection(fruits2,fruits3)
# print(common)

# #multip[le sset intersection with operator]
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"strawberry", "mango", "pineapple"}
# fruits3 = {"raspberry","strawberry", "tomato"}
# fruit_all =  fruits & fruits2 &  fruits3
# print(fruit_all)


#with operator
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"raspberry","strawberry"}
# common = fruits & fruits2
# print(common)


# #difference()
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"raspberry","strawberry"}
# common = fruits.difference(fruits2)
# print(common)

# #difference_update()
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"raspberry","strawberry"}
# fruits.difference_update(fruits2)
# print(fruits)

# #with operator
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"raspberry","strawberry"}
# common = fruits - fruits2
# print(common)

# #multiple set in difference with operator
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"strawberry", "mango", "pineapple"}
# fruits3 = {"raspberry","strawberry", "tomato" , "apple"}
# fruit_all =  fruits - fruits2 - fruits3
# print(fruit_all)

#multiple set in difference
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"strawberry", "mango", "pineapple"}
# fruits3 = {"raspberry","strawberry", "tomato" , "apple"}
# fruit_all =  fruits.difference(fruits2,fruits3)
# print(fruit_all)


# #symmetric difference return the value of both except the intersection
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"strawberry", "mango", "pineapple"}
# fruit_all =  fruits.symmetric_difference(fruits2)
# print(fruit_all)

##operator of symmetric difference is ^
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"strawberry", "mango", "pineapple"}
# fruit_all =  fruits ^ fruits2
# print(fruit_all)

#updating in same set
# fruits = {"apple", "banana" , "cherry", "strawberry"}
# fruits2 = {"strawberry", "mango", "pineapple"}
# fruits.symmetric_difference_update(fruits2)
# print(fruits)


# list_name = [1,2,1,2,3,4,5,6,7,8,9,10]
# set1 = set(list_name)
# final_list = list(set1)
# print(f"The list without the duiplicate value is : {final_list}")
# print(f"The length of list without the duiplicate value is : {len(final_list)}")

#Assignment
list_name = [1,2,1,2,3,4,5,6,7,8,9,10,9]
new_set = set()
for x in list_name:
    count = 0
    for y in list_name:
        if x == y :
            count += 1
    if count>1:
        new_set.add(x)
print(f"The item that are duplicate in the list are :{new_set}")
