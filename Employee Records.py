# The Code Purpose: This is for recording a registered employee in a business.

def add_employee():
    try:
        emp_id = input("Enter Employee ID: ").strip()
        # Ensure Employee ID is not empty using assert
        assert len(emp_id) > 0, "Employee ID cannot be empty."

        name = input("Enter Employee Name: ").strip()
        salary = float(input("Enter Monthly Salary: "))

        # Raise ValueError if salary is 0 or negative
        if salary <= 0:
            raise ValueError("Salary must be a positive number.")

    except AssertionError as ae:
        print(f"Error: {ae}")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        # Executes only if no errors occurred in try block
        with open("employees.txt", "a") as file:
            file.write(f"{emp_id}, {name}, {salary:.2f}\n")
        print("Employee saved successfully.")
    finally:
        # Executes regardless of pass or fail
        print("Completed 'Add Employee' operation.")


def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if not records:
                print("No employee records found.")
                return

            print("\n--- Employee List ---")
            for record in records:
                print(record.strip())
    except FileNotFoundError:
        print("Error: 'employees.txt' does not exist yet. Please add an employee first.")
    finally:
        print("Completed 'View Employees' operation.")


def search_employee():
    search_id = input("Enter Employee ID to search: ").strip()
    found = False

    try:
        with open("employees.txt", "r") as file:
            for line in file:
                emp_id, name, salary = line.strip().split(", ")
                if emp_id.lower() == search_id.lower():
                    print(
                        f"\nEmployee Found!\nID: {emp_id}\nName: {name}\nSalary: ${salary}"
                    )
                    found = True
                    break

        if not found:
            print(f"No employee found with ID '{search_id}'.")

    except FileNotFoundError:
        print("Error: 'employees.txt' does not exist yet.")
    finally:
        print("Completed 'Search Employee' operation.")


def main():
    while True:
        print("\n===== Employee Salary System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Thank you for using the Employee Salary System.")
            break
        else:
            print("Invalid option! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()