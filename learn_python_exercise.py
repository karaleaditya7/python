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


# number = int(input("guess the number : "))
# winning_number = 47
# guess = 1
# game_over =False

# while not game_over:
#     if number == winning_number:
#         print(f"you won, and you guessed yhe winning number in {guess} times")
#         game_over = True

#     else:
#         if number < winning_number:
#             print("too low")
#             guess += 1
#             number = int(input("guess again: "))

#         else:
#             print("too high")
#             # guess += 1
            # number = int
            # number = int(input("guess the number : "))


# number = int(input("guess the number : "))
# winning_number = 47
# guess = 1
# game_over =False

# while not game_over:
#     if number == winning_number:
#         print(f"you won, and you guessed yhe winning number in {guess} times")
#         game_over = True  #or break

#     else:
#         if number < winning_number:
#             print("too low")
            
#         else:
#             print("too high")
            
#         guess += 1
        # number = i
        # for i in range(1,11,1):nt(input("guess again: "))


# for i in range(1,11,2):
#     print(i)

# name ="aditya"
# temp=""
# #i = 0
# for i in range(len(name)):
#     if name[i] not in temp:
#         temp = temp + name[i]
#         print(name[i])
#     i += 1

#     #print(name[i])

# def add_two(a,b):
#     return a+b 

# total = add_two(5,4)
# print(total)

# def add_name(first_name,second_name):
#     return first_name+second_name

# # total = add_name("aditya"," karale")
# # print(total)
# first_name = input("enter your 1st name: ")
# second_name = input("enter your last name:")
# print(add_name(first_name,second_name))

# def sum_is(a,b,c):
#     return a*b*c
#     #print(a+b+c)

# print(sum_is(5,5,5))

# def last_char(name):
#     return name[-1]
# name = input("enter the char name: ")
# print(last_char(name))

# def odd_even(num):
#     if num%2 == 0:
#         return "even"

#     else:
#         return "odd"

# print(odd_even(10))

# def odd_even(num):
#     if num%2 == 0:
#         return "even"
#     return "odd"

# print(odd_even(9))

# def is_even(num):
#     if num%2 == 0:
#         return True
    
#     else:
#         return False

# print(is_even(9))

# def is_even(num):
#     if num%2 == 0:
#         return True
#     return False

# print(is_even(9))

# def song():
#     return "Happy Birthday"

# print(song())

# first_num = int(input("enter first num: "))
# second_num = int(input("enter second num: "))

# def greater_num(first_num,second_num):
#     if first_num > second_num:
#         return first_num
#     else:
#         return second_num
# print(greater_num(first_num,second_num))

# first_num = int(input("enter first num: "))
# second_num = int(input("enter second num: "))
# third_num = int(input("enter third num: "))

# def greater_num(first_num,second_num,third_num):
#     if first_num > second_num and second_num > third_num:
#         return first_num
#     elif second_num > first_num and first_num > third_num:
#         return second_num
#     else:
#         return third_num
# print(greater_num(first_num,second_num,third_num))


# first_num = int(input("enter first num: "))
# second_num = int(input("enter second num: "))
# def greater_num(first_num,second_num):
#     if first_num > second_num:
#         return first_num
#     return second_num

# third_num = int(input("enter third num: "))

# def greater_new(first_num,second_num,third_num):
#     # bigger = greater_num(first_num,second_num)
#     # return greater_num(bigger,third_num)
#     return greater_num(greater_num(first_num,second_num),third_num)
# print(greater_new(first_num,second_num,third_num))


# def greater(a,b):
#     if a > b:
#         return a
#     return b

# def greatest(a,b,c):
#     bigger = greater(a,b)
#     return greater(bigger,c)

# print(greatest(30,40,100))

# word = input("check palindrom: ")

# def is_palindrom(word):
#     reversed_word = word[::-1]
#     if reversed_word == word:
#         return True
#     else:
#         return False
# print(is_palindrom(word))

# def is_palindrom(word):
#     if word[::-1] == word:
#         return True
#     return False
# print(is_palindrom(word))

# for i in range(1,11):
#     print(i, end="  ")

#==========
#fibonacci series


# def fibonacci_series(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     elif n == 2:
#         print(a,b)
#     else:
#         print(a,b, end=" ")
#         for i in range (n-2):
#             c = a+b
#             a = b
#             b = c
#             print(b, end=" ")
# print(fibonacci_series(10))

# def user_info(first_name,last_name,age):
#     print(f"your first name is {first_name}")
#     print(f"your last name is {last_name}")
#     print(f"your sge is {age}")

# print(user_info("aditya","karale",27))

# mixed = [1,2,3,4,5,'six','seven',None]
# print(mixed[-1])

# mixed[1:]=['three','four']
# print(mixed)

# mixed[1]='two'
# print(mixed)


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




# print(d1)   

# user = {'name':"aditya", 'age':27}
# print(user.get('name'))

# def cube_dict(l):
#     dict = {}
#     for i in range(1,l+1):
#         dict[i] = i**3
#     return dict

# print(cube_dict(5))



# s = {1,2,3,2}
# print(s)

# l = [1,2,2,2,3,3,4,4,4,5,6,7,7,8]
# # s2 = set(l)
# s2 = list(set(l))
# print(s2)

# l1 = {1,2,3,5}
# l1.add(4)
# print(l1)

# l1.remove(2)
# print(l1)

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# print(s1 & s2)


# square = [i**2 for i in range(1,11)]
# print(square)

# negative = [-i for i in range(1,11)]S
# print(negative)

# names = ['Aditya','Rohan','Karthik']
# namess = [i[0] for i in names]
# print(namess)

# list1 = ['abc', 'pqr', 'xyz']
# list2 = [[i[::-1] for i in list1][::-1]]
# # a = list2[::-1]
# print(list2)

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even = []

# for i in numbers:
#         if i%2 == 0:
#             even.append(i)
        
# print(even)
# 
# even = [i for i in numbers if i%2 == 0]
# print(even)

# list = [1,2,3,['p','q','r'],2.5,'adi',1.6, True,False]

# string = []

# for i in list:
#         if type(i) != int:
#                 string.append(i)

# string = [str(i) for i in list if type(i)!=int]
# print(string) 
                        
# list = [1,2,3,4,5,6,7,8,9]
# list1 = []

# for i in list:
#         if i%2!=0:
#                 list1.append(-i)
#         else:
#                 list1.append(i**2)
# print(list1) 


# list_comp = [i**2 if i%2==0 else -i for i in list]
# print(list_comp)

# list = ([1,2,3],[1,2,3],[1,2,3])
# nested_list = []
# def nested(l):
#     nested_list = []
#     for i in l:
#         nested_list.append[0]
        
#         return nested_list


# print(nested(list))

# square = {num:num**2 for num in range(1,11)}
# print(square)

# square = {f"square of {num} is":num**2 for num in range(1,11)}
# print(square)
# for k,v in square.items():
#         print(f"{k}:{v}")

# string = "Aditya"
# word_count = {i:string.count(i) for i in string }
# print(word_count)

# def all_total(*args):
#     print(args)
#     print(type(args))

# all_total(1,2,3,25,35,98)

# user = {'name':"aditya", 'age':27}
# print(user.get('name'))

# print(user.get('fav'))
# print(user.get('fav','not found'))

# def cube_dict(l):
#     cubes = {}
#     for i in range(1,l+1):
#         cubes[i] = i**3
#     return cubes
# print(cube_dict(5))

# def all_total(*args):
#         total = 0
#         for num in args:
#                 total = total + num
#         return total
# print(all_total(31,2,3,5))

# add = lambda a,b : a+b
# print(add(2,3))

# multiply = lambda a,b : a*b
# print(multiply(2,3))

# def odd_even(a):
#     return a % 2 == 0

# print(odd_even(5))

#lambda fun -->


# odd_even = lambda a : a%2==0
# print(odd_even(4))


# def cal_lenght(l):
#     if len(l) > 5:
#         return True
#     else:
#         return False
# print(cal_lenght('aditya'))

# def cal_lenght(l):
#     return len(l) > 5

# print(cal_lenght('aditya'))


# cal_lenght = lambda l : len(l) > 5
# print(cal_lenght('aditya'))

# names = ['abc', 'abcd', 'aditya']
# pos =1
# for name in names:
#     print(f"{pos} ---> {name}")
#     pos += 1

# for pos,name in enumerate(names):
#     print(f"{pos} ---> {name}")


# numbers = [1,2,3,4]

# def square(a):
#     return a**2

# squaress = list(map(square,numbers))
# print(squaress)

# squaress = list(map(lambda a : a**2, numbers))
# print(squaress)

# square = [i**2 for i in numbers]
# print(square)


# def square(a):
#     return a**2
# new_list = []
# for num in numbers:
#     new_list.append(square(num))
# print(new_list)
    
# numbers = (1,2,3,4,5,6,7,8,9,10)

# def even_no(a):
#         list = []
#         for i in a:
#                 if i%2 == 0:
#                         list.append(i)
        
#         return list

# # i += 1

# print(even_no(numbers))

# numbers = [1,2,3,4,5,6,7,8,9,10]

# def is_even(a):
#     return a%2 == 0
# evens = tuple(filter(is_even, numbers))

# print(evens)

# numbers = [1,2,3,4,5]

# square = list(map(lambda a : a**2, numbers))

# print(square)

# numbers = [1,2,3,4,5]

# square = map(lambda a : a**2, numbers)

# number_iter = iter(numbers)
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))

# user_id = ['user1','user2','user3']
# names = ['aditya','rohan','atharv']

# print(list(zip(user_id,names)))


# example = [('a',1),('b',2)]
# print(dict(example))
<<<<<<< HEAD
# list1 = [1,2,3]
# list2 = [3,6,9]
# list3 = [2,4,6]

# avg = []
# def lists(l1,l2,l3):
#         p1 = []
#         p2 = []
#         p3 = []

#         for i in l1,l2,l3:
#                 p1.append(i[0])
#         # avg.append(sum(p1)/len(p1))
                
#         for i in l1,l2,l3:
#                 p2.append(i[1])
#         avg.append(sum(p2)/len(p2))
               
#         for i in l1,l2,l3:
#                 p3.append(i[2])
#         avg.append(sum(p2)/len(p2))
        
#         return p1,p2,p3
#         avg.append(sum(p1)/len(p1))
       
# print(avg)
# print(lists(list1,list2,list3))

average_finder = lambda *args : [sum(a)/len(a) for a in zip(*args)]
print(average_finder([1,2,3],[4,5,6],[7,8,9]))
=======

# numbers1 = [2,4,6,8]
# numbers2 = [1,2,3,4,5]

# #list comp

# ex = all([num%2 == 0 for num in numbers1])
# print(ex)

# def my_sum(*args):
#     if all([(type(arg) == int or type(arg) == float) for arg in args]):
#         total = 0
#         for num in args:
#             total += num
#         return total 
#     else:
#         return ("wrong input")
    
# print(my_sum(1,2,3,4.5))

# names = ['aditya k','abcd', 'pqt']

# print(max(names, key = lambda i : len(i)))

# names = ['aditya k','abcd', 'pqt']

# print(min(names, key = lambda i : len(i)))

# students =[
#     {'name':'aditya','age':27,'score':90},
#     {'name':'karthik','age':24,'score':95},
#     {'name':'rohan','age':25,'score':99}
# ]

# print(max(students, key = lambda i:i.get('score')))
# print(max(students, key = lambda i:i.get('score'))['name'])

# students ={
#     'aditya':{'age':27,'score':90},
#     'karthik':{'age':24,'score':95},
#     'rohan':{'age':25,'score':99}
# }

# print(max(students, key= lambda i:students[i]['score']))


# fruites = ['mango','apple','grapes']
# fruites.sort()
# print(fruites)

# fruites = ('mango','apple','grapes')
# print(sorted(fruites))


# badminton = [
#     {'company':'yonex','price': 4000},
#     {'company':'lining','price': 3000},
#     {'company':'victor','price': 2000}
# ]

# print(sorted(badminton, key = lambda i : i['price']))
# print(sorted(badminton, key = lambda i : i['price'], reverse = True))


# def add(a,b):
#     '''this function takes 2 numbers'''
#     return a+b
# print(add.__doc__)
# print(len.__doc__)

# print(help(sum))


# def square(a):
#     return a**2

# l = [1,2,3,4]

# def my_map(func, l):
#     new_list = []
#     for item in l:
#         new_list.append(func(item))
#     return new_list

# # print(my_map(square,l))

# print(my_map(lambda a:a**3,l))

# l = [1,2,3,4]

# print(list(map(lambda a:a**2,l)))


# def outer_func():
#     def inner_func():
#         print('insie inner func')
#     return inner_func

# var = outer_func()

# def outer_func2(msg):
#     def inner_func2():
#         print(f"inside inner func {msg}")
#     return inner_func2
# var = outer_func2("hello there")
# # var()

# def power(x):
#     def to_the(n):
#         return n**x
#     return to_the
# cube = power(3)
# print(cube(5))


# def decorater_function(any_func):
#     def inner_func():
#         print('this is awesome')
#         any_func()
#     return inner_func


# def func1():
#     print("hi hello")


# def func2():
#     print("how are you")

# var = decorater_function(func1)
# var()

# def nums(n):
#     for i in range(1,n+1):
#         print(i)
# nums(10)

# class Person: #name of class should start with capital letter
#     #class me koi bhi function define hoga use hum 'method' bolte he.
#     def __init__(self,first_name,second_name,age):
#         print('init method class')
#         self.person_first_name = first_name
#         self.person_second_name = second_name
#         self.age = age

# p1 = Person('Aditya','Karale',27)
# p2 = Person('karthik','Tanpure',24)

# print(p1.person_first_name)
# print(p2.age)


# class Laptop:
#     def __init__(self, brand_name,model_name,price):
#         self.lapi_brand_name = brand_name
#         self.lapi_model_name = model_name
#         self.lapi_prce = price

# l1 = Laptop('mac','book',100000)
# l2 = Laptop('hp','pavillion',50000)

# print(l1.lapi_brand_name)


# class Person:
#     def __init__(self,first_name,second_name,age):
#         print('init method class')
#         self.person_first_name = first_name
#         self.person_second_name = second_name
#         self.age = age
#     def full_name(self):
#         return f'{self.person_first_name} {self.person_second_name}'

# p1 = Person('Aditya','Karale',27)
# p2 = Person('karthik','Tanpure',24)

# print(p1.person_first_name)

# print(Person.full_name(p1))
# #or
# print(p2.full_name())

# l = [1,2,3]
# l.clear()
# print(l)    
# l.append(5)
# print(l)
# list.append(l,6)
# print(l)

# class Person:
#     def __init__(self,first_name,second_name,age):
#         print('init method class')
#         self.person_first_name = first_name
#         self.person_second_name = second_name
#         self.age = age
#     def full_name(self):
#         return f'{self.person_first_name} {self.person_second_name}'
    
#     def age_above18(self):
#         return self.age>18

# p1 = Person('Aditya','Karale',27)
# p2 = Person('karthik','Tanpure',24)

# print(p2.age_above18())
# print(Person.age_above18(p2))



# class Laptop:
#     def __init__(self, brand_name,model_name,price):
#         self.lapi_brand_name = brand_name
#         self.lapi_model_name = model_name
#         self.lapi_price = price
    
#     def apply_dicount(self):
#         a = self.lapi_price - self.lapi_price*0.6
#         return a 
    
    
        
 
# l1 = Laptop('mac','book',100000)
# l2 = Laptop('hp','pavillion',50000)

# print(l2.apply_dicount())

# class Circle:
#     def __init__(self,radius,pi):
#         self.radius = radius
#         self.pi = pi
#     def circumference(self):
#         return 2*self.pi*self.radius
    
# c1 = Circle(4,3.14)
# c2 = Circle(5,3.14)

# print(c1.circumference())
# print(Circle.circumference(c1))

#define class variable pi

# class Circle:
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius
#     def circumference(self):
#         return 2*Circle.pi*self.radius
    
# c1 = Circle(4)
# c2 = Circle(5)

# print(c1.circumference())
# print(Circle.circumference(c1))


# class Laptop:
#     discount = 100
#     def __init__(self, brand_name,model_name,price):
#         self.lapi_brand_name = brand_name
#         self.lapi_model_name = model_name
#         self.lapi_price = price

#     def apply_dicount(self):
#         a = self.lapi_price - self.lapi_price*Laptop.discount/100
#         return a 

# l1 = Laptop('mac','book',100000)
# l2 = Laptop('hp','pavillion',50000)

# print(Laptop.apply_dicount(l2))
# print(l2.apply_dicount())

# print(l1.__dict__)

class Laptop:
    # discount = 100
    def __init__(self, brand_name,model_name,price):
        self.lapi_brand_name = brand_name
        self.lapi_model_name = model_name
        self.lapi_price = price

    def apply_dicount(self):
        a = self.lapi_price - self.lapi_price*self.discount/100
        return a 

l1 = Laptop('mac','book',100000)
l2 = Laptop('hp','pavillion',50000)

print(Laptop.apply_dicount(l2))
print(l2.apply_dicount(10))

print(l1.__dict__)
>>>>>>> de1b235c9b89218935ecce004ba88ac1e7c4de94
