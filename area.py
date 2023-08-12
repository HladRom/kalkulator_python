def calculate_area(length,width):
    area = length * width
    return area
#we receive input from the user
length = float(input('Enter length: '))
width = float(input('Enter width: '))
#call the function and display the result
area = calculate_area(length,width)
print('The area of the rectangle',area)


