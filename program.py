import math

def calculate_circle_area(radius):
    # Обчислити площу кола за формулою A = π * r^2
    area = math.pi * radius ** 2
    return area

# Запитати користувача про радіус кола
radius = float(input("Введіть радіус кола: "))

# Викликати функцію для обчислення площі кола та вивести результат
circle_area = calculate_circle_area(radius)
print("Площа кола з радіусом", radius, "дорівнює", circle_area)