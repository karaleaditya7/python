we cant use single quote inside single and double quote inside double

Escape sequence

we can use double quote inside double quotein follo case:
print("hello \"world\" world")
 \"
 \'
 \\  backslash
 \n  new line 
 \t  tab
 \b  backspace

 comments

only for user
ctrl + / --> to comment whole line
ctrl + / --> to uncomment whole line

==============================

by putting r at start, we can make any escape sequence as a normal text
print(r"line a \n line b")
o/p => line a \n line b

=============
print emoji

https://unicode.org/emoji/charts/full-emoji-list.html
U+1F600 => repalce + with 000 and start with \
print("\U0001F600")

==================
python as calculator

/ floating  division 2/4 = 0.5   4/2 = 2.0
// intiger division 4//2 = 2  2//4=0

print(2**3) = 8
1.4141235648
print(round(2**3,4))
1.4141

============
precedence rule 

bodmas

% modulo
print(3%2)
it give reminder = 1

=============================
variable in python

number1 = 2
print(number1)
number1 = 4
print(number1)

o/p 2
    4

name = "aditya"
print(name)
name = 123
print(name)

o/p aditya
    123

this is called dynamic programming language

variable cannot start with number e.g. 1name
u cant use special symbol in variable
can start with any letter or _

user_one_name => snake case writing => mostly used in python
UserOneName => camel case writing => mostly used in java

===========================
String Concatenation

first_name = "aditya"
last_name = "karale"
full_name = first_name +" " + last_name
print(full_name)

we cant add string with number
if we want to add string with number, make int as string e.g. "3"

==============
user input 

name = input("type your name")
print("hello" + name)
 ==========
 int() function

 number= int(input("enter a no"))

 =======================
more variables in single line 
name, age = "aditya", "27"
print("Hello" + name + "your age is" + age)

x=y=z=1
print(x+y+z)
============================
2 or more input in one line 
#name = input("enter your name : ")
#age = input("enter your age: ")
name, age =input("enter your name and age").split()
print(name)
print(age)

or 

name, age =input("enter your name and age").split(",")
print(name)
print(age)

=======================
*** string formatting

python 3

name = "aditya"
age = 27
print("hello {} your age is {}".format(name, age))

python 3.6

print(f"hello {name} your age is {age}")

========================
string indexing

language = "python"
print(language[4])

=================
string slicing

lang = "python"

#syntex- [start argument:stop argument-1]
print(lang[2:4])
print(lang[2:])
print(lang[:4])

========================
step argument

print("aditya"[2:5])

print("aditya"[0:5:2])
print("aditya"[0::2])
print("aditya"[5::-1])

============================
string method

#len function

print(len("aditya"))

or 
name = "aditya"
print(len(name))

lenght =len(aditya)
print(lenght)

#lower method
name = "ADITYA"
print(name.lower())

#upper method
name = "aditya"
print(name.upper())

#titel method
name = "aDiTyA"
print(name.title())

#count method
name ="aditya"
print(name.count("a"))

===========================
strip method

name ="     aditya         "
dots = "................"
print(name+dots)

====================
find and replace method

string = "she is beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was"))
print(string.replace("is","was",1))

#find method
print(string.find("is"))

is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1+1)

#center method

name = "aditya"
print(name.center(8,"*"))
print(name.center(len(name)+4,"*"))

#string immutable
in python strings are immutable

string = "string"
print(string.replace("t","T"))
print(string)

===============
assignment operator 

name = "aditya"
name += "ka"
print(name)

================================================
if statement 

age = input("enter your age: ")
age = int(age)
if age >= 14:
    print("you are eligible")

======================================
pass statement 

x =18
if x > 18:
    pass

======================================
else statement

we can write if statement alone but not else statement
else statement will always be after if statement 

age = input("enter your age: ")
age = int(age)
if age >= 14:
    print("you are eligible")

else:
    print("you cant play")

========================================
and, or operator

name = 'aditya'
age = '27'

if name=='aditya' and age == '27':
    print("conditio true")
else:
    print("condition false")
=======
if name=='aditya' or age == '28':
    print("condition true")
else:
    print("condition false")

========================================

if-elif-else

age=int(input("enter your age: "))

if 3 < age <= 10:
    print("you cant watch the movie")

elif 10 < age <= 18:
    print("you have half ticket")

elif age > 18:
    print("you have full ticket")

else:
    print("you cannt watch the ticket") 
===========================================

in keywoed

name = "aditya"

if "a" in name:
    print("a is present")
else:
    print("not present")

=================
check empty or not

name ="aditya"
if name:
    print("string is not empty")
else:
    print("string is empty")

=======================================

#loops
while loop and for Loop 
we can use both the loop 

#while loop 

i = 1
while i<=5:
    print("hello World")
    i = i+1

#sum using while loop

total = 0
i = 1

while i<=10:
    total = total + i
    #total += i
    i = i+1
    #i += 1
print(total)

===================================
#infinite Loop 

i =0
while i <= 10:
    print("Hello world")

OR 

while True:
    print("Hello world")

=======================================

#for loop

range is impoertant in for Loop 


for i in range(10): # 0 to 9
    print(f"Hello world : {i}")

===============
sum

total = 0
for i in range(0,10):
    total = total + i
    print(total)

<<<<<<< HEAD
==================================
guess the number 

number = int(input("guess the number : "))
winning_number = 47
guess = 1
game_over =False

while not game_over:
    if number == winning_number:
        print(f"you won, and you guessed yhe winning number in {guess} times")
        game_over = True

    else:
        if number < winning_number:
            print("too low")
            guess += 1
            number = int(input("guess again: "))

        else:
            print("too high")
            guess += 1
            number = int(input("guess again: "))

============================================================

DRY (dont repeat yourself)

number = int(input("guess the number : "))
winning_number = 47
guess = 1
game_over =False

while not game_over:
    if number == winning_number:
        print(f"you won, and you guessed yhe winning number in {guess} times")
        game_over = True  #or break

    else:
        if number < winning_number:
            print("too low")
            
        else:
            print("too high")
            
        guess += 1
        number = int(input("guess again: "))
=============================================================

step argument

for i in range(1,11,2):
    print(i)

=====================================================

#FUNCTIONS

we dont have to write code again and again by using function

def add_two(a,b):
    return a+b 

total = add_two(5,6)
print(total)

or 
print(add_new(5,6))

============================
return vs print

we should use return

def sum_is(a,b,c):  # a.b.c are arguments
    print(a+b+c)

sum_is(5,5,5)       #5,5,5 arer parameters

==========================================

default parameters

def user_info(first_name,last_name,age):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your sge is {age}")

print(user_info(aditya, karale, 27))
=======
======================
count char in name
name = input("enter your name : ")
temp=""
for i in range (len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]

=================================================
break and continue keyword

for i in range(1, 10):
    if i == 5:
        break
    print(i)

for i in range(1, 10):
    if i == 5:
        continue
    print(i)

=================================
modify number guessing game 

===========================

variable scope

x = 5 # <== Global variable
def func():
    x = 7  #  <== local variable , local variable is limited into the function only
    return x

print(x) # ==> it will print global variable

#to print local variable, we have to call function
print(func())

#to call the global variable in the function, 
x=5
def func():
    global x
    x=7
    return 7

print(func())


======================================
list

numbers = [1,2,3,4]
print(numbers)

words = ["word1","word2","word3"]
print(words)
mixed[1] = "two"
mixed[1:] = "two"
mixed[1:] = ["three","four"]

mixed = [1,2,3,4,"word1", "word2", 2.3, none]
print(mixed)

=============================

Add data to list

fruits = ["grapes","apple"]
fruits.append("mango")
print(fruits) 

=============================
insert 

fruits1 = ["apple","grapes","mango"]
fruits1.insert = [1,"pine"]

============================

delete data from list

POP == DELETE

fruits = ['apple','orange', 'pine', 'grapes', 'watermelon']
fruits.pop()
print(fruits)

fruits.pop(1)   
print(fruits)

DEL == DELETE

del fruits[1]
print(fruits)

To remove particular item from the list

fruits.remove("pine")
print(fruits)

To add data ==> append, extend, insert
To remove data ==> pop, del , remove

======================
to check particular element is in the list or not

fruits = ['apple', 'mango', 'banana', 'watermelon']
if 'apple' in fruits:
    print("apple is present")
else:
    print("not present")

=================================

count method

fruits = ['apple', 'mango', 'banana', 'watermelon']
fruits.count("apple")
print(fruits)

=======================
to SORT  items in alphabetical order

fruits = ['apple', 'mango', 'banana', 'watermelon']
fruits.sort()

print(fruits)

numbers = [3,4,6,8,9,5]
numbers.sort()
print(numbers.sort())

print(sorted(numbers)) # to see sorted numbers while printing ony

=============================
split method

convert string into the list 

user_info = "aditya 27".split()
print(user_info)

name, age = "aditya,27".split(',')
ptint(name)
print(age)

name, age = input("enter name and ege: ").split('')
print(name, end=" ")
print(age)

================================
List vs array

List is Mutable (can change)

=========================
loops in list

fruits = ['apple','banana','chiku','mango','pear']

#for loop
for fruit in fruits:
    print(fruit)

#while loop
i = 0
while i < len(fruits):
    print(fruits[i])

    i += 1

=============== 
list inside list

list = [[1,2,3],[4,5,6],[7,8,9]]

for i in list:
    for n in i:
        print(n)

print(list[1][1])
==========================

more about list 

numbers = list(range(1,11))
# print(numbers)

popped_item = numbers.pop()
print(popped_item)
print(numbers)

print(numbers.index[1])

============================
pass list to a function 

list = [1,2,3,4,5,6,7,8,9,10]
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-l)
    return negative 

print(negative_list(list))

=====================================
#with reverse method
numbers = [1,2,3,4,5]
def reverse_list(l):
    return l.reverse()

def reverse_list(l):
    l.reverse()
    return l 

print(reverse_list(numbers))

#with string slicing
def reverse_list(l):
    return l[::-1]

# popped method

popped_item =numbers.pop()
def reverse_list(l):
    popped = []
    for i in range(len(l)):
        popped_item = l.pop()
        popped.append(popped_item)
    return popped
print(reverse_list(numbers))


============================
min and max function

numbers = [2,40,10]
print(min(numbers))
print(max(numbers))

=================================================================
TUPLES




=========================================
dict

unordered collection of unique item

s = {1,2,3,2}
print(s)


print(s[1]) ===> not possible i.e unordered 

set data type

set is basically used to remove duplicate items
l = [1,2,2,2,3,3,4,4,4,5,6,7,7,8]
s2 = set(l)
print(s2)

s2 = list(set(l))

l1 = {1,2,3,5}
l1.add(4)
print(l1)

l1.remove(2)

you cant set liste or dict in set

s1 = {1,2,3,4}
s2 = {3,4,5,6}

=============================================
list comprehenssion 


square = [1**2 for i in range(1,11)]
print(square)

names = ['Aditya','Rohan','Karthik']
namess = [names[0] for i in names]
print(names)

=============================
if statement in comprehension 

numbers = [1,2,3,4,5,6,7,8,9,10]
even = []
def even_numbers(even):
    for i in numbers:
        if numbers%2 == 0:
            even.append(i)
    print(even_numbers)

string = [str(i) for i in list if type(i)!=int]
print(string) 
               

=============================
if else with list comprehenssion

list_comp = [i**2 if i%2==0 else -i for i in list]
print(list_comp)

in list comprehension of if else we took for statement at last 

====================================
Nested list ==> List under list

list = [[1,2,3],[1,2,3],[1,2,3]]
nested_list = []
def nested(l):
    nested_list = []
    for i in l:
        nested_list.append[0]

print(nested(list))

=============================================
dictionary comprehenssion

square = {num:num**2 for num in range(1,11)}
print(square)
        
remenber, dict is always in key:value format, so ":" is must

==============================================
* args 

def all_total(*args):
    print(args)
    print(type(args))

all_total(1,2,3,25,35,98)


here all work is done by * operator

you can replace args with any other word

def all_total(*args):
        total = 0
        for num in args:
                total = total + num
        return total
print(all_total(31,2,3,5))


======================================
LAMBDA function
======================================

add = lambda a,b : a+b
print(add(2,3))

==========

def odd_even(a):
    return a % 2 == 0

print(odd_even(5))


def cal_lenght(l):
    return len(l) > 5

print(cal_lenght('aditya'))

cal_lenght = lambda l : len(l) > 5
print(cal_lenght('aditya'))

==========================================

enumerate function

names = ['abc', 'abcd', 'aditya']
pos = 0
for name in names:
    print(f"{pos} ---> {name}")

=========
for pos,name in enumerate(names):
    print(f"{pos} ---> {name}")

===========
map function

numbers = [1,2,3,4]

def square(a):
    return a**2

squaress = list(map(square,numbers))
print(squares)

====================
filter function


numbers = [1,2,3,4,5,6,7,8,9,10]

def is_even(a):
    return a%2 == 0
evens = tuple(filter(is_even, numbers))

print(evens)

=================================
iterator and iterables

numbers = [1,2,3,4,5]

square = map(lambda a : a**2, numbers)

number_iter = iter(numbers)
print(numers)

numbers = [1,2,3,4,5]


number_iter = iter(numbers)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))

===========================================
zip function

user_id = ['user1','user2','user3']
names = ['aditya','rohan','atharv']

print(list(zip(user_id,names)))


tuple to dict
example = [('a',1),('b',2)]
print(dict(example))