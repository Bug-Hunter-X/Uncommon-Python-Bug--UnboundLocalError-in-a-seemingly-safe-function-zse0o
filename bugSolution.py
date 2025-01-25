def function_with_uncommon_error(x):
    try:
        result = 1 / x
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Input must be a number.")
        return None

if __name__ == "__main__":
    result = function_with_uncommon_error(0)
    print(result)
    result = function_with_uncommon_error("a")
    print(result)
    if result is not None:
        print(1 / result) # Check if result is valid before calculation