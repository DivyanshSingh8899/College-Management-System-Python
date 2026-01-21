from student_module.student import student_menu
from faculty_module.faculty import faculty_menu
from course_module.course import course_menu
from fees_module.fees import fees_menu

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
