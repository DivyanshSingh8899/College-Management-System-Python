import json

FILE = "data/students.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    students = load_data()
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    students.append({"ID": sid, "Name": name, "Course": course})
    save_data(students)
    print("Student Added Successfully")

def view_students():
    students = load_data()
    for s in students:
        print(s)

def student_menu():
    while True:
        print("\n--- Student Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Back")

        ch = int(input("Enter choice: "))
        if ch == 1:
            add_student()
        elif ch == 2:
            view_students()
        elif ch == 3:
            break

FACULTY_FILE = "data/faculty.json"

def load_faculty():
    try:
        with open(FACULTY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_faculty(data):
    with open(FACULTY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_faculty():
    faculty_list = load_faculty()
    fid = input("Enter Faculty ID: ")
    name = input("Enter Faculty Name: ")
    department = input("Enter Department: ")
    faculty_list.append({"ID": fid, "Name": name, "Department": department})
    save_faculty(faculty_list)
    print("Faculty Added Successfully")

def view_faculty():
    faculty_list = load_faculty()
    for f in faculty_list:
        print(f)

def faculty_menu():
    while True:
        print("\n--- Faculty Management ---")
        print("1. Add Faculty")
        print("2. View Faculty")
        print("3. Back")

        ch = int(input("Enter choice: "))
        if ch == 1:
            add_faculty()
        elif ch == 2:
            view_faculty()
        elif ch == 3:
            break

def course_menu():
    print("\n--- Course Management ---")
    print("Coming Soon!")

def fees_menu():
    print("\n--- Fees & Reports ---")
    print("Coming Soon!")

if __name__ == "__main__":
    while True:
        print("\n===== COLLEGE MANAGEMENT SYSTEM =====")
        print("1. Student Management")
        print("2. Faculty Management")
        print("3. Course Management")
        print("4. Fees & Reports")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_menu()
        elif choice == 2:
            faculty_menu()
        elif choice == 3:
            course_menu()
        elif choice == 4:
            fees_menu()
        elif choice == 5:
            print("Thank You!")
            break
        else:
            print("Invalid choice")
