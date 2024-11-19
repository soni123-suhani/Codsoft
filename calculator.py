def calculator():
    print("welcome to calculator with brackets support!")
    print("Select operation:")
    print("Example: (2 + 3) * 4 / (1 - 5)")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Module")
 
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("Result:", num1 + num2)
        elif choice == '2':
            print("Result:", num1 - num2)
        elif choice == '3':
            print("Result:", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero")
        elif choice == '5':
            if num2 != 0:
                print("Result:", num1 % num2)
            else:
                print("Error: Cannot find modulo by zero")
    else:
        print("Invalid Input")
calculator()           
            

