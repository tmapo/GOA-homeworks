#task num 1

#in the first task we need to ask the user for their name, but before we print it out we need to add a space between each letter
name = input("enter your name: ")

res = " "

for letter in name:
    res += letter + " "
    print(res) 

#done!

print("///")

#task num 2

#in the second task, we will ask our user for a specific range of numbers. after that we need to write a code, which will only print the numbers that we can get using 2 and 3.

range0 = int(input("enter a specific range to a number: "))

#for the number 2
print("for number 2")
for num in range(0 , range0 , +2 ) : 
    print(num)

#for the number 3
print("for number 3")
for num in range(0 , range0 , +3 ) : 
    print(num)

#done!

print("///")

#task num 3

#in the third task, we should create a variable "result". after that, using the for loop function we will ask the user for 5 different numbers and get an average number from them.

result = 0

for i in range(5):
    num = int(input("input a number: "))
    result += num
result = result / 5
print(result)

#ask guram

print("///")

#task num 4

#now  we need to select a range from -100 to 100, but only print positive numbers

for i in range(-100 , 100):
    if i>0 :
      print(i)

#done!

print("///")

#task num 5

#in this task, we need to force the user to enter a negative number.

result = 0

num = int(input("Please input a negative number: "))

while num >= 0:
    num = int(input("Please input a negative number: "))

print("Congrats! You inputted a negative number: ")

#done! 
print("///")

#homework wasn't yet completed!
print("homework wasn't yet comleted!")