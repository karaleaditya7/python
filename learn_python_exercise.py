# print("this is \\\\ double backslash")
# print("these are /\\/\\/\\/\\ mountains")
# print("he is \t awesome")
# print("\\' \\\" \\n \\t")

# print(number1)
# number1 = 4
# print(number1)

# first_name ="aditya"
# last_name ="karale"
# full_name = first_name +" "+ last_name
# print(full_name)

# name, age = "aditya", "27"
# print("Hello" + name + "your age is" + age)
# name, age =input("enter your name and age").split()
# print(name)
# print(age)

# name = "aditya"
# age = 27
# print("hello {} your age is {}".format(name, age))
# print(f"hello {name} your age is {age}")
# print(f"hello {name} your age is {age + 2}")

# a,b,c = int(input("enter 3 no: ")).split(",")
# print((a+b+c)/3)
# language = "python"
# print(language[4])

#lang = "python"

# #syntex- [start argument:stop argument-1]
# print(lang[2:4])

# print("aditya"[2:5])
#print("aditya"[0:5:2])
# print("aditya"[0::])
# print("aditya"[5::-1])

# name = "aditya"

# print(len(name))
# lenght =len("aditya")
# print(lenght)

# name = "ADITYA"
# print(name.lower())
# name = "aditya"
# print(name.upper())
# name = "aDiTyA"
# print(name.title())
# name ="aditya"
# print(name.count("a"))
# name ="     aditya         "
# dots = "................"
# print(name+dots)
# print(name.lstrip().rstrip()+dots)
# print(name.strip()+dots)
# string = "she is beautiful and she is good dancer"
# print(string.replace(" ","_"))
# print(string.replace("is","was"))
# print(string.replace("is","was",1))
#print(string.find("is"))
# is_pos1 = string.find("is")
# is_pos2 = string.find("is",is_pos1+1)
# print(is_pos2)

# name = "aditya"
# print(name.center(8,"*"))
# print(name.center(len(name)+4,"*"))

# string = "string"
# print(string.replace("t","T"))
# print(string)

# name = "aditya"
# name += "07"
# print(name)

# age = int(input("enter your age: "))
# #age = int(age)
# if age >= 14:
#     print("you are eligible")

# x =18
# if x > 18:
#     pass

# age = input("enter your age: ")
# age = int(age)
# if age >= 14:
#     print("you are eligible")

# else:
#     print("you cant play")

# name = 'aditya'
# age = '27'

# if name=='aditya' and age == '27':
#     print("condition true")
# else:
#     print("condition false")


# if name=='aditya' or age == '28':
#     print("condition true")
# else:
#     print("condition false")

# age = int(input("enter your age: "))
# name = input("your name: ")

# if age >= 10 and (name[0]=="A" or name[0]=="a"):
#     print("you can watch the movie")

# else:
#     print("you cant watch the movie") 

# age=int(input("enter your age: "))

# if 3 < age <= 10:
#     print("you cant watch the movie")

# elif 10 < age <= 18:
#     print("you have half ticket")

# elif age > 18:
#     print("you have full ticket")

# else:
#     print("you are child") 

# name = "aditya"

# if "a" in name:
#     print("a is present")
# else:
#     print("not present")

# name ="aditya"
# if name:
#     print("string is not empty")
# else:
#     print("string is empty")

# i = 1
# while i<=5:
#     print("hello World ")
#     i = i+1

# while i<=5:
#     print(f"hello World {i}")
#     i = i+1

# total = 0
# i = 1

# while i<=10:
#     total = total + i
#     i = i+1
# print(total)

# number = int(input("anter a number: "))
# total = 0
# i = 1
# while i<= number:
#     total += i
#     i += 1
# print(total)

# number = input("enter any no.: ")

# total = 0   
# i=0
# while i < len(number):
#     total = total + int(number[i])
#     i = i + 1
# print(total)

# name = input("what is your name: ")
# neglect_double=""
# i=0

# while i < len(name):
#     if  name[i] not in neglect_double:
#         #we have to store chara in our names in the "neglect_double" variable
#         neglect_double = neglect_double + name[i]
#         print(f"{name[i]}.{name.count(name[i])}")
#     i += 1

# i =0
# while i <= 10:
#     print("Hello world")

# while True:
#     print("Hello world")

# for i in range(10):
#     print(f"Hello world : {i}")
#     print("this is line \n")

# total = 0
# for i in range(0,10):
#     total = total + i
#     print(total)

# total = 0
# for i in range(0,10):
#     total = total + i
# print(total)

# num = int(input("the number is: "))
# total=0
# for i in range(0,num+1):
#     total += i
# print(total)

# name = input("enter your name : ")
# temp=""
# i=0
# for i in range (len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]}: {name.count(name[i])}")
#         temp += name[i]

# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

# for i in range(1, 10):
#     if i == 5:
#         continue
#     print(i)

# x = 5 # <== Global variable
# def func():
#     x = 7  #  <== local variable , local variable is limited into the function only
#     return x

# print(x) # ==> it will print global variable

# #to print local variable, we have to call function
# print(func())

#to call the global variable in the function, 
# x=5
# def func():
#     global x
#     x = 7
#     return x

# print(func())
# print(x)



# numbers = [1,2,3,4]
# print(numbers)

# words = ["word1","word2","word3"]
# print(words)
# print(words[:2])

# mixed = [1,2,3,4,"word1", "word2", 2.3, None]
# #mixed[1] = "two"
# mixed[1:] = "two"
# mixed[1:] = ["three","four"]
# print(mixed)

# fruits = ["grapes","apple"]
# fruits.append("mango")
# print(fruits) 

# fruits1 = ["apple","grapes","mango"]
# fruits1.insert(1,"pine")
# print(fruits1)

# fruits = ['apple','orange', 'pine', 'grapes', 'watermelon']
# fruits.pop()
# print(fruits)
# fruits.pop(1)
# print(fruits)

# del fruits[1]
# print(fruits)

# fruits.remove("pine")
# print(fruits)

# fruits = ['apple', 'mango', 'banana', 'watermelon']
# if 'apple' in fruits:
#     print("apple is present")
# else:
#     print("not present")

# fruits.count("apple")
# print(fruits.count("apple"))

# fruits.sort()
# print(fruits)

# numbers = [3,4,6,8,9,5]
# # numbers.sort()
# # print(numbers)

# print(sorted(numbers))

# user_info = "aditya 27".split()
# print(user_info)

# user_info = "aditya,27".split(',')
# print(user_info)

# name, age = "aditya,27".split(',')
# print(name, end=" ")
# print(age)

# name, age = input("enter name and ege: ").split(' ')
# print(name, end=" ")
# print(age)

# fruits = ['apple','banana','chiku','mango','pear']

# for fruit in fruits:
#     print(fruit)

# i = 0
# while i < len(fruits):
#     print(fruits[i])

#     i += 1

# list = [[1,2,3],[4,5,6],[7,8,9]]

# for i in list:
#     for n in i:
#         print(n)

# print(list[1][1])

# print(type(list))

# numbers = list(range(1,11))
# print(numbers)

# popped_item = numbers.pop()
# print(popped_item)
# print(numbers)

# print(numbers.index(2)) 

# list = [1,2,3,4,5,6,7,8,9,10]
# def negative_list(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative 

# print(negative_list(list))

#===============

# numbers = [1,2,3,4,5]

# def square_numbers(sq):
#     squares = []
#     for i in sq:
#         squares.append(i**2)
#     return squares
# print(square_numbers(numbers))

# def reverse_list(l):
#     return l.reverse()

# def reverse_list(l):
#     l.reverse()
#     return l 

# print(reverse_list(numbers))


# def reverse_list(l):
#     return l[::-1]
# print(reverse_list(numbers))

# def reverse_list(l):
#     popped = []
#     for i in range(len(l)):
#         popped_item = l.pop()
#         popped.append(popped_item)
#     return popped
# print(reverse_list(numbers))
# list = ['abc','pqr','xyz']
# def reverse_item(l):
#     rev = []
#     for i in l:
#             q= i[::-1]
#             rev.append(q)
#     return rev 
      
# print(reverse_item(list))

# numbers = [1,2,3,4,5,6,7]

# def odd_even_list(l):
#         odd = []
#         even = []
#         for i in l:
#             if i%2 == 0:
#                 even.append(i)
#             else:
#                 odd.append(i)
#             i += 1
#     # return even and even 
#         combine = [odd, even]
#         print(combine)

# odd_even_list(numbers)

    
# list1 = [1,2,3,4]
# list2 = [1,2,5,6,7]

# l1 = [1,2,3,4]
# l2 = [1,2,5,6,7]
# def common(list1, list2):

#     combine = []
#     for i in list1:
#         if i in list2:
#             combine.append(i)
#     return combine

# print(common(l1, l2))

# numbers = [2,40,10]
# print(min(numbers))
# print(max(numbers))

# def greatest_diff(l):
#     return max(l)-min(l)
# print(greatest_diff(numbers))    

# list1 = [1,2,3,[1,2],[2,3]]
# def findout_list_no(l1):
#     count = 0
#     for i in l1:
#         if type(i) == list:
#             count += 1
#     return count

# print(findout_list_no(list1))



# user_info = {
#     'name' : 'aditya',
#     'age' : 27,
#     'fav_movie' : ['movie1','movie2'],
#     'fav_songs' : ['song1','song2']
# }

# print(user_info['name'])
# user_info['fav_songs'] = ['song1','song2']

# print(user_info)

# popped_item = user_info.pop('fav_songs')
# print(popped_item)
# print(user_info)

# popped_item = user_info.popitem()
# print(popped_item)
# print(user_info)

# more_info = {'state':'maharashtra','district':'ahmednagar','locality':'savedi'}
# user_info.update(more_info)
# print(user_info)

d = dict.fromkeys(('name','age','height'),'unknown')
# print(d)

# p = dict.fromkeys(range(1,11),'unknown')
# print(p)
# print(p.get(1))
# print(d.get('name'))

d1 = d.copy()
# d1 = d

d.popitem()
print(d)

print(d1)   