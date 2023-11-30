
while True:
    num1 = input("Enter Your First Number: ")
    if num1.isdigit():
        num1=int(num1)
        break
    else:
        print("Please enter a valid number!!")
        
while True:
    num2 = input("Enter Your Second Number: ")
    if num2.isdigit():
         
        num2 = int(num2)
        break
    else:
        print("Please enter a valid number!!")
        
while True:
    op = input("Choose Your Operator (+, *, /, -): ")
    if op in ["+","*","/","-"]:
        break
    else:
        print("Please provide a valid operator!!")


if op == "+":
    result = num1 + num2
    print("The Answer is:", result)
elif op == "-":
    result = num1 - num2
    print("The Answer is:", result)
elif op == "/":
    if num2 == 0:
        print("Cannot divide by zero!!")
    else:
        result = num1 / num2
        print("The Answer is:", result)
elif op == "*":
    result = num1 * num2
    print("The Answer is:", result)

