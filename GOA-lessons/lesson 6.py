#task num 1

#using the input() command we should make a program, which will calculate users age, by current year and their birth year

current_year = 2024
birth_year = int(input("enter your bith year: "))
your_age = str(current_year - birth_year )
print("you are "  + your_age + " years old")

#done!

print("///")

#task num 2

#we should use variables and input() command, to ask the user about ractangle's length and height, then try to find P and S

length = int(input("enter ractangle's length: "))
height = int(input("enter ractangle's height: "))
p = str((length + height) * 2)
s = str(length * height) 
print("rectangle's P = " + p ) 
print("rectangle's S = " + s )

#done!

print("///")

#task num 3

#let's ask the user then distance, between their own house and their school in km, and then print the same distance in m,cm

distance = int(input("enter the distance between your home and your school in km: "))
km = str(distance) 
m = str(distance * 1000)
cm = str(distance * 100000)
print(" the distance in km = " + km)
print(" the distance in m = " + m)
print(" the distance in cm = " + cm)

#done!

print("///")

#task num 4

#lets collect users info! we should ask them their mame/surename , their parents name/surename , their favorite car brand (ps - hummer) , 3 of their favorite colors and a hobby. after that we will print it
name_surename = input("enter your name & surename : ")
dads_name_surename = input("enter your dad's name & surename : ")
moms_name_surename = input("enter your mom's name & surename : ")
fav_car = input("enter your favorite car brand : ")
colors = input("enter 3 colors you like the most : ")
hobby = input("enter your hobby : ")
print("Hey! my name is " + name_surename + " , my mom is " + moms_name_surename + " and my dad is " + dads_name_surename + ". my favorite car brand is " + fav_car + ", great pick, huh?. i have 3 favorite colors: " + colors + ". my hobby is " + hobby + ". i hope you find me interesting <3")

#done!

print("///")

#homework was completed successfully.
print("homework was completed successfully.")