print ('Enter the data:')
A = int(input('Enter number:'))
C = input('Enter action:')
B = int(input('Enter number:'))
if C == '+':
 Suma = A+B
elif C == '-':
 Suma = A-B
elif C == '/':
 Suma = A/B
elif C == '*':
 Suma = A*B
print ('Sum:', Suma)