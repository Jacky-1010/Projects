num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
opt=input("Select the Operation(+,-,*,/):")
match opt:
    case '+':
        print(num1,"+",num2,"=",num1+num2)
    case '-':
        print(num1,"-",num2,"=",num1-num2)
    case '*':
        print(num1,"*",num2,"=",num1*num2)
    case '/':
        print(num1,"/",num2,"=",num1/num2)
    case _:
        print("Invalid Input")
