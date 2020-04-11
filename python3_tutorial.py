# You can use this python file to practice, refresh your knowledge or learn python3
# this script starting from logical statements and doesn't contain variables and data types
# How to use: just uncomment the output you want to see, and don't forget to comment it back
# Change anything you want in the examples to see different outputs
# Titles and head lines are surrounded by $ $, keep them commented
# empty lines between different examples
# Be careful on commenting and uncommenting lines to avoid errors
# Best of luck

# -----------------------------------------------------------------------------------------------

# $ User input $

# name = input("Enter your name : ")
# print ("you intered " + name)

# ---------------------------------------------------------------------

# $ String Formatting "F-String" $

# print ("How many kilometers you ran today!?")
# km = float(input())
# miles = km / 1.60934
# print (f"Okay, you ran {km / float(1.6)} miles today")
# print (f"miles are {miles}")
# rounded_miles = round(miles, 2) # rounding the decimals to 2 
# print (f"rounded miles are {rounded_miles}")

# ---------------------------------------------------------------------------

# $ If statements $ if, elif and else $

# color = input("What is your favourite color? ")
# if color == "Blue":
#     print ("excelent choice")
# elif color == "White":
#     print ("not bad")
# elif color == "Black":
#     print ("good choice")
# elif color == "Yellwo":
#     print ("MTN")
# else:
#     print ("You know nothing")

# --------------------------------------------------------------------------

# $ Truthy and Falsy $

# if 0:         # 0 always false
#     print ("test0") 

# if 1:         # 1 always true
#     print ("test1")

# team = input("enter your favourite team: ")
# if team: # this checks if you entered something, if yes "true", proceed, or don't do any thing
#     print(team + " is your favourite team")

# ---------------------------------------------------------------------------

# $ Logical Not $

# age = 22
# if not ((age >=1 and age <=8) or age >= 65): # 'not' reverse the whole statement
#     print ("your age between 8 and 64")

# ----------------------------------------------------------------------------

# $ Nested If $

# age = input("enter your age : ")
# if age:
#     age = int(age)
#     if age >= 18 and age <= 21:
#         print ("your good to drink, but you need a wristband")
#     elif age > 21:
#         print ("take a seat old man")
#     else:
#         print ("you are not allowed lil boy :( ")
# else:
#     print ("please enter your age!")

# ----------------------------------------------------------------------------

# $ Random Numbers $

# import random
# a = random.randint(0,10)
# print (a)

# ------------------------------------------------------------------------------

# $ For Loops and Range $

# for x in range (10):
#     print (x)

# for x in range (1,10):
#     print (x)

# for x in range (10,1,-2): # negative sign reverts the count, 2 is step
#     print (x)

# for char in "coffee":
#     print (char*5)

# number = int(input("How many times do I have to tell you : "))
# for i in range(number):
#     print ("clean up your room!")

# for num in range(1,21):
#     if num == 4 or num == 13:
#         state = "Unlucky"
#     elif num % 2 == 0:
#         state = "Even"
#     else:
#         state = "Odd"
#     print (f"{num} is {state}")

# -----------------------------------------------------------------------------

# $ While Loops $

# msg = input("what the secret word! ")
# while msg != "banana":
#     print ("WRONG")
#     msg = input("What is the secret word!")
# print ("CORRECT")

# num = 1
# while num < 10:
#     print ("\U0001f600 "*num)
#     num += 1

# for num in range(10):
#     count = 1
#     while count < num:
#         count += 1
#     print ("\U0001f600 "*num)

# ---------------------------------------------------------------------------

# $ BREAK $

# times = int(input("How many times do i haev to tell! "))
# for time in range(times):
#     print ("clean up your room")
#     if time >= 4:
#         print ("do you even listen!")
#         break

# ---------------------------------------------------------------------

# $ Gussing Game $

# import random
# random_number = random.randint(1,10)
# while True:
#     guess = input("Pick a number from 1 to 10: ")
#     guess = int(guess)
#     if guess < random_number:
#         print ("Too low!")
#     elif guess > random_number:
#         print ("Too high!")
#     else:
#         print ("you won!")
#         play_again = input("Do you wnat to play again!? 'y/n' ")
#         if play_again == "y":
#             random_number = random.randint(1,10)
#             guess = None
#         else:
#             print("Thank you for playing :) ")
#             break

# ---------------------------------------------------------------------

# $ Lists $

# chars = ['a', 'b', 'c', 'a']
# if 'd' in chars:
#     print ("True")
# else:
#     print ("False")

# for char in chars:
#     print (char)
  
# i = 0
# while i < len(chars):
#     print (chars[i])
#     i += 1

# --------------------------------------------------------------------------

# $ List Methods $

chars = ['a', 'b', 'c', 'a'] # will be used in all methods, so keep it uncommented

# -Append method
# chars.append('d') # takes only one argument
# print (chars)

# -Extend method
# chars.extend(['e','f']) # takes many arguments
# print (chars)

# -Inser method
# chars.insert(2,10) # 2 arguments, in what index to insert! and what to insert!
# print (chars)

# -Clear method
# chars.clear() # remove all the elements of the list
# print (chars)

# -Pop method
# chars.pop()
# last_char = chars.pop() # returns the removed item, we can store it in other variable
# print(chars)
# print(last_char)

# -Remove method
# chars.remove('b')
# print (chars)

# -Index method
# chars.index('c') # returns the index of a given item
# chars.index('a', 1) # find the index of 'a' after index 1 
# chars.index('a', 0, 2) # find the index of 'a' starting from index 0 to index 2 "start and end indecies" 
# print (chars.index('c'))

# -Count method
# print(chars.count('c')) # count the how many "c" in the list
# print(chars.count('a')) 

# -Reverse method
# chars.reverse()
# print(chars) 

# -sort method # in strings, Capital case comes before lower case
# numbers = [10,3,6,8,1,3,7,20]
# numbers.sort()
# print(numbers) 

# -Join method
# joined_items = ", ".join(chars)
# print (joined_items) 

# --------------------------------------------------------------------

# $ Slicing $

# numbers = [10,3,6,8,1,3,7,20]
# sliced_numbers = numbers[2:7] # take part of the list, from index 2 to 7
# sliced_numbers = numbers[2:] # to the end
# print(sliced_numbers)

# you can slice from the end using negative numbers

# copy_numbers = numbers[0:] # makes copy of the list, not same list
# print(copy_numbers)

# end_slice = numbers[:2] # start from index 0 to the given index
# print(end_slice)

# you can slice from the end using negative numbers too, slicing backward

# new_numbers = numbers[1::2] # with 2 steps
# print(new_numbers)

# revese_numbers = numbers[1::-1] # negative numbers reverse the direction
# print(revese_numbers)

# revese_numbers = numbers[::-1] # another way to reverse the list
# print(revese_numbers)

# names = ["ahmed", "mohammed", "ali"]
# reverse_name = names[1][::-1]
# print(reverse_name)

# Swaping Values "using comma"
# friends = ["John", "Doe"]
# friends[0], friends[1] = friends[1], friends[0]
# print(friends)

# ---------------------------------------------------------------------------------------

# $ List Comprehension $

# numbers = [10,3,6,8,1,3,7,20]

# manipulated_list = [x*10 for x in numbers]
# print(manipulated_list)

# names = ["ahmed", "mohammed", "ali"]
# new_names = [name[0].upper() for name in names]
# print(new_names)

# string_numbers = [str(num) for num in numbers] # converting list of numbers to strings
# print(string_numbers)

# -------------------------------------------------------------------------------------------

# List Comprehension with Conditional Logic

# numbers = [10,3,6,8,1,3,7,20]

# evens = [num for num in numbers if num % 2 == 0]
# print(evens)

# new_num = [num*2 if num % 2 == 0 else num/2 for num in numbers]
# print(new_num) 

# with_vowels = "this is so much fun!"
# without_vowels = ''.join(char for char in with_vowels if char not in 'aeiou')
# print(without_vowels)

# ----------------------------------------------------------------------------

# Nested Lists

# nested_list = [[1,2,3],[4,5],[6,7,8]]
# print(nested_list[2][2])

# for l in nested_list:
#     for value in l: # nested lists need 2 for loops to go inside of its elements
#         print(value)

# [[print(value) for value in l] for l in nested_list] # Nested list conprehension

# board = [[num for num in range(1,4)] for val in range(1,3)] # creating nested list 
# print(board)

# xo_list = [["X" if num % 2 != 0 else "O" for num in range(1,5)]for val in range(1,4)]
# print(xo_list)

# ---------------------------------------------------------------------------------------

# $ Dictionaries $

# student = {"name": "Ahmed", "age": 20, "is_graduate": False, 11:"fav num"} # keep it uncommented

# print(student)

# cat = dict(name = 'catty', age = 2) # another way of creating a dictionary using 'dict'
# print(cat)

# -accessing data inside dictionary

# student_name = student["name"]
# print(student_name)

# -itrating over dictionaries

# for value in student.values(): # print only the values of the dictionary,, "dict_name.values()"
#     print(value)

# for key in student.keys(): # print only the keys of the dictionary,, "dict_name.keys()"
#     print(key)
    
# for item in student.items(): # print both the key and it's value "output are tuples",, "dict_name.items()"
#     print(item)
# for key,value in student.items(): # print both the key and it's value " not tuples"
#     print(key,value)
# for key,value in student.items(): # printing using f-string
#     print(f" Key is {key} and Value is {value}")

# -using 'in' with dictionaries.. "testing existance of certain key or value in dictionary"

# testing the existance of key:
# if "name" in student:
#     print("True")
# if "city" in student: # "not in" can be used too
#     print("False")

# -testing the existance of value:
# if "Ahmed" in student.values():
#     print("True")
# if "Mohammed" in student.values():
#     print("False")

# -testing existance of key by student.keys()!!
# if "name" in student.keys():
#     print("True")   # yes it works, but no need, .keys() is already the default, just dict_name is enough

# ---------------------------------------------------------------------------------------

# $Dictionary Methods$

# -clear method
# student.clear()
# print(student)

# -copy method
# student_copy = student.copy()
# print(student_copy)
# student_copy is student # False, because we store the copied on in different memory 'reference', but they are equal "="
# student_copy == student # True

# -fromkeys method
# new_user = {}.fromkeys(['name', 'age', 'email', 'score'], 'unknown') # or you can use dict.fromkeys([])
# # print(new_user)

# fromkey_user = new_user.fromkeys(['phone'], 'unknown')
# print(fromkey_user)
# print(new_user)

# -get method
# get_stu_name = student.get("name")
# print(get_stu_name)
# get_stu_city = student.get("city")
# print(get_stu_city) # output is None, instead of keyError

# -pop method
# poped_name = student.pop('name')
# print(poped_name)
# print(student)
# poped_city = student.pop('city')
# print(poped_city) # keyError

# -popitem method
# popeditem = student.popitem()
# print(popeditem)
# popeditem_name = student.popitem('name')
# print(popeditem_name) # TypeError

# -update method
# first = dict(a=1, b=2, c=3, d=4)
# second = {}
# third = {'z':100}
# second.update(first)
# third.update(first) # will add the key-value pairs in first to existing pair 
# print(second)
# print(third)
# print(first.update({})) # will not removes things
# print (first)

# --------------------------------------------------------------------------

# $ Nested Dictionaries and Lists $

# playlist = {"title": "Favourites",
#             "author": "John",
#             "songs": [
#                 {"name": "song 1", "artist": ["artist1"], "duration": 3.5},
#                 {"name": "song 2", "artist": ["artist2", "unknown"], "duration": 3.0},
#                 {"name": "song 3", "artist": ["artist3"], "duration": 4.3}
#             ]
#             }
# print(playlist)
# total_duration = 0
# for song in playlist["songs"]:
#     total_duration += song["duration"]
# print(total_duration) # the summatoin of all durations

# ------------------------------------------------------------------

# $ Dictionary Comprehension $

# first = dict(a=1, b=2, c=3, d=4)
# squared_numbers = {key: value ** 2 for key,value in first.items()}
# print (squared_numbers)

# new_numbers = {num:num ** 2 for num in [1,2,3,4,5]}
# print (new_numbers)

# str1="ABC"
# str2="123"
# combo = {str1[i]:str2[i] for i in range(0,len(str1))}
# print(combo)

# num_list = [1,2,3,4] # conditional logic with dictionaries
# even_odd = {num : ("Even" if num % 2 == 0 else "Odd") for num in num_list}
# print(even_odd)

# -----------------------------------------------------------------------

# $ Tuples and Sets $

# $ Tuples $

x = (1, 2 , 3, 3, 3, 5)
# print(3 in x) # True
# x[0] = 4 # trying to change!! TypeError: 'tuple' object doesn't support item assignment, cus tuples are unchangable
# print(x[2])

# y = tuple((1, 'a', 'name')) # creating tuple using "tuple" keyword
# print(y)

# -tuples can be used as keys in dictionary
# location = {
#     (23.654, 447.968): "Office 1",
#     (10.654, 217.968): "Office 2",
#     (6.654, 417.968): "Office 3",
# }
# print(location)

# loc = {
#     [23.654, 447.968], "office 1", # using list as a key in dictionary!?
#     [10.654, 217.968], "Office 2",
# }
# print(loc) # TypeError : unhashable type: 'list'

# print (student.items()) # returns a list of tuples

# Looping in tuple .. same as looping in list

# for i in x:
#     print(i)

# ---------------------------------------------------------------------------------

# $ Tuple Methods $

# -Count method
# print(x.count(3))

# -Index method
# print(x.index(1))

# -nested tuples are same as nested lists
# nested_tuple = ('a', 'b', (8,9), 'c')
# print(nested_tuple)
# print(nested_tuple[2])
# print(nested_tuple[2][0])

# -tuple slicing is same as list slicing too

# sliced_tuple = nested_tuple[1:3]
# sliced_tuple = nested_tuple[0:3:2]
# print(sliced_tuple)

# ----------------------------------------------------------------------------------

# $ Sets $

s = {1, 2, 3, 4, 5, 6, 7, 8} # creating a set

# print(s)

# t = set({'x', 'y', 'z'}) # another way for creating set
# print(t)

# -accessing a set!!?
# print(s[0]) # TypeError: 'set' object does not support indexing
# indexing is not supported, but you can test if an element is in a set
# print(4 in s) # True
# print(10 in s) # False

# for num in s: # accessing all values with the same old for loop
#     print(num) 

# cities = ["Khartoum", "Madani", "Alobaied", "Algadarif", "Khartoum", "Sinar", "Aldamazeen", "Madani", "Shandi"]
# cities_set = set(cities) # converting list to set
# print(cities_set ) # notice there is no more duplications, sets don't contains duplicated items
# print(list(cities_set)) # return it back to list, with unique cities, no duplications

# --------------------------------------------------------------------------------------------

# $ Set Methods $

# -add method
# s.add(3.5)
# print(s)

# -remove method
# s.remove(2)
# s.remove(5.5) # trying to remove item not in set!! KeyError: 5.5
# print(s)

# -copy method
# s_copy = s.copy()
# print(s_copy) 

# -clear method
# s.clear()
# print(s)

# ------------------------------------------------------------------------------

# $ Sets Math $

# math_students = {"kepa", "kante", "mount", "james", "tomori", "kova"}
# biology_students = {"zouma", "abraham", "kante", "kova", "willian"}

# print(math_students | biology_students) # math union
# print(math_students & biology_students) # math intersection

# --------------------------------------------------------------------------------

# $ Set Comprehension $

# s_co = {x * 2 for x in s} # same as list comprehension, notise the prackets
# print(s_co)
# s_dict = {x:x*2 for x in s} # returns dictionary
# print(s_dict)

# ------------------------------------------------------------------------------------

# $ Functions $

# def say_something(): # creating function using 'def' stands for define, then the function name
#     print("something")
# say_something() # calling the function

# -Return key word

# def square_of_5():
#     return 5**2
# result = square_of_5()
# print(result)

# from random import random # importing "random" module to use its methods
# def coin_flip():
#     r = random() # generate a random number 0-1
#     if r > 0.5:
#         return "head"
#     else:
#         return "tail"
# print(coin_flip())

# -passing parameters to function

# def square_of_number(num): # num here is a prameter
#     return num**2
# print(square_of_number(6))

# def add(a,b): # passing 2 parameters
#     return a+b

# def exponent(number, power=2): # passing default parameter "pwoer"
#     if power:
#         return number ** power
#     return number ** 2
# print(exponent(3,3)) # here, we overwrite the default parameter
# print(exponent(7)) # here, we use the default parameter

# -passing function as a prameter!! you can pass anything as a parameter(functions, lists, dictionaries, strings, booleans)

# def add(a,b):
#     return a + b

# def math(a, b, fn=add):
#     return fn(a, b)

# def subtract(a,b):
#     return a - b

# print(math(1,2)) # 3
# print(math(2,2, subtract)) # 0

# -Keyword Arguments

# def full_name(first="ahmed", last="mohammed"):
#     return f"your name is {first} {last}"
# print(full_name("ahmed"))
# print(full_name(last="adam", first="yousif")) # using keyword arguments, the order is not a matter when using keyword arguments

# ---------------------------------------------------------------------------------------------

# $ Scope $

# instructor = "colt" # global variable, not defined inside the function
# def say_hallo():
#     return f"Hallo {instructor}"
# print(say_hallo())
# print(instructor) # it works

# def say_hallo():
#     instructor = "Steele" # variable defined inside the function
#     return f"Hallo {instructor}"
# print(say_hallo())
# print(instructor) # NameError: name 'instructor' is not defined,,, cus it defined inside the function, not global variable

# total = 0 # global variable
# def increament():
#     total += 1 # trying to manipulate global variable inside a function!!
#     return total
# increament()  # UnboundLocalError: local variable 'total' referenced before assignment,, python looking for a local variable
# this doesn't mean you cannot use global function inside function, but you need to minimize that

# total = 0 
# def increament():
#     global total # using 'global' keyword to tell python to look for 'total' globaly
#     total += 1 
#     return total
# print(increament())

# ---------------------------------------------------------------------------------------

# $ Documenting Functions $

# def say_hallo():
#     """ a simple function to print hallo""" # function documentation using triple double quote
#     return "Hallo"
# print(say_hallo())
# print(say_hallo.__doc__) # a way to get the function documentation

# getting any function documentation!! trying to see whats in 'print' documentation
# print(print.__doc__)

# ----------------------------------------------------------------------------------------------

# $ *args $

# def sum_all_num(num1,num2,num3): # demo function
#     return num1 + num2 + num3 
# print(sum_all_num(20,10,30))

# what if you want to add more numbers!!
# def all_nums(*args):
#     print(args) # so args is tuple of all passed arguments
# print(all_nums(2,5,7,8,6,9)) 

# so, if you want to do sum of nums, you need to loop in the tuple
# def sum_nums(*args): # you can still add parameters alonside *args
#     sum = 0
#     for num in args:
#         sum += num
#     return sum
# print(sum_nums(1,10,50,48,4))

# def insure_correct_info(*args):
#     print(args)
#     if "ahmed" in args and "mohammed" in args: # check if "ahmed" and "mohammed" are passed in arguments
#         return "Welcome"
#     return "Not sure who you are"
# print(insure_correct_info()) # not sure who you are
# print(insure_correct_info(1, "string", "ahmed", "mohammed", False)) # Welcome
# so it checks if the condition is met according to the arguments passed or not

# ----------------------------------------------------------------------------------------

# $ **kwargs $

# def test_kwargs(**kwargs):
#     print(kwargs) # so kwargs is dictionary, not a tuple
#     for person, color in kwargs.items(): # how to retrieve key and value from dictionary
#         print(f"{person}'s favorite color is {color}")
# print(test_kwargs())
# print(test_kwargs(yousif = "red", hamid = "white"))
# print(test_kwargs(yousif = "red", hamid = "white", shahin = "blue", omer = "black")) # it works no matter how many we pass in

# def special_greeting(**kwargs):
#     if "david" in kwargs and kwargs["david"] == "special":
#         return "special greeting David"
#     elif "david" in kwargs:
#         return f"{kwargs['david']} David"
#     return "Not sure who's this"
# print(special_greeting(david='hallo'))
# print(special_greeting(david='special'))
# print(special_greeting(john='special'))
# print(special_greeting(heather='hallo', david='special'))

# -------------------------------------------------------------------------------------------

# $ Ordering Parameters $ # 1- parameters 2- *args 3- default parameters 4- **kwargs

# def display_info(a, b, *args, instructor="colt", **kwargs):
#     return [a, b, args, instructor, kwargs]
# print(display_info(1,2,3, last_name="adam", job="Instructor"))
# a -> 1
# b -> 2
# args -> (3,) # tuple
# instructor -> 'colt' # default parameter
# kwargs -> {'last_name': 'adam', 'job': 'Instructor'} # dictionary

# --------------------------------------------------------------------------------------------

# $ Tuple Unpacking $

# def sum_nums(*args): # same old function
#     print(args) # check what's inside args
#     sum = 0
#     for num in args:
#         sum += num
#     return sum
# print(sum_nums(1,10,50,48,4)) # we can pass arguments like this
# numbers = [10,21,33,1,25,64,82] # what if you want to pass this!!
# print(sum_nums(numbers)) # TypeError
# print(sum_nums(*numbers)) # 236, so * unpacks the values of the list "or tuple"

# -------------------------------------------------------------------------------------

# $ Dictionary Unpacking $

# def display_names(first, second):
#     print(f"{first} says hi to {second}")
# names = {"first": "ahmed", "second": "mohammed"}
# display_names(first="charly", second="mosunda") # we can call it directly
# display_names(**names) # use the double ** to unpack the dictionary

# def add_multiply_numbers(a, b, c, **kwargs): # you can still pass arguments before **kwargs
#     print(a + b * c)
#     print("Other stuff...")
#     print(kwargs)
# add_multiply_numbers(1,3,5) # simple passing
# data = dict(a=1, b=2, c=3) # what if we need to pass this dictionary!
# add_multiply_numbers(data) # TypeError
# add_multiply_numbers(**data, color="blue") # with **

# --------------------------------------------------------------------------------------------

# $ Built-in Functions $

# -Lambda function

# def square(num): # simple function that returns the square of a number
#     return num * num

# def square(num): return num * num # also, can be written like this
# or 
# lambda num: num * num # you can think of it as function has no name

# lambda_square = lambda num: num * num # save it to variable
# print(lambda_square(3))

# lambda_exponent = lambda num, power: num ** power 
# print(lambda_exponent(4,3))

# print(square.__name__) # check the name of the function
# print(lambda_square.__name__) # has no name
# print(lambda_exponent.__name__) # has no name

# -Map function

# nums = [1,2,3,4,5,6,7,8]
# doubles = map(lambda x: x*2, nums)
# print(doubles) # <map object at 0x7fe080373a58>, we need to iterate over this too
# for d in doubles:
#     print(d)
# print(list(doubles)) # if you don't want to iterate, you can convert it to a list

# people = ["asim", "kharkhar", "jamal", "kareem"]
# upper_people = map(lambda name: name.upper(), people) # upper case all the strings
# print(list(upper_people))

# names = [
#     {"first": "rusty", "last": "steele"},
#     {"first": "colt", "last": "steele"},
#     {"first": "blue", "last": "steele"},
#     ] # a list of dictionaries
# first_names = list(map(lambda n: n["first"], names))
# print(first_names)

# -Filter Function

# l = [10,15,20,25,30,35,40,45]
# evens = list(filter(lambda y: y%2 == 0, l)) # return only the values that meet the condition "True"
# print(evens)

# names = ["austin", "penny", "anthony", "angel", "billy"]
# a_names = list(filter(lambda n: n[0] == "a", names)) # return names that start with "a"
# print(a_names)

# users = [
#     {"username":"ammar", "tweets": ["Chelsea", "COYB"]},
#     {"username":"wael", "tweets": ["Liverpool", "YNWA"]},
#     {"username":"mazin", "tweets": ["Manchester", "GGMU"]},
#     {"username":"mohammed", "tweets": ["Arsenal", "COYG"]},
#     {"username":"adam", "tweets": []},
#     {"username":"omer", "tweets": []},
# ] # list of dictionaries of user's tweets "list"
# inactive_users = list(filter(lambda user: len(user["tweets"]) == 0, users))
# print(inactive_users)
# active_users = list(filter(lambda u: u["tweets"], users)) # lists, empty strings '' and 0 are falsie "False" by default
# print(active_users)
# not_active = list(filter(lambda u: not u["tweets"], users)) # notice "not", to give the opposite
# print(not_active)
# lc_not_active = [user for user in users if not len(user["tweets"])] # can be done by list comprehension too! even easier
# print(lc_not_active)

# -compine filters and maps

# names = ["ahmed", "amal", "mohammde", "noor", "adil"]
# instructors = list(map(lambda name: f"your instructor is {name}",
#     filter(lambda n: len(n)<5, names)))
# print(instructors)

# -All Function: all()

# all([0,1,2,3,4]) # False, cuz 0 is falsie
# all([char for char in "eio" if char in "aeiou"]) # True, all 'eio' letters are in 'aeiou'
# people = ["Charly", "Chris", "Colt", "Camry"]
# all([string[0] == 'C' for string in people]) # check if all strings start with 'C', returns True

# -Any Function: any()

# any([0,1,2,3,4]) # True, cuz 1 is truthy
# any([x for x in [1,2,3] if x>2]) # True  
# any([value for value in [1,2,3] if value>5]) # False, cuz all values are falsie  

# -Sorted Function: sorted()

# numbers = [2,9,4,88,110,3,90,1000,199,0]
# print(sorted(numbers))
# print(sorted(numbers, reverse=True)) # sort by the opposite direction
# letters = ["f", "I", "j", "Q", "Z", "X", "a", "B"]
# print(sorted(letters))

# users = [
#     {"username":"ammar", "tweets": ["Chelsea", "COYB", "hazaaard", "kanteeee"]},
#     {"username":"wael", "tweets": ["Liverpool", "YNWA", "Salaaah"]},
#     {"username":"tibyan", "tweets": ["Manchester", "GGMU"], "color": "Red"},
#     {"username":"mohammed", "tweets": ["Arsenal", "COYG"], "num": 7, "color": "white"},
#     {"username":"adam", "tweets": []},
#     {"username":"omer", "tweets": []},
# ] # sorting a dict!!
# print(sorted(users, key=len)) # sorted by the length of dict
# print(sorted(users, key=lambda user: user["username"])) # sort by username
# print(sorted(users, key=lambda user: len(user["tweets"]))) # sort by tweets "most tweets"

# songs = [
#     {"title": "somebody", "playcounts":10},
#     {"title": "sky full of stars", "playcounts":21},
#     {"title": "blinding lines", "playcounts":13},
#     {"title": "Kkkkkkoooorrrrronnnaaa Viiiirruuuuss", "playcounts":8},
#     ]
# print(sorted(songs, key=lambda song: song["playcounts"]))

# -Max and Min Function: max(), min()

# print(max(99,12,50,100,1))
# print(min(99,12,50,100,1))
# print(max("c","d","a","y","i"))
# print(min("c","d","a","y","i"))

# names = ["Arya", "Semson", "Dora", "Tim", "Ollivander"] # min and max!!
# print(max(names)) # Tim!!
# print(min(names)) # Arya!!
# it returns the max and the min based on the alphapetic order
# print(max(names, key=lambda n: len(n))) # Ollivander
# print(min(names, key=lambda n: len(n))) # Tim

# songs = [
#     {"title": "somebody", "playcounts":10},
#     {"title": "sky full of stars", "playcounts":21},
#     {"title": "blinding lights", "playcounts":13},
#     {"title": "Kkkkkkoooorrrrronnnaaa Viiiirruuuuss", "playcounts":8},
#     ]
# print(max(songs, key=lambda song: song["playcounts"])) # maximum playcounts
# print(min(songs, key=lambda song: song["playcounts"])) # minimum playcounts
# print(min(songs, key=lambda song: song["playcounts"])["title"]) # if you want the title of the minimum playcounts song

# -Reversed Function: reversed()

# nums = [1,2,3,4]
# print(list(reversed(nums)))
# letters = ("a", "x", "z", "h")
# print(list(reversed(letters)))
# print(list(reversed("Hallo World")))
# print("hallo"[::-1]) # slicing!! can make reversed string too, but for only lists, not all iterators support sclices
# print(''.join(list(reversed("hallo")))) # if you insist in using reversed

# -Length Function: len()

# len("awesome")
# len([1,2,3,4,5])
# len(range(20,200))
# len({"a","b","c","d"})
# len({"a":1, "b":2})
# print("check".__len__()) # len() behind the scenes calls .__len__()

# -Absolute Function: abs()

# print(abs(-5)) # 5
# print(abs(5)) # 5
# print(abs(-2.444)) # 5

# -Summation Function: sum()

# print(sum([1,2,3,4]))
# print(sum([1,2,3,4], 10)) # 10 is start, like start counting from 10, its optional, by default its 0
# print(sum([1,2,3,4], -10)) # 0, start counting from -10

# -Round Function: round()

# print(round(2.2)) # 2
# print(round(2.5)) # 2
# print(round(2.51)) # 3!!! it rounds to the nearest integer
# print(round(2.21574369, 2)) # 2.21, you can specify the number of digits you want to round to
# print(round(4.21574369, None)) # None sets round to the default, which is, rount to nearest integer

# -Zip Function: zip()

# zipped_test = zip(["a", "b", "c"], [1,2,3,4,5])
# print(list(zipped_test)) # convert it to a list
# print(dict(zipped_test)) # convert it to a dictionary

# letters = ["a", "b", "c"]
# numbers = [1,2,3,4,5]
# words = ["hi", "lol", "haha", ";)"]
# print(list(zip(letters,numbers,words))) # the output length according to the shortest iterable

# five_by_two = [(0,1), (1,2), (2,3), (3,4)]
# print(list(zip(*five_by_two))) # unpacking, 2 individual lists

# complex example

# midterm = [80, 91, 78]
# finals = [98, 89, 53]
# students = ["Dan", "Ang", "Kate"]
# how to assign each student to his/her highiest grade, in a dictionary!!?
# highiest_grades = {"Dan": 98, "Ang":91, "Kate":78} , this sould be the output
# by using list comprehension:
# highiest_grades = dict(zip(students, [max(pair) for pair in zip(midterm, finals)]))
# print(highiest_grades)
# by using lambda:
# grades = dict(
#     zip(
#         students,
#         map(
#             lambda pair: max(pair),
#             zip(midterm,finals)
#         )
#     )
# )
# print(grades)

# ----------------------------------------------------------------------------------------------

# $ Debugging $

# Common Types of Error in python:
    # * SyntaxError
    # examples
# def first:
# None = 1
# return 

    # * NameError
# test # name 'test' is not defined

    # * TypeError
# len(5)
# "awesome" + []    

    # * IndentationError
# l = ["covid-19"]
# l[2] # out of range

    # * ValueError
# int("foo")

    # * KeyError
# d = {}
# d["foo"]

    # * AttributeError
# "world".foo

# ------------------------------------------------------------------------------------------

# $ Raise your own Errors # using "raise" keyword $

# -raise ValueError("Invalid Value")

# def colorize(text, color):
#     colors = ("red", "white", "black", "blue")
#     if type(text) is not str:
#         raise TypeError("text must be instance of str")
#     if color not in colors:
#         raise ValueError("color is invalid color")
#     print(f"printed {text} in {color}")
# colorize("world", "red")
# colorize(2, "red")
# colorize("world", "purple")

# ------------------------------------------------------------------------------------

# $ Handle Errors $

# try:
#     foober
# except:
#     print("PROBLEM!!")
# print("after the try")

# d = {"name": "Ricky"}
# def get(d,key):
#     try:
#         return d[key]
#     except KeyError:
#         return None 
# print(get(d,"name"))

# -----------------------------------------------------------------------------------------------------

# $ Try, Except, Else and Finally $

# try:
#     num = int(input("enter a number: ")) 
# except:
#     print("that's not a number")
# else:
#     print("In else")
# finally:
#     print("Runs no matter what")

# while True: # using them in a guessing game
#     try:
#         num = int(input("enter a number: ")) 
#     except:
#         print("that's not a number")
#     else:
#         print("correct")
#         break
#     finally:
#         print("Runs no matter what")

# def divide(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("don't divide by zero")
#     except TypeError as err:
#         print("a and b must be numbers") # you can write both "except" in a single line, using tuple
#         print(err)
#     else:
#         print(f"{a} divided by {b} is {result}")
# divide(1,2)
# divide(1,0)
# divide(1,"q")

# ---------------------------------------------------------------------------------------------

# $ Modules $

# -Built-in Modules

# import random
# print(random.choice(["banana", "tomato","orange","mango"])) # choice is method in random
# print(random.shuffle(["banana", "tomato","orange","mango"])) # shuffle is method too

# import random as rand # sometimes, you import long-named module, you can give it alias using "as"
# print(rand.choice(["banana", "tomato","orange","mango"])) # then you refer to the alias "rand"
# print(rand.shuffle(["banana", "tomato","orange","mango"]))

# from random import choice, randint # use "from" to import parts of a module
# print(choice(["banana", "tomato","orange","mango"]))  # random is no longer a thing in this file, so delete it and use the function only
# print(randint(1,10))  # random is no longer a thing in this file, so delete it and use the function only
# print(shuffle(["banana", "tomato","orange","mango"])) # using shuffle gives error, cus it wasn't imported

# from random import choice as c, randint as magic_num # import parts of the module and give it alias
# print(c(["banana", "tomato","orange","mango"])) 
# print(magic_num(1,10)) 

# ----------------------------------------------------------------------------------------------------------

# -External Modules # modules that downloaded from the internet, see "pypi.python.org"

# import termcolor # make sure you download it first, open terminal, run "python3 -m pip install termcolor"
# text = termcolor.colored("Hallo World!", color="magenta", on_color="on_cyan", attrs=["blink"])
# print(text)

# -----------------------------------------------------------------------------------------

# starting from here, empty line doesn't mean end of example, some empty lines used between functions, so be careful on uncommenting

# $ Object Oriented Programming OOP $

# Defining the simplest possible class
# class User:
#     pass
# user1 = User()
# print(user1)
# print(type(user1))

# class User:
#     def __init__(self): # almost every time you need to define __init__ method in a class 
#         print("A new user has been made") # you don't usualy print here, but you add your data, print here to illustrate the functionality

# user1 = User() # __init__ method is called automatically when creating object from class
# user2 = User()
# user3 = User()

# class User:
#     def __init__(self, first):
#         self.name = first
# user1 = User("Joe")
# user2 = User("Peter")
# print(user1.name) # to access specific attribute of instance, run: instance.attribute_name

# class User:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
# user1 = User("Joe", "Barton", 30)
# user2 = User("Peter", "Parker", 40)
# print(user1.age, user1.first)
# print(user1.first, user1.last)

# ------------------------------------------------------------------------------------

# $ Underscores "Dunder" methods, Name Mangling $

# class person:
#     def __init__(self):
#         self.name = "Joe"
#         self._secret = "Use this only inside the class" # private convention, this should be private
#         self.__msg = "ordinary msg!" # Name Mangling

# p = person()
# print(p.name)
# print(p._secret)
# # print(p.__msg) # AttributeError!! cuz double underscore attributes stores as "_ClassName__AttributeName"
# print(p._person__msg) # the correct way to call __attribute
# print(dir(p)) # this print all the methods and attributes of a class

# ---------------------------------------------------------------------------------------------

# $ Instance Methods $

# class person:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

#     def full_name(self): # its an ordinary function, but inside a class its called "Method" 
#         return f"{self.first} {self.last}"

#     def initails(self):
#         return f"{self.first[0].upper()}.{self.last[0].upper()}."

#     def hobby(self, hobby): # method can have other parameters with alongside self
#         return f"{self.first} likes {hobby}"

#     def is_senior(self):
#         if self.age >= 65:
#             return "Is Senior"
#         return "Not Senior"

#     def birthday(self):
#         self.age += 1 
#         return f"Happy {self.age}th {self.first}"

# p1 = person("ahmed", "yousif", 70)
# p2 = person("John", "Doe", 30)
# print(p1.full_name())
# print(p1.initails())
# print(p1.hobby("football"))
# print(p1.is_senior())
# print(p1.birthday())
# print(p2.full_name())
# print(p2.initails())
# print(p2.is_senior())
# print(p2.birthday())

# --------------------------------------------------------------------------------------------

# $ Class Attributes $

# class User:
#     active_users = 0 # class attribute 

#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         User.active_users += 1 # every time a user created, add 1 to active_users

#     def log_out(self):
#         User.active_users -= 1
#         return f"{self.first} has logged out"

#     def full_name(self):
#         return f"{self.first} {self.last}"

#     def initails(self):
#         return f"{self.first[0].upper()}.{self.last[0].upper()}."

#     def hobby(self, hobby):
#         return f"{self.first} likes {hobby}"

#     def is_senior(self):
#         if self.age >= 65:
#             return "Is Senior"
#         return "Not Senior"

#     def birthday(self):
#         self.age += 1 
#         return f"Happy {self.age}th {self.first}"

# print(User.active_users) # 0
# user1 = User("ahmed", "yousif", 70) # first user created
# user2 = User("John", "Doe", 30) # second user created
# print(User.active_users) # 2 active users now
# print(user2.log_out())
# print(User.active_users) # 1 active users cus user2 logged out

# class Pet:
#     allowed = ["Cat", "Dog", "Fish", "Rat"] # a list of allowed pets

#     def __init__(self, name, species):
#         if species not in Pet.allowed:
#             raise ValueError(f"You can't have a {species} pet!")
#         self.name = name
#         self.species = species

#     def set_species(self,species):
#         if species not in Pet.allowed: # by using "allowed" as class attribute, you don't need to define it in every method, use it directly
#             raise ValueError(f"You can't have a {species} pet!")
#         self.species = species

# cat = Pet("Blue", "Cat")
# dog = Pet("Wyatt", "Dog")
# # tiger = Pet("Tony", "Tiger") # ValueError
# # cat.set_species("Lion") # ValueError cuz Lion not in allowed
# cat.set_species("Fish")
# print(cat.species) # cat now is a fish
# print(Pet.allowed)
# Pet.allowed.append("Pig") 
# print(Pet.allowed) # the list is updated in every instance

# ---------------------------------------------------------------------------------------------------

# $ Class Methods $ # signify that what will work inside the method is not instance, it's a class

# class User:
#     active_users = 0
#  
#     @classmethod # use "@classmethod" to create class method, 
#     def display_active_user(cls): # self here doesn't matter, you can use "cls" for class
#         print(cls) # just to see what is cls
#         return f"there are currently {cls.active_users} active users"

#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         User.active_users += 1

#     def log_out(self):
#         User.active_users -= 1
#         return f"{self.first} has logged out"

#     def full_name(self):
#         return f"{self.first} {self.last}"

#     def initails(self):
#         return f"{self.first[0].upper()}.{self.last[0].upper()}."

#     def hobby(self, hobby):
#         return f"{self.first} likes {hobby}"

#     def is_senior(self):
#         if self.age >= 65:
#             return "Is Senior"
#         return "Not Senior"

#     def birthday(self):
#         self.age += 1 
#         return f"Happy {self.age}th {self.first}"

# user1 = User("Joe", "Mark", 30)
# print(User.display_active_user()) # you can use class name, cus @classmethod has nothing to do with instance
# print(user1.display_active_user()) # you can still use it with instance

# -advanced example

# class User:
#     active_users = 0 
#     @classmethod
#     def display_active_user(cls):
#         return f"there are currently {cls.active_users} active users"

#     @classmethod 
#     def from_string(cls, data_str):
#         first,last,age = data_str.split(",") # sometimes you deal with comma separated data, you need to handle it first before you create instance
#         return cls(first, last, int(age))

#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         User.active_users += 1

#     def log_out(self):
#         User.active_users -= 1
#         return f"{self.first} has logged out"

#     def full_name(self):
#         return f"{self.first} {self.last}"

#     def __repr__(self): # the instance representation method
#         return f"{self.first}"

#     def initails(self):
#         return f"{self.first[0].upper()}.{self.last[0].upper()}."

#     def hobby(self, hobby):
#         return f"{self.first} likes {hobby}"

#     def is_senior(self):
#         if self.age >= 65:
#             return "Is Senior"
#         return "Not Senior"

#     def birthday(self):
#         self.age += 1 
#         return f"Happy {self.age}th {self.first}"

# joe = User.from_string("Joe,Mark,30") # passing arguments as one string separated by comma, not as 3 arguments "check it again"
# print(joe.first)
# print(joe.last)
# print(joe.age)
# print(joe.full_name())
# print(joe)

# ----------------------------------------------------------------------------------

# Deck Of Cards Exercise

# ------------------------------------------------------------------------------------

# $ Inheritance $

# class Animal:
#     cool = True

#     def make_sound(self, sound):
#         return f"this animal says {sound}"

# class Cat(Animal): # telling python this Cat class inherits the Animal class
#     pass

# c = Cat()
# print(c.make_sound("graaoo")) # even if c is instance from Cat, but still can access methods of Animal class
# print(c.cool)
# print(isinstance(c, Cat)) # isinstance is a built in method that returns True or False, it tells if a method is instance of the class or not

# --------------------------------------------------------------------------------------------

# $ Properties $

# class Human:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self._age = age # underscore to show it's a private
    
#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self, value):
#         if value >= 0:
#             self._age = value
#         else:
#             raise ValueError("Age must not be negative!")
    
#     @property
#     def full_name(self):
#         return f"{self.first} {self.last}"
    
#     @full_name.setter
#     def full_name(self, name):
#         self.first, self.last = name.split(" ")
    
# jane = Human("Jane", "William", 40)
# print(jane.age) # notice, parentheses weren't used "jane.age()" even though we called a method, this is the property
# # jane.age = -40 # setting a negative value to age, using age.setter property.. should raise error
# # print(jane.age)
# print(jane.full_name)
# jane.full_name = "Jack Norman"
# print(jane.full_name) 
# print(jane.__dict__)

# --------------------------------------------------------------------------------------------

# $ Introduction to super() $

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
    
#     def __repr__(self):
#         return f"{self.name} is a {self.species}"

#     def make_sound(self, sound):
#         return f"this animal says {sound}"

# class Cat(Animal):
#     def __init__(self, name, breed, toy):
#         super().__init__(name, species = "Cat") # super refers to base class "parent class",, here, super refers to Animal class, so we dont need to add self.name in the subclass
#         self.breed = breed
#         self.toy = toy
    
#     def play(self):
#         return f"{self.name} plays with {self.toy}"

# class Dog(Animal):
#     def __init__(self, name, breed, toy):
#         super().__init__(name, species = "Dog") # here, we specified that every dog instance its species is "Dog"
#         self.breed = breed
#         self.toy = toy

# c = Cat("Blue", "Scottish", "String")
# print(c.__repr__())
# print(c.play())
# d = Dog("Wyatt", "German", "String")
# print(d.__repr__())

# -another example

# class User:
#     active_users = 0 

#     @classmethod
#     def display_active_user(cls):
#         return f"there are currently {cls.active_users} active users"

#     @classmethod 
#     def from_string(cls, data_str):
#         first,last,age = data_str.split(",")
#         return cls(first, last, int(age))

#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         User.active_users += 1

#     def log_out(self):
#         User.active_users -= 1
#         return f"{self.first} has logged out"

#     def full_name(self):
#         return f"{self.first} {self.last}"

#     def __repr__(self): 
#         return f"{self.first}"

#     def initails(self):
#         return f"{self.first[0].upper()}.{self.last[0].upper()}."

#     def hobby(self, hobby):
#         return f"{self.first} likes {hobby}"

#     def is_senior(self):
#         if self.age >= 65:
#             return "Is Senior"
#         return "Not Senior"

#     def birthday(self):
#         self.age += 1 
#         return f"Happy {self.age}th {self.first}"

# class Moderator(User):
#     total_mods = 0

#     @classmethod
#     def display_active_moderators(cls): # to see the total moderators
#         return f"currantly {Moderator.total_mods} active moderators"

#     def __init__(self, first, last, age, community):
#         super().__init__(first, last, age)
#         self.community = community
#         Moderator.total_mods += 1 # adding active moderator in every instance creation
    
#     def remove_post(self):
#         return f"{self.full_name()} removed post from {self.community} community"

# class Visitor(User):
#     def __init__(self, first, last, age, community):
#         super().__init__(first, last, age)
#         self.community = community

# print(User.display_active_user()) # 0, no user yet
# print(Moderator.display_active_moderators()) # 0
# joe = Moderator("Joe", "Mark", 30, "Football")
# print(User.display_active_user()) # 1, new user created
# print(Moderator.display_active_moderators()) # 1, cus new moderator was created
# print(joe.community)
# print(joe.remove_post())
# alex = Visitor("Alex", "Sancliar", 40, "Football")
# print(User.display_active_user()) # 2, another user created
# print(Moderator.display_active_moderators()) # 1, still 1 cuz alex is not a moderator
# print(alex.community)
# print(alex.remove_post()) # AttributeError, cus alex is website visitor who cant remove anything

# --------------------------------------------------------------------------------------------------

# $ Multiple Inheritance $

# class Aquatic:
#     def __init__(self,name):
#         print("AQUATIC INIT!")
#         self.name = name

#     def swim(self):
#         return f"{self.name} is swimming"

#     def greet(self):
#         return f"I am {self.name} of the sea!"

# class Ambulatory:
#     def __init__(self,name):
#         print("AMBULATORY INIT!")
#         self.name = name

#     def walk(self):
#         return f"{self.name} is walking"

#     def greet(self):
#         return f"I am {self.name} of the land!"

# class Penguin(Ambulatory, Aquatic): # inherits both class
#     def __init__(self,name):
#         print("PENGUIN INIT!")
#         Ambulatory.__init__(self,name=name)
#         Aquatic.__init__(self, name=name)

# jaws = Aquatic("Jaw")
# lassie = Ambulatory("Lassie")
# peni = Penguin("Peni")
# print(peni.swim()) # from Aquatic class
# print(peni.walk()) # from Ambulatory class
# print(peni.greet()) # greet is in both class, which one to be called!?
# print(f"Peni is instance of Aquatic: {isinstance(peni, Aquatic)}")
# print(f"Peni is instance of Ambulatory: {isinstance(peni, Ambulatory)}")
# print(f"Peni is instance of Penguin: {isinstance(peni, Penguin)}")

# ------------------------------------------------------------------------------------

# $ Method Resolution Order (MRO) $

# class A:
#     def do_something(self):
#         return "Do something in: A"

# class B(A):
#     def do_something(self):
#         return "Do something in: B"

# class C(A):
#     def do_something(self):
#         return "Do something in: C"

# class D(B,C):
#     pass

# d = D()
# print(d.do_something()) # which do_something will be called!?
# # print(D.__mro__) # the order of inheritance 
# # print(D.mro()) # second way to show the order
# # help(D) # third way to show the order

# --------------------------------------------------------------------------------------------

# $ Polymorphism $

# class Animal:
#     def speak(self):
#         raise NotImplementedError ("Subclass needs to implement this method") # forcing every class to have it's own speak method

# class Dog(Animal):
#     def speak(self):
#         return "woof"

# class Cat(Animal):
#     def speak(self):
#         return "Mewo"

# class Fish(Animal):
#     pass

# d = Dog()
# print(d.speak()) # works fine
# f = Fish()
# print(f.speak()) # notice, speak wasn't defined in Fish class, so will go to Animal speak()

# ---------------------------------------------------------------------------------------------

#  $ Special Methods "__magic__ methods" $

# class Human:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

#     def __repr__(self):
#         return f"Human is {self.first} {self.last}"

#     def __len__(self): 
#         return self.age # len() now returns the age of human

#     def __add__(self, other): # you can change the behaviour of normal addition
#         if isinstance(other, Human): # check if other is instance of Human class
#             return Human(first="Newborn", last=self.last, age=0)
#         return "You can't add this!"
    
#     def __mul__(self,other): # changing the behaviour of multiplication
#         if isinstance(other, int): # check if other is integer
#             return [self for i in range(other)] 
#         return "Can't multiply"
        
# mount = Human("Mason", "Mount", 21)
# tomori = Human("Fikayo", "Tomori", 22)
# print(mount)
# print(len(mount))
# print(mount + tomori)
# print(mount + 2) # + sign will look for __add__
# print(mount * 2) # * sign will look for __mul__

# --------------------------------------------------------------------------------------

