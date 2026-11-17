def display_all_students(students):
    if not students:
        print("\nNo student records found.")
        return
    print("\n--- All Student Records ---")
    for roll, data in students.items():
        marks = data["marks"]
        total = sum(marks)
        average = total / len(marks) if marks else 0
        print(f"Roll No: {roll} | Name: {data['name']} | Marks: {marks} | Total: {total} | Average: {average:.2f}")
    print("---------------------------")

def add_student(students, roll_no, name, marks):
    students[roll_no] = {
        "name": name,
        "marks": marks
    }
    print(f"[SUCCESS] Student with Roll No. {roll_no} added successfully.")

def search_student(students, roll_no):
    if roll_no in students:
        data = students[roll_no]
        marks = data["marks"]
        total = sum(marks)
        average = total / len(marks) if marks else 0
        print(f"\n[FOUND] Roll No: {roll_no} | Name: {data['name']} | Marks: {marks} | Total: {total} | Average: {average:.2f}")
    else:
        print(f"\n[ERROR] Student with Roll No. {roll_no} not found.")

def main():
    students = {}
    
    while True:
        print("\n=== STUDENT RECORDS MANAGEMENT SYSTEM ===")
        print("1. Display All Students")
        print("2. Add New Student")
        print("3. Search Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            display_all_students(students)
        elif choice == '2':
            roll_no = input("Enter Roll Number: ").strip()
            if roll_no in students:
                print("[ERROR] Student with this Roll Number already exists.")
                continue
            name = input("Enter Student Name: ").strip()
            try:
                marks = []
                print("Enter marks for 3 subjects:")
                for i in range(1, 4):
                    m = int(input(f"  Subject {i}: "))
                    marks.append(m)
                add_student(students, roll_no, name, marks)
            except ValueError:
                print("[ERROR] Marks must be valid integers.")
        elif choice == '3':
            roll_no = input("Enter Roll Number to search: ").strip()
            search_student(students, roll_no)
        elif choice == '4':
            print("Thank you for using the Student Records System. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter a number between 1 and 4.")

if _name_ == "_main_":
    main()