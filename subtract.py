firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
if secondNumber > firstNumber:
    print("ERROR!!! First number must be larger than second number.")  # not allowed
else:
    result = firstNumber - secondNumber  # perform subtraction
    print("Subtraction result is: ", result)
