while True:
    try:
        a = int(input('Enter the first number : '))
        b = int(input('Enter the second number : '))
        c = input(f'What operation do you wanna perform with {a} and {b}: ')
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
                print('Enter the valid arithmetic operator.')
                continue
        d = input('Do you want to continue? : ')
        if d != 'yes':
            print('Hope we will meet again, have a nice day :)')
            break
    except:
        print('Enter the valid numbers.')
        continue
