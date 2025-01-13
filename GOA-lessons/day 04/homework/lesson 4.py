#task num 1

# the task is to create three variables, using the input() command. with these variables we should use either one of + - * / ** // to make math problems

num1 = int(input("enter first number:"))
math_operator = input("enter a mathematical operator:")
num2 = int(input("enter the second number:"))

#variables are done, now lets create a simple code to build a calculator-like program


if math_operator == "+" :
    result = print(num1 + num2)

elif math_operator == "-" : 
    result = print(num1 - num2)

elif math_operator == "*" :
    result = print(num1 * num2)

elif math_operator == "/" :
    result = print(num1 / num2)

elif math_operator == "**" : 
    result = print(num1 ** num2)

elif math_operator == "//" :
    result = print(num1 // num2)

else :
    result = print("invalid operator!") 

#the code is done, we successfully assembled a calculator :)

print("///")

#task num 2

#using the input() command we should create a program, which will make us enter our name and age, after that it will print both of them

name = input("enter your name: ")
age = input("enter your age: ")

#nice! we created two varaibles and stored the input() command in it with a question

print("your name is " + name + " and you are " + age + " years old.")

#the terminal will ask us to enter our information to then print, or use other commands on them
#done!

print("///")

#task num 3

#we learned that a variables can be updated several times, let prove that!

points = "50"
print("you have " + points + " points!")

print("you lost one game!(-16 points!)")

points = "34"
print("now you have " + points +" points.")

print("you won two games!(+ 43 points)")

points = "76"
print("now you have " + points + " points!")

#done!

print("///")

#task num 4

#using variables, we should create a program which will calculate our current age

birth_year = int(input("enter your bith year: "))
current_year = int(input("enter current year: "))

print("you are", current_year - birth_year , "years old!")

#done!

print("///")

#homework was completed successfully.
print("homework was completed successfully.")