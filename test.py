#n = int(input('Add number:'))
#sum = 0 

#for i in range (1, n+1):
#    sum += 1
#print('sum yours numbers', n, 'natural numbers',sum)
#----------------------------------------------------
#for number in range (1,11):
#    print(number)
#----------------------------------------------------
#sum = 0 
#for number in range (1,101):
#    sum += number
#    print ('Сума чисел від 1 до 100', sum)
#----------------------------------------------------
#for numb in range (1,6):
#    S = numb * numb
#    print('квадрат',numb ,'дорівнбює',S)
#----------------------------------------------------
#def add_numbers():
#    num1 = float (input('Ввкдіть число: '))
#    num2 = float (input('Ввкдіть число: '))
#    sum = num1 + num2
#    print ('Сума чисел:',sum)
#add_numbers()
#----------------------------------------------------
#def string_length():
#    user_input = input('Введіть число:')
#    lenght = len (user_input)
#    return lenght
#string_length = string_length()
#print('Довжина рядка: ',string_length)
#----------------------------------------------------
def is_even (number):
    if number % 2 == 0:
        return True
    else:
        return False
user_number = int(input('Введіть число: '))
if is_even(user_number):
    print('Число є парним: ')
else:
    print('Число є не парним: ')
