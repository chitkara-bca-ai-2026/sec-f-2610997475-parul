# Part B: Update Details & Academic Performance

def main_part_b():
    # Sample dictionary for standalone testing of Part B
    students = {
        "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
        "104": {"Name": "Simran", "Branch": "BCA AI", "Semester": "1", "Marks": [88, 91, 84]}
    }

    while True:
        print("\n--- Part B Menu ---")
        print("4. Update Student Details")
        print("5. View Academic Performance")
        print("7. Exit")
        choice = input("Enter choice (4, 5, or 7): ").strip()

        if choice == "4":
            roll = input("Enter Roll Number to update: ").strip()
            if roll in students:
                student = students[roll]
                print(f"Current details for {student['Name']} (Roll {roll}):")
                print("1. Branch | 2. Semester")
                field_choice = input("Choose field to update (1 or 2): ").strip()
                
                if field_choice == "1":
                    new_branch = input("Enter new branch: ").strip()
                    student["Branch"] = new_branch
                    print(f"\n[SUCCESS] Branch updated to '{new_branch}'.")
                elif field_choice == "2":
                    new_sem = input("Enter new semester: ").strip()
                    student["Semester"] = new_sem
                    print(f"\n[SUCCESS] Semester updated to '{new_sem}'.")
                else:
                    print("\n[ERROR] Invalid field choice.")
            else:
                print(f"\n[ERROR] Student with Roll No {roll} not found.")

        elif choice == "5":
            roll = input("Enter Roll Number for Academic Performance: ").strip()
            if roll in students:
                student = students[roll]
                marks_list = student["Marks"]
                total = sum(marks_list)
                average = total / len(marks_list)
                status = "PASS" if average >= 40 else "FAIL"
                
                print("\n" + "*" * 42)
                print(" " * 12 + "ACADEMIC REPORT")
                print("*" * 42)
                print(f"Student Name : {student['Name']} (Roll: {roll})")
                print(f"Subject Marks: {marks_list}")
                print(f"Total Marks  : {total} / {len(marks_list) * 100}")
                print(f"Average Marks: {average:.2f}%")
                print(f"Final Result : {status}")
                print("*" * 42)
            else:
                print(f"\n[ERROR] Student with Roll No {roll} not found.")

        elif choice == "7":
            print("Exiting Part B.")
            break
        else:
            print("Invalid choice.")

if _name_ == "_main_":
    main_part_b()