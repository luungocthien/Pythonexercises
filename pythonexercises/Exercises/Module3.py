# 1.
try:
    zlen = float(input("Zander's length (cm): "))
    if zlen >= 48:
        print("Nice catch!")
    else:
        print(f"Your zander is {48-zlen} cm under the limit, please release")
except:
    print("Invalid input")

# 2.
# cabin_class = input("Enter the cabin class:\n ")
# if cabin_class == "LUX":
#     print("LUX: upper-deck cabin with a balcony.")
# elif cabin_class == "A":
#     print("A: above the car deck, equipped with a window.")
# elif cabin_class == "B":
#     print("B: windowless cabin above the car deck.")
# elif cabin_class == "C":
#     print("C: windowless cabin below the car deck.")
# else:
#     print("Invalid cabin class")

# 3.
# try:
#     bio_gender = str(input("Enter your biological gender (male/female):\n"))
#     hemoglobin_value = float(input("Enter your hemoglobin value (g/l):\n"))
#
#     if bio_gender == "female":
#         if hemoglobin_value > 155:
#             print("Your hemoglobin value is higher than normal")
#         elif hemoglobin_value < 117:
#             print("Your hemoglobin value is lower than normal")
#         elif 117 <= hemoglobin_value <= 155:
#             print("Your hemoglobin value is normal")
#     if bio_gender == "male":
#         if hemoglobin_value > 167:
#             print("Your hemoglobin value is higher than normal")
#         elif hemoglobin_value < 134:
#             print("Your hemoglobin value is lower than normal")
#         elif 134 <= hemoglobin_value <= 167:
#             print("Your hemoglobin value is normal")
#     else:
#         print("Invalid input")
# except:
#     print("Invalid input")

# 4.
# try:
#     year = int(input("Enter year: "))
#     if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")
# except:
#     print("Invalid input")