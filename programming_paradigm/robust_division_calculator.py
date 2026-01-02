def safe_divide(numerator, denominator):
    try:
         nume = float(numerator)
         deno = float(denominator)
         return(nume / deno)
    except ValueError:
        return("ValueError: both arguments must be numbers")
    except ZeroDivisionError:
        return("ZeroDivisionError: the second argument must not be zero")
