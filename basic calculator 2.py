a = int(input("Enter the first number : "))
b = int(input('Enter the second number : '))
c = input("Enter the arithmetic operation you want to perform : ")
match c :
    case '+':
        print("Addition of",a,"and",b,"is",a+b)
    case '-':
        print("Substraction of",a,"and",b,"is",a-b)
    case '*':
        print("Multiplication of",a,"and",b,"is",a*b)
    case '/':
        if b == 0:
            print("Denominator cannot be zero")
        else:
            print("Division of",a,"and",b,"is",a/b)
    case '**':
        print("Exponential of",a,"and",b,"is",a**b)
    case '//':
        print("Floor division of",a,"and",b,"is",a//b)
    case '%':
        print("Modulo of",a,"and",b,"is",a%b)
    case _:
        print("Enter a valid arithmetic operation.")
    