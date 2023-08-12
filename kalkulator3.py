
def calculator ():
    print ('Select an option:')
    print ('addition')
    print('subtraction')
    print('multiplication')
    print('division')
    choise = input ('Your choice: (1/2/3/4) :')
    num1 = float(input('Enter the first number:'))
    num2 = float(input('Enter the second number:'))
    if choise == '1':
        result = num1 + num2
    elif choise == '2':
        result = num1 - num2
    elif choise == '3':
        result = num1 * num2
    elif choise == '4':
        if num2 !=0:
            result = num1 / num2
        else:
            print('Division by 0 is impossible')
            return
    else:
        print('wrong choice')
        return
    print('Result:',result)
calculator()
    