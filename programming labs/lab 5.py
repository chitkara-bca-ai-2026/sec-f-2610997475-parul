# Lab 05 - Engineering Calculation Tool

import math

# Taking input
value = float(input("Enter a numerical value: "))
exponent = float(input("Enter an exponent: "))
decimal_value = float(input("Enter a decimal measurement: "))

# Calculations
power = pow(value, exponent)
square_root = math.sqrt(value)
ceil_value = math.ceil(decimal_value)
floor_value = math.floor(decimal_value)

# Displaying results
print("\n------ Results ------")
print("Value:", value)
print("Exponent:", exponent)
print("Power (pow):", power)
print("Square Root (sqrt):", square_root)
print("Decimal Value:", decimal_value)
print("Ceil Value:", ceil_value)
print("Floor Value:", floor_value)
print("---------------------")