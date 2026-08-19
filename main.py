from student_manager import StudentManager


def main():
    manager = StudentManager()

    while True:
        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        try:
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
                print("Invalid choice. Please enter a number from 1 to 6.")

        except ValueError:
            print("Invalid input. Please enter the correct value.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()