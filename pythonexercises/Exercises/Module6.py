# 1.
import random
def RollDice():
    r = random.randint(1,6)
    return r
#
# result = 0
# while result != 6:
#     result = RollDice()
#     print(result)

# 2.
# import random
# def RollDice(x):
#     r = random.randint(1,s)
#     return r
#
# s = int(input("Enter number of sides: "))
# result = 0
# while result != s:
#     result = RollDice(s)
#     print(result)

# 3.
# def GallontoLiter(x):
#     l = 3.78541*x
#     return l
# g = float(input("Enter number of gallon: "))
# while g >= 0:
#     print(f"{g} gallons() is equal to {GallontoLiter(g)} liter(s)")
#     g = float(input("Enter number of gallon: "))
# print("Program ended")

# 4.
# def SumofList(x):
#     s = 0
#     for i in x:
#         s = s + i
#     return s
#
# n = [4,6,5,7]
# print(f"Sum of list is: {SumofList(n)}")

# 5.
# def RemoveOdd(x):
#     y = []
#     for i in x:
#         if i % 2 == 0:
#             y.append(i)
#     return y
#
# n = [1,1,1,2,3,4,5,6,7,8,9,10,11]
# print(f"Original list: {n}")
# print(f"List with uneven removed: {RemoveOdd(n)}")

# 6.
# def PizzaPriceCheck(diameter,price):
#     diameter_m = float(diameter)/100
#     area = 0.25*3.14*diameter_m**2
#     priceperarea = float(price)/area #smaller is better
#     return priceperarea
#
# p1d = input("Enter pizza 1 diameter (cm): ")
# p1p = input("Enter pizza 1 price (EUR): ")
# p2d = input("Enter pizza 2 diameter (cm): ")
# p2p = input("Enter pizza 2 price (EUR): ")
# pizza1 = float(PizzaPriceCheck(p1d,p1p))
# pizza2 = float(PizzaPriceCheck(p2d,p2p))
# if pizza1 < pizza2:
#     print("Pizza 1 is better for the money")
# else:
#     print("Pizza 2 is better for the money")



