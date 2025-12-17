num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

def print_result(result):
    print(f"The result is {result}.")
match operation:
    case "+":
        print_result(num1 + num2)
    case "-":
        print_result(num1 - num2)
    case "*":
        print_result(num1 * num2)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print_result(num1 / num2)
    
