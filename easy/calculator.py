def calculator():
    first_number = float(input("Enter first number: "))
    operator = input("choose operation (+ - * /): ")
    second_number = float(input("Enter second number: "))

    if operator == "+":
        answer = first_number + second_number
    elif operator == "-":
        answer = first_number - second_number
    elif operator == "*":
        answer = first_number * second_number
    elif operator == "%":
        if second_number == 0:
            print("You cannot divide by zero.")
            return
        answer = first_number / second_number
    else:
        print("Invalid operator")
        return
    
    print(answer)


calculator()