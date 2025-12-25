def perform_operation(num1, num2, operation):
    match operation:
        case "add" :
            return(num1 + num2)
        case "subtract":
            return(num1 - num2)
        case "multipy":
            return(num1 * num2)
        case "divide":
            if num2 == 0:
                return("Error division by zero")
            return(num1 / num2)
        case _:
            return("Enter a valid operation")

