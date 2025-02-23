# def fab(n):
#     a,b = 0,1
#     for _ in range(n):
#         yield a  ##returns value in iteration
#         a,b = b, a+b
# for num in fab(10):
#     print(num)

#map function(function, numbers)

# num = [ 1,2,3,4,5]
# squared = list(map(lambda x:x*x , num))
# print(squared)


# def sq(x):
#     return x*x
# num = [ 1,2,3,4,5]
# squared = list(map(sq, num))
# print(squared)\

#filter function takes the number with the true and discard other
# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_num = list(filter(lambda x: x%2 == 0, numbers))
# print(even_num)

# def even(x):
#      return x%2 == 0

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_num = list(filter(even, numbers))
# print(even_num)


from functools import reduce

# numbers = [1,2,3,4,5,6,7,8,9,10]
# sum = reduce(lambda x,y : x+y, numbers)
# print(sum)

# number = [3,8,1,6,2]
# great = reduce(lambda x,y : x if x> y else y, number)
# print(great)

# words = [ "hello"," ", "world"]
# sentence = reduce(lambda x, y : x+y, words)
# print(sentence)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# mul = reduce(lambda x,y : x*y, numbers)
# print(mul)


# # question  1
# words = ["abc", "csv", "json"]
# caps = list(map(lambda x: x.upper(), words))
# print(caps)

# # question  2
# words = ["cat","elephant", "dog","giraffe","bird"]
# bigger = list(filter(lambda x: True if len(x)>=4 else False, words))
# print(bigger)

# # question  3
# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_num = list(filter(lambda x: x%2 == 0, numbers))
# sq_even_num = list(map(lambda x: x*x, even_num))
# print(sq_even_num)

# # question  4
# temp1 = int(input("Enter the current temperature: "))
# temp2= int(input("Enter the last temperature: "))
# temp = [temp1, temp2]
# in_fahre = list(map(lambda x : x* 9/5 + 35, temp))
# print(f"The temperature in fahrenheit is {in_fahre}")

# # question  5
# lis1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# new_list = list(filter(lambda x : True if x> 10 or x%2 != 0 else False , lis1))
# print(new_list)
# sq_num = list(map(lambda x: x*x , new_list))
# print(sq_num)
# sum = reduce(lambda x, y : x+y , sq_num)
# print(sum)

