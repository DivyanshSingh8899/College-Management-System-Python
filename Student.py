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
