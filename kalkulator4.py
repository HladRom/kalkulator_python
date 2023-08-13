add = lambda X, Y: X + Y
subtract = lambda X, Y: X - Y
multiply = lambda X, Y: X * Y
divide = lambda X, Y: X / Y

print ("Меню:")
print ("1.Додавання")
print ("2.Віднімання")
print ("3.Множення")
print ("4.Ділення")
choise = input("Введіть опцію 1/2/3/4: ")
numb1 = float(input("Введіть число 1: "))
numb2 = float(input("Введіть число 2: "))
 
if choise == "1":
 print ("Результат", add(numb1 , numb2))
elif choise == "2":
 print ("Результат", subtract(numb1 ,numb2))
elif choise == "3":
 print ("Результат", multiply(numb1 , numb2))
elif choise == "4":
 if numb2 != 0:
    print ("Результат", divide(numb1 ,numb2))
 else:
  print ("Введене число невірне: ")
else:
  print ("Виберіть варіант 1/2/3/4 ")