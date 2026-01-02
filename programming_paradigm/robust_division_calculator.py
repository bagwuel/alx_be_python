def safe_divide(numerator, denominator):
    try:
         nume = float(numerator)
         deno = float(denominator)
         return(f"The result of the division is {nume / deno}")
    except ValueError:
        return("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        return("Error: Cannot divide by zero.")
