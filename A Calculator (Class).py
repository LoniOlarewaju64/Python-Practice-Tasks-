# ---- First Part: Variable and Program Initialisation

class Calculator:
    def __init__(self):
        # We can store a running total or a history of calculations here
        self.result = 0
        self.history = []

    def get_result(self):
        # Returns the current result.
        return self.result

    def clear(self):
        # Resets the calculator result back to zero.
        self.result = 0
        return self.result



# --- Testing Code (Zone 1) (Outside the class) ---
# Create an instance (object) of the Calculator class
# my_calc = Calculator()

# Check the starting result
# print("Initial Result:", my_calc.get_result()) 




# --- Second Part: Arithmetic Methods ---
    def add(self, a, b):
        self.result = a + b
        return self.result
# For adding two numbers. E.G: 7 + 10 = 17

    def subtract(self, a, b):
        self.result = a - b
        return self.result
# For subtracting two numbers. E.G: 8 - 7 = 1

    def multiply(self, a, b):
        self.result = a * b 
        return self.result 
# Can multiply both inputted integers. E.G: 50 x 50 = 2,500

    def divide(self, a, b):
        if b == 0:
            print("Error: Cannot divide by zero!")
            return None
        self.result = a / b
        return self.result
     
# Divides two inputted numbers. Also, stops the '0 / 0' errors. E.G: 85/5 = 17


# --- Third Part: Code Execution and User Interface Creation ---
# OUTDATED CODING SCRAPS:
   # print("Initial Result:", my_calc.get_result())
   # print("5 + 3 =", my_calc.adding(5, 3))
   # print("10 / 2 =", my_calc.divide(10, 2))

def main():    
    calc = Calculator()

    while True:
        print("\n--- Python OOP Calculator ---")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '5':
            print("Goodbye!")
            break
            
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {calc.multiply(num1, num2)}")
            elif choice == '4':
                res = calc.divide(num1, num2)
                if res is not None:
                    print(f"Result: {num1} / {num2} = {res}")
        else:
            print("Invalid selection! Please pick a number from 1 to 5.")


# Standard entry point to start the program
if __name__ == "__main__":
    main()