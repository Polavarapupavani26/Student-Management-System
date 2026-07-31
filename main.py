from student_manager import StudentManager

manager = StudentManager()

while True:
    print("\n========== Student Management System ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.view_students()

    elif choice == "3":
        manager.search_student()

    elif choice == "4":
        manager.update_student()

    elif choice == "5":
        manager.delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1 and 6.")