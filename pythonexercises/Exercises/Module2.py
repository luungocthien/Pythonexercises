# 1.
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 2.
# radius = float(input("Enter the radius of the circle: "))
# print(f"Area of the circle is: {3.14*radius**2}")

# 3.
# s1 = float(input("Enter first side of rectangle: "))
# s2 = float(input("Enter second side of rectangle: "))
# print(f"Perimeter of the rectangle is: {(s1+s2)*2}, area of the rectangle is: {s1*s2}")

# 4.
# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     num3 = float(input("Enter the third number: "))
#
#     print(f"Sum of the numbers: {num1+num2+num3}, produce of the numbers:{num1*num2*num3}, average of the numbers:{(num1+num2+num3)/3}")
# except:
#     print("Invalid input")

# 5.
# try:
#     talents = float(input("Enter talents: "))
#     pounds = float(input("Enter pounds: "))
#     lots = float(input("Enter lots: "))
#
#     w_lots = 13.3
#     w_pounds = 32 * w_lots
#     w_talents = 20 * w_pounds
#
#     gram = (talents * w_talents) + (pounds * w_pounds) + (lots * w_lots)
#     kilogram = gram // 1000
#     remain_gram = gram % 1000
#     print(f"The weight in modern units: {kilogram:.0f} kilogram(s) {remain_gram:.2f} gram(s)")
# except:
#     print("Invalid input")

# 6.
# import random
#
# random_number1_1 = str(random.randint(0,9))
# random_number1_2 = str(random.randint(0,9))
# random_number1_3 = str(random.randint(0,9))
# random_number2_1 = str(random.randint(1,6))
# random_number2_2 = str(random.randint(1,6))
# random_number2_3 = str(random.randint(1,6))
# random_number2_4 = str(random.randint(1,6))
#
# print(f"Code 1: {random_number1_1+random_number1_2+random_number1_3}")
# print(f"Code 2: {random_number2_1+random_number2_2+random_number2_3+random_number2_4}")