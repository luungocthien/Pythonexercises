# 1.
# seasons = ("spring","summer","autumn","winter")
# while True:
#     try:
#         month = int(input("Enter the month: "))
#         if month == 12 or 2>= month >=1:
#             print(f"The month is in {seasons[3]}")
#         elif 5 >= month >= 3:
#             print(f"The month is in {seasons[0]}")
#         elif 8 >= month >= 6:
#             print(f"The month is in {seasons[1]}")
#         elif 11 >= month >= 9:
#             print(f"The month is in {seasons[2]}")
#         else:
#             print("Invalid input")
#     except:
#         print("Invalid input")

# 2.
# names = set()
# n = str(input("Enter a name:"))
# while n != "":
#     if n in names:
#         print("Existing name")
#     else:
#         print("New name")
#     names.add(n)
#     n = str(input("Enter a name:"))
# print("Program ended")

# 3.
# airport = {}
# i = 0
# while i != 3:
#     try:
#         print("Select an option:\n1. Add airport\n2. Search airport\n3. Quit\n")
#         i = int(input("Select option:"))
#         if i == 1:
#             icao = input("Enter the ICAO code of the airport: ")
#             airport_name = input("Enter the name of the airport: ")
#             airport[icao] = airport_name
#             print(f"Airport with ICAO code '{icao}' and name '{airport_name}' has been added.")
#         elif i == 2:
#             icao = input("Enter the ICAO code of the airport to fetch information: ")
#             if icao in airport:
#                 print(f"The airport with ICAO code '{icao}' is '{airport[icao]}'")
#             else:
#                 print(f"No airport found with ICAO code '{icao}'")
#     except:
#         print("Invalid input")
# print("Program ended")