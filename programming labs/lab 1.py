# Student Fee Calculator

# Taking input from the user
tuition_fee = float(input("Enter Tuition Fee: "))
lab_fee = float(input("Enter Lab Fee: "))
library_fee = float(input("Enter Library Fee: "))
exam_fee = float(input("Enter Exam Fee: "))
discount = float(input("Enter Discount Amount: "))

# Calculating total fee
total_fee = tuition_fee + lab_fee + library_fee + exam_fee

# Subtracting discount
fee_after_discount = total_fee - discount

# Calculating annual fee (2 semesters)
annual_fee = fee_after_discount * 2

# Calculating monthly installment
monthly_installment = annual_fee / 12

# Displaying results
print("\nTuition Fee:", tuition_fee)
print("Lab Fee:", lab_fee)
print("Library Fee:", library_fee)
print("Exam Fee:", exam_fee)

print("Total Fee:", total_fee)
print("Discount:", discount)
print("Fee after Discount:", fee_after_discount)
print("Annual Fee:", annual_fee)
print("Monthly Installment:", monthly_installment)