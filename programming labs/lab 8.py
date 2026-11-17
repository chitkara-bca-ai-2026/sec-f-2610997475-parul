# Lab 08 - School Result Processing

# Taking student details
student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

# Creating an empty list
marks = []

# Taking marks for 5 subjects
print("\n--- Enter Marks for 5 Subjects (0-100) ---")

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))

    # Validating marks
    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100.")
        break

    marks.append(mark)

# Processing result only if all 5 marks are valid
if len(marks) == 5:

    # Calculating total and percentage
    total = sum(marks)
    percentage = (total / 500) * 100

    # Checking pass or fail
    if min(marks) < 40:
        result = "FAIL"
        grade = "F"
        remark = "Failed in one or more subjects"

    else:
        result = "PASS"

        # Assigning grade and remark
        if percentage >= 90:
            grade = "A+"
            remark = "Outstanding"

        elif percentage >= 80:
            grade = "A"
            remark = "Excellent"

        elif percentage >= 70:
            grade = "B"
            remark = "Very Good"

        elif percentage >= 60:
            grade = "C"
            remark = "Good"

        elif percentage >= 50:
            grade = "D"
            remark = "Satisfactory"

        elif percentage >= 40:
            grade = "E"
            remark = "Pass"

    # Displaying report card
    print("\n========================================")
    print("             STUDENT REPORT CARD")
    print("========================================")

    print(f"Student Name : {student_name}")
    print(f"Roll Number  : {roll_number}")

    print("----------------------------------------")
    print(f"Total Marks  : {total} / 500")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Result       : {result}")
    print(f"Grade        : {grade}")
    print(f"Remarks      : {remark}")

    print("========================================")