num = int(input('add numbers:'))

print('multiplication table for', num)
for i in range (1, 11):
    result = num * i 
    print (num, "x", i, "=", result)
