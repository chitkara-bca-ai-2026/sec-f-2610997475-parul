# Part A: Setup, Menu, View, Search, and Register

def display_menu():
    print("\n" + "=" * 55)
    print("          STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("=" * 55)
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    print("-" * 55)

def main_part_a():
    # 1. Initial Data Setup
    students = {
        "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
        "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
        "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]}
    }

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\n--- Enrolled Student Records ---")
            for roll, info in students.items():
                print(f"Roll No: {roll} | Name: {info['Name']} | Branch: {info['Branch']}")
                print(f"Sem: {info['Semester']} | Marks: {info['Marks']}")
            print(f"Total Enrolled Students: {len(students)}")

        elif choice == "2":
            roll = input("Enter Roll Number to search: ").strip()
            student = students.get(roll)
            if student:
                print(f"\n[FOUND] Record for Roll No {roll}:")
                print(f"Name     : {student['Name']}")
                print(f"Branch   : {student['Branch']}")
                print(f"Semester : {student['Semester']}")
                print(f"Marks    : {student['Marks']}")
            else:
                print(f"\n[ERROR] Student with Roll No {roll} not found.")

        elif choice == "3":
            print("\n--- Register New Student ---")
            roll = input("Enter Roll Number: ").strip()
            if roll in students:
                print(f"\n[ERROR] Student with Roll No {roll} already exists!")
            else:
                name = input("Enter Student Name: ").strip()
                branch = input("Enter Branch (e.g., BCA AI): ").strip()
                semester = input("Enter Semester: ").strip()
                try:
                    m1 = int(input("Subject 1: "))
                    m2 = int(input("Subject 2: "))
                    m3 = int(input("Subject 3: "))
                    students[roll] = {
                        "Name": name,
                        "Branch": branch,
                        "Semester": semester,
                        "Marks": [m1, m2, m3]
                    }
                    print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")
                except ValueError:
                    print("\n[ERROR] Invalid marks entered.")

        elif choice in ["4", "5", "6", "7"]:
            print("\n[INFO] This operation belongs to Part B or Part C.")
        else:
            print("\n[ERROR] Invalid choice!")

if _name_ == "_main_":
    main_part_a()