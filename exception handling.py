try:
    num1 = int(input("Enter first number = "))
    num2 = int(input("Enter second number = "))
    # value_error
    """
    when declare integer input but use float then it gives us value error
    """
    result = num1 / num2
    print(result)
except(ValueError,ZeroDivisionError):
    print("You Entered incorrect input")
