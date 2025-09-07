def calculator():
    print("Welcome to Python Calculator")
    operators = ['+','-','/','*']
    num1 = operand1_var
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator: ")
    if ( type(num1 and num2) == int ) and operator in operators:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        else:
            return f"Invalid operator: {operator}"
    else:
        return f"Invalid operator: {operator}"






