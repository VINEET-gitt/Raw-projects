while True:
    try:
        first_num = int(input('Enter the first number : '))
        second_num = int(input('Enter the second number : '))
        opt = input(f'What operation do you wanna perform with {first_num} and {second_num}: ')
        match opt :
            case '+':
                print(f"Addition of {first_num} and {second_num} is {first_num+second_num}.")
            case '-':
                print(f"Subtraction of {first_num} and {second_num} is {first_num-second_num}")
            case '*':
                print(f"Multiplication of {first_num} and {second_num} is {first_num*second_num}.")
            case '/':
                if second_num == 0:
                    print(f"Denominator cannot be zero")
                else:
                    print(f"Division of {first_num} and {second_num} is {first_num/second_num}.")
            case '**':
                print(f"Exponential of {first_num} and {second_num} is {first_num**second_num}.")
            case '//':
                print(f"Floor division of {first_num} and {second_num} is {first_num//second_num}.")
            case '%':
                print(f"Modulo of {first_num} and {second_num} is {first_num%second_num}.")
            case _:
                print('Enter the valid arithmetic operator.')
                continue
        user_exit1 = input('Do you want to continue? : ')
        user_exit2 = user_exit1.capitalize()
        if user_exit2.startswith('Y'):
            continue
        else:
            print('Hope we will meet again, have a nice day :)')
            break
    except ValueError:
        print('Enter the correct integer value.')
        continue
