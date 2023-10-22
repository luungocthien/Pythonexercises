# 1.
n=0
while n <= 1000:
    if n % 3 == 0:
        print(n)
    n = n + 1

# 2.
# try:
#     inch = float(input("Enter length in inches:"))
#     cm=0
#     while inch >= 0:
#         cm = inch*2.54
#         print(f"{inch} inch(es) is equal to {cm} centimetter(s)")
#         inch = float(input("Enter length in inches:"))
#     print("Program ended")
# except:
#     print("Invalid input")


# numbers = []
# while True:
#     try:
#         n = input("Enter numbers (Press Enter to stop):\n")
#         if n != "":
#             n_value = float(n)
#             numbers.append(n_value)
#         elif n == "":
#             break
#     except:
#         print("Wrong input")
# if numbers != []:
#     minnum = min(numbers)
#     maxnum = max(numbers)
#     print(f"Smallest number: {minnum}, biggest number: {maxnum}")
# else:
#     print("No input")

# import random
# r_num = random.randint(1,10)
# print(r_num)
# guess = 0
# while guess != r_num:
#     try:
#         guess = int(input("Enter your guess (1-10):"))
#         if guess > r_num:
#             print("Too high")
#         elif guess < r_num:
#             print("Too low")
#         elif guess == r_num:
#             print("Correct")
#     except:
#         print("Invalid input")
# else:
#     print("Game ended")

# username = "python"
# password = "rules"
# input_username = None
# input_password = None
# timestried = 0

# while timestried < 5 and input_username != username and input_password != password:
#     input_username = input("Enter your username:\n")
#     input_password = input("Enter your password:\n")
#     timestried = timestried + 1
#     if input_username == username and input_password == password:
#         print("Welcome")
# if input_username != username and input_password != password:
#     print("Access denied")

# import random
# n_points = int(input("Enter the number of random points: "))
# n = 0
# p_in = 0
# while n <= n_points:
#     x = random.uniform(-1,1)
#     y = random.uniform(-1,1)
#     if x**2 + y**2 < 1:
#         p_in += 1
#     n += 1
# a_pi = 4 * p_in / n_points
# print(f"Approximation of pi using {n_points} random points: {a_pi}")