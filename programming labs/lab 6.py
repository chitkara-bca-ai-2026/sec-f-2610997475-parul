# Lab 06 - Shop Billing System

# Taking input
customer_name = input("Enter Customer Name: ")
garment_name = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))

# Calculating total amount
total_amount = price * quantity

# Displaying bill
print("\n================================")
print("             BILL")
print("================================")

print(f"Customer Name : {customer_name}")
print(f"Garment Name  : {garment_name}")
print(f"Price per Unit: Rs. {price}")
print(f"Quantity      : {quantity}")
print(f"Total Amount  : Rs. {total_amount}")

print("================================")