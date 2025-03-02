print("Mini Calculator")

num1 = int(input())
operator = input()
num2 = int(input())

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2 if num2 != 0 else "Error")