# 4.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    print(f"Sum of the numbers: {num1+num2+num3}, produce of the numbers:{num1*num2*num3}, average of the numbers:{(num1+num2+num3)/3}")
except:
    print("Invalid input")
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