print("Hello World")
print("\n")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")
print("\n")

print("Working with variables")
character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")
print("\n")

print("Working with strings")
phrase = "We Love Bug"
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("W"))
print(phrase.index("Lov"))
print(phrase.replace("We","You"))
print("\n")

print("Working with numbers")
print(-2.0987) #-2.0987
print(3 + 4.5) #7.5
print(3 * 4 + 5) #17
print(10 % 3) #1
my_num = 5
print(str(my_num) + " is my favorite number")
my_num = -5
print(abs(my_num)) #5
print(pow(3, 2)) #9
print(max(4, 6)) #6
print(min(4, 6)) #4
print(round(3.2)) #3
print(round(3.7)) #4

from math import *
print(floor(3.7)) #3
print(ceil(3.7)) #4
print(sqrt(36)) #6.0
print("\n")

#getting input from user
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)
# print("\n")

#build a basic calculator
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)

#madlibs game
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
#
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)
# print("\n")

#Lists
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends) # ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']
print(friends[0]) # Kevin
print(friends[-1]) # Toby
print(friends[1:3]) # [ 'Karen', 'Jim']
print(friends[1:]) # [ 'Karen', 'Jim', 'Oscar', 'Toby']
friends[1] = "Mike"
print(friends[1]) # Mike











