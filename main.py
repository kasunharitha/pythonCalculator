#simple calculator using python

num1 = input("Enter number: ")
num2 = input("Enter number: ")

num1=int(num1)
num2=int(num2)

operation = input("Enter operation: +,-,/,* ")

if operation=="+":
    print(num1+num2)
elif operation=="-":
    print(num1-num2)
elif operation=="*":
    print(num1*num2)
elif operation=="/":
    print(num1/num2)
