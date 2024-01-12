from math import *
import useful_tools
import docx

# name = "Ryan Parsa Allahyari"
# age = 10
# print("There once was a good boy named " + name + ", ")
# print("he was " + str(age) + " years old.")
# print("He really liked the name " + name + ", ")
# print("but didn't like being " + str(age) + ".")
#
# print("     /\\")
# print("    /  \\")
# print("   /    \\")
# print("  /      \\")
# print(" /________\\")
#
# print(name.upper().isupper())
# print(len(name))
# print(name.lower().count("a"))
# print(name.find("y"))
# print(name[7])
# numero = (name.index("A"))
# print(numero)
# print(name.replace("A","O"))
#
# adad = 666.6
# other = -222
# print(adad + other)
# print(adad.__ceil__())
# print(other.__abs__())
# print(other.__abs__()+adad.__ceil__())
# print(pow(4,3))
# print(max(15, 19))
# print(round(124.4))
# print(floor(3.7))
# print(adad.__floor__())
# print(sqrt(25))
# print(16**(1/4))

# my_name = input("Enter your name here: ")
# my_age = input("Enter your age: ")
# print("Hello " + my_name + "! You are " + my_age + " years old.")

# print(" ❤️ Calculator ❤️")
# num1 = float(input("enter the first number here: "))
# num2 = float(input("enter the second number here: "))
# sum_of = num1 + num2
# print(sum_of)

# print(" ❤️ Mad Libs Game ❤️")
# color = input("what is your favorite color? ")
# flower = input("what is your favorite flower? ")
# celebrity = input("who is your favorite celebrity? ")
# print("Roses are " + color + ", \n" + flower + "s are blue, \nI love " + celebrity + ".")

# print(" ❤️ Lists and Lists functions ❤️ ")
# friends = ["jim" , "sam" , "kary" , "mark" , "mark" , "mark" , "viola" , "sundee"]
# friends2 = friends.copy()
# friends.sort()
# print(friends)
# lucky_numbers =[16, 18, 20, 21, 4, 25]
# lucky_numbers.sort()
# print(lucky_numbers)
# friends.extend(lucky_numbers)
# friends.append("matt")
# friends.insert(2, "mary")
# friends.remove("jim")
# print(friends.__contains__("matt"))
# friends.pop()
# print(friends.__contains__("kary"))
# print(friends.index("mark"))
# friends.reverse()
# print(friends)
# print(friends.__contains__("matt"))
# print(friends.count("mark"))
# print(friends2)

# print(" ❤️ Tuples ❤️  Tuples are immutable.")
# data = (2, 4, 6, 8, 10)
# print(data)

# print(" ❤️ Functions ❤️")
# def sayHi(host):
#     name = input("What is your name? ")
#     print("Hello " + name + " from " + host +"!")
# sayHi("Python")
# sayHi("JavaScript")

# def cube(num):
#     return num*num*num
# result = cube(6)
# print(result)

# print(" ❤️ IF Statements ❤️")
# is_male = False
# is_tall = True
# if is_male and is_tall:
#     print("you are a tall man.")
# elif is_male and not is_tall:
#     print("you are a short man.")
# elif not is_male and is_tall:
#     print("you are a tall woman.")
# else:
#     print("you are a short woman.")

# print(" ❤️ IF Statements and Comparison variables ❤️")
# def max(num1, num2, num3):
#     if num1>num2 and num1>num3:
#         return num1
#     elif num2>num1 and num2>num3:
#         return num2
#     else:
#         return num3
#
# print(max(3, 5, 1))

# print(" ❤️ Building a better calculator ❤️")
# num1 = float(input("enter first number: "))
# op = input("enter operator: ")
# num2 = float(input("enter second number: "))
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op =="/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("invalid operator")

# print(" ❤️ Dictionaries in Python ❤️")
# months_dict = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "October",
#     11: "November",
#     12: "December"
# }
# print(months_dict["Jan"])
# print(months_dict["Feb"])
# print(months_dict.get("Dec"))
# print(months_dict.get(5))

# print(" ❤️ While Loop ❤️")
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("Done with loop!")

# print(" ❤️ Guessing Game ❤️")
# secret_word = "giraffe"
# guess = ""
# i=1
# while i<=3:
#     guess = str(input("guess a word: "))
#     if guess == secret_word:
#         print("success")
#         break
#     i += 1
# if i > 3:
#     print("Sorry you are out of guess.")

# print(" ❤️ For Loops ❤️")
# for letter in "Ryan Allahyeri":
#     print(letter.upper())
#
# friends = ["Ryan","Jack","Suzzie","Mark"]
# for friend in friends:
#     print(friend)
#
# for i in range(len(friends)-1):
#     print(friends[i])

# print(" ❤️ Exponent Function ❤️")
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for i in range(pow_num):
#         result = result * base_num
#     return result
# print(raise_to_power(3, 5))

# print(" ❤️ 2D Lists and Nested Loops ❤️")
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
# for row in number_grid:
#     for col in row:
#         print(col)

# print(" ❤️ Build a Translator ❤️")
# vowels = ["a", "e", "i" , "o", "u"]
# def translation(word):
#     translated = ""
#     for letter in word:
#         if letter.lower() in vowels:
#             if letter.isupper():
#                 translated = translated + "G"
#             else:
#                 translated = translated + "g"
#         else:
#             translated = translated + letter
#     return translated
# print(translation("Ryan Allahyari"))

# print(" ❤️ Try Except ❤️")
# try:
    # value = 10/0
#     number = int(input("Enter a number "))
#     print(number)
# except ZeroDivisionError:
#     print("invalid, Divided by zero")
# except ValueError:
#     print("invalid input")

# print(" ❤️ Reading Files ❤️")
# employee_file = open("employees.txt" , "r")
# print("r for read")
# print("w for write aka overwrite")
# print("a for append")
# print("r+ for read & write")
# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readlines()[3])
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()

# print(" ❤️ Writing to Files ❤️")
# employee_file = open("employees.txt" , "a")
# employee_file.write("\nNikka - Human resources")
# employee_file.close()
#
# employee_file = open("employees1.txt" , "w")
# employee_file.write("\n Zhina - Customer Service")
# employee_file.write("\n Shadmehr - Human resources")
# employee_file.close()

# print(" ❤️ Modules and Pip ❤️")
# print(useful_tools.Roll_Dice(6))
# print(useful_tools.Feet_in_Mile)
# print(useful_tools.Meters_in_Kilometer)
# print(useful_tools.Get_File_ext("employees1.txt"))

# print(" ❤️ Python Data Type: Class ❤️")
# # class in student.py
# from Student import Student
# student1 = Student("Ryan", "Medicine", 2.8, False)
# student2 = Student("Parisa", "Pharmacy", 4.0, False)
# print(student1.name)
# print(student1.gpa)
# print(student2.major)
# print(student2.is_on_probation)
# print(student1.on_honor_roll())


# print(" ❤️ Building a Multiple Choice Quiz ❤️")
# from Question import Question
# prompts = [
# "Who killed King Joffrey Baratheon during the Purple Wedding?\n(a) Sansa Stark\n(b) Tyrion Lannister\n(c) Olenna Tyrell\n(d) Littlefinger\n\n",
# "What is the ancestral home of House Stark?\n(a) Casterly Rock\n(b) Riverrun\n(c) Winterfell\n(d) Dragonstone\n\n",
# "Which character is known for saying, 'Chaos is a ladder'?\n(a) Varys\n(b) Tywin Lannister\n(c) Petyr Baelish (Littlefinger)\n(d) Cersei Lannister\n\n",
# "What is the primary religion in the city of Braavos?\n(a) The Old Gods\n(b) The Drowned God\n(c) The Lord of Light (R'hllor)\n(d)The Many-Faced God\n\n",
# "Which House uses the motto 'Fire and Blood'?\n(a) House Targaryen\n(b) House Stark\n(c) House Lannister\n(d) House Greyjoy\n\n",
# "Who becomes the Night King in Game of Thrones?\n(a) Bran Stark\n(b) Jon Snow\n(c) Theon Greyjoy\n(d) The Night King was not a human before.\n\n",
# ]
#
# test_questions =[
#     Question(prompts[0], "c"),
#     Question(prompts[1], "c"),
#     Question(prompts[2], "c"),
#     Question(prompts[3], "c"),
#     Question(prompts[4], "a"),
#     Question(prompts[5], "b"),
# ]
#
# def test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print("you got " + str(score) + " out of " + str(len(questions)))
#
# print(test(test_questions))

# print(" ❤️ Inheritance ❤️")
# from Chef import Chef
# from ChineseChef import ChineseChef
# myChef = Chef()
# myChef.make_salad()
# myChineseChef = ChineseChef()
# myChineseChef.make_fried_rice()
# myChineseChef.make_salad()
# myChineseChef.make_special_dish()

print(" ❤️   Python Interpreter ❤️")

















