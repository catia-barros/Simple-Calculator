''' A calculator that runs in an infinite loop until until the user insert "q" to quit '''
while True:
    # Ask the user which operation they want to perform
    operator = input("Choose an operation (+, -, *, /, %, **), or 'q' to quit: ")

    # If the user inserts "q" the program stops
    if operator == "q":
        print("Goodbye!")
        break

    # Checks to ensure only allowed symbols are used
    if operator not in ["+", "-", "*", "/", "%", "**"]:
        print("Invalid operator")
        continue

    try:
        # Input is converted into float so we can handle decimal numbers
        number_1 = float(input("Enter first number: "))
        number_2 = float(input("Enter second number: "))
    
    except ValueError:
        # A ValueError will be raised if the user isn't addinng a number
        print("Error: Please enter valid numbers")
        continue

    # Module by zero isn't allowed in Python
    if operator == "%" and number_2 == 0:
        print("Error: Cannot modulo by zero")
        continue

    # Handle division by zero and return "Infinity"
    if operator == "/" and number_2 == 0:
        print("Result: Infinity")
        continue

    # The correct operation is performed based on the chosen operator
    if operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "*":
        result = number_1 * number_2
    elif operator == "/":
        result = number_1 / number_2
    elif operator == "%":
        result = number_1 % number_2
    elif operator == "**":
        result = number_1 ** number_2
    
    # The result is printed
    print("Result:", result)