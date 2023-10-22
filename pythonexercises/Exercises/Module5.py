# 1.
import random
result = 0
dices = int(input("Number of dices to roll: \n"))
for d in range(dices):
    roll = random.randint(1,6)
    print(f"Rolled a {roll}")
    result += roll
print(f"result is {result}")

# 2.
# numlist = []
# while True:
#     try:
#         n = input("Enter numbers (Press Enter to stop):\n")
#         if n != "":
#             n_value = float(n)
#             numlist.append(n_value)
#         elif n == "":
#             break
#     except:
#         print("Wrong input")
# numlist.sort(reverse=True)
# print(numlist[:5])

# 3.
# try:
#     n = int(input("Enter an integer: "))
#     c = 0
#     for i in range(1,n+1):
#         if n % i == 0:
#             c += 1
#     if n == 1:
#         print(f"{n} is not a prime number")
#     elif c > 2:
#         print(f"{n} is not a prime number")
#     elif c == 2:
#         print(f"{n} is a prime number")
# except:
#     print("Invalid input")

# 4.
# cities = []
# for i in range(5):
#     c = str(input("Enter a city: "))
#     cities.append(c)
# for city in cities:
#     print(f"{city}")