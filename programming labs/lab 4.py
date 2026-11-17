# Lab 04 - Data Conversion Utility

# Taking input from the user
product_name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

# Calculating total price
total_price = price * quantity

# Converting total price into string
amount_str = str(total_price)

# Displaying data types
print("\n--------- TYPE CASTING SUMMARY ---------")

print("Variable       Value       Data Type")
print("product_name:", product_name, type(product_name))
print("price:", price, type(price))
print("quantity:", quantity, type(quantity))
print("total_price:", total_price, type(total_price))
print("amount_str:", amount_str, type(amount_str))

# Displaying tax invoice
print("\n------------- TAX INVOICE -------------")
print(f"Product Name   : {product_name}")
print(f"Price per Unit : Rs. {price}")
print(f"Quantity       : {quantity}")
print(f"Invoice Total  : Rs. {amount_str}")
print("---------------------------------------")