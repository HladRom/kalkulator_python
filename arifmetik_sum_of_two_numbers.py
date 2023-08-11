print('Add numbers and calculate their average')
numbers = []  # Створюємо пустий список для збереження чисел

n = int(input('How many numbers do you want to add: '))

for i in range(n):
    num = int(input(f'Add number {i + 1}: '))
    numbers.append(num)  # Додаємо число до списку

sum_numbers = sum(numbers)  # Обчислюємо суму всіх введених чисел
average = sum_numbers / n  # Обчислюємо середнє арифметичне

print('Sum:', sum_numbers)
print('Average:', average)