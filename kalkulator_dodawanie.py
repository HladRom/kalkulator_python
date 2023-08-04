print ('Введіть данні:')
A = int(input('Введи числа:'))
C = input('Введи дію:')
B = int(input('Введи числа:'))
if C == '+':
 Suma = A+B
elif C == '-':
 Suma = A-B
elif C == '/':
 Suma = A/B
elif C == '*':
 Suma = A*B
print ('Сума:', Suma)