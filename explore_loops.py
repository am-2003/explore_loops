def countdown_timer():
    # Task 1
    try:
        start_num = int(input("Enter the starting number: "))
        if start_num <= 0:
            print("Please enter a positive number!")
            return
            
        print("\nCountdown begins:")
        while start_num > 0:
            print(start_num, end=" ")
            start_num -= 1
        print("Blast off!")
    except ValueError:
        print("Please enter a valid number!")

def multiplication_table():
    # Task 2
    try:
        num = int(input("\nEnter a number for multiplication table: "))
        if num <= 0:
            print("Please enter a positive number!")
            return
            
        print(f"\nMultiplication table for {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Please enter a valid number!")

def calculate_factorial():
    # Task 3
    try:
        num = int(input("\nEnter a number to calculate factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers!")
            return
            
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(f"The factorial of {num} is {factorial}.")
    except ValueError:
        print("Please enter a valid number!")

countdown_timer()
multiplication_table()
calculate_factorial()