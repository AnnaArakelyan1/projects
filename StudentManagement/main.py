from classes import ManagementSystem

def main():
    system = ManagementSystem()
    while True:
        print("\nStudent Management System ")
        print("1. Add Student")
        print("2. Add teacher")
        print("3. Display All Students")
        print("4. Display All Teachers")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.add_teacher()
        elif choice == '3':
            system.display_students()
        elif choice == '4':
            system.display_teachers()
        elif choice == '0':
            print("Ending")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
