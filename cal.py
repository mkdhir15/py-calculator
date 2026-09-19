#Project -1 [Calculator] (Concepts used: functions, if-else, input-output)

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return "cannot divide by zero"
        return num1 / num2

    else:
        return"invalid operators"

#input 
num1 = float(input("enter first no.: "))
operator = input("enter operator: +, -, *, /: ")
num2 = float(input("enter second no."))

#function call
result = calculator(num1, num2, operator)

#output
print("Result: ", result)