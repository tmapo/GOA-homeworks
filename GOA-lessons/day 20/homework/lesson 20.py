
#task num 1

# in this task we should create a random list of letters and only print out vowels

arr = ["a" , "g" , "s" , "i"]

vowels = ["a" , "e" , "i" , "o" , "u"]  

for letter in arr:
    if letter in vowels:
        print(arr)

#done!
    
print("///")

#task num 2

# in this task we should create a list and only print numbers which are resulted after multypling 5 or 3

arr = [25 ,  57 , 40 , 9 , 11 , 68]

for num in arr:
    if num % 5 == 0 or num % 3 == 0:
        print(num)

#done!

print("///")

#task num 3

# in this task we should create arr = [] with random numbers and words and print out every one of them together in one string

arr = str([ 2 , " arwori " , 6 , " mgetvi " , 10 , " zviangi " , "," , " da " , "me vnaxe " ])

print(arr[8] , arr[4] , arr[3] , arr[6] ,  arr[2] , arr[1] , arr[7] , arr[5])

#done!

print("///")

#task num 4

# in this task, we should create a specific shape:
 #******
  #******
   #******
    #******

for i in range(4):
    print(" " * i + "*" * 6)

#done!

print("///")

#task num 5

# in this task we should ask out user if they are age of 12+ or 12-, if they are we should print out "you aren't 12 years old" 

users_age = int(input("enter your age: "))

if users_age == 12 :
    print("you are 12!")
elif users_age > 12 :
    print("you are older than the age 12!")
else:
    print("you are younger than the age 12!")

#done!

print("///")

#homework was completed successfully.
print("homework was completed successfully.")