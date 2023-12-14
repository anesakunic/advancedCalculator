import math

saved_numbers = []
last_result = None
temp_result = None
save_result = False

def addition(firstNum, secondNum):
    result = firstNum + secondNum
    print(f"Result is: {result}")
    return result

def subtraction(firstNum, secondNum):
    result = firstNum - secondNum
    print(f"Result is: {result}")
    return result

def multiplication(firstNum, secondNum):
    result = firstNum * secondNum
    print(f"Result is: {result}")
    return result

def division(firstNum, secondNum):
    result = firstNum / secondNum
    print(f"Result is: {result}")
    return result

def remainder(firstNum, secondNum):
    result = firstNum % secondNum
    print(f"Result is: {result}")
    return result

def exponential(firstNum, secondNum):
    result = 1
    if secondNum >= 0:
        for _ in range(int(secondNum)):
            result *= firstNum
        print(f"Result is: {result}")
        return result
    else:
        return 0  # invalid input

def root(firstNum):
    result = math.sqrt(float(firstNum))
    print(f"Result is: {result}")
    return result

def save_number(number):
    saved_numbers.append(number)
    print(f"Number {number} saved")

def list_saved_numbers():
    if len(saved_numbers) == 0:
        print("No saved numbers")
    else:
        for i, number in enumerate(saved_numbers):
            print(f"{i + 1}: {number}")

def retrieve_number(index):
    try:
        index = int(index)
        if index < 1 or index > len(saved_numbers):
            print("Result does not exist at location")
            return None
        else:
            return saved_numbers[index - 1]
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

print("Key Triggers")
print("+ Sum operator")
print("- Subtraction operator")
print("/ Division operator")
print("* Multiplication operator")
print("% Remainder operator")
print("^ Exponential operator")
print("s Square root operator")
print("= Operator that triggers a particular operation (above) to execute")
print("M Save last input")
print("P List saved numbers")
print("Rn Retrieve with any number where n is any number from the list")

while True:
    firstNum = input("Enter first number: ")
    operator = input("Enter operator: ")
    
    try:
        num1 = float(firstNum)
    except ValueError:
        print('Invalid input. Please enter a number.')
        continue

    if operator in ('+', '-', '*', '/', '%', '^', 's'):
        if operator == "+":
            secondNum = input("Enter second number: ")
            try:
                num2 = float(secondNum)
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue
            temp_result = addition(num1, num2)
        elif operator == "-":
            secondNum = input("Enter second number: ")
            try:
                num2 = float(secondNum)
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue
            temp_result = subtraction(num1, num2)
        elif operator == "*":
            secondNum = input("Enter second number: ")
            try:
                num2 = float(secondNum)
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue
            temp_result = multiplication(num1, num2)
        elif operator == "/":
            secondNum = input("Enter second number: ")
            try:
                num2 = float(secondNum)
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue
            temp_result = division(num1, num2)
        elif operator == "%":
            secondNum = input("Enter second number: ")
            try:
                num2 = float(secondNum)
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue
            temp_result = remainder(num1, num2)
        elif operator == "^":
            secondNum = input("Enter second number: ")
            try:
                num2 = float(secondNum)
            except ValueError:
                print('Invalid input. Please enter a number.')
                continue
            temp_result = exponential(num1, num2)
        elif operator == "s":
            temp_result = root(num1)
        else:
            print("Choose a correct operator, try again.")

        save_result = input("Enter M to save result: ") == "M"
        if save_result:
            save_number(temp_result)
        last_result = temp_result
        print(temp_result)

    elif operator == "=":
        if last_result is not None:
            temp_result = last_result
            print(f"Result is: {temp_result}")
        else:
            print("No result to display.")

    elif operator == "M":
        if temp_result is not None:
            save_number(temp_result)
            last_result = temp_result
        else:
            result = input("Enter result to save: ")
            save_number(result)
            last_result = result

    elif operator == "P":
        list_saved_numbers()

    elif operator.startswith("R"):
        index = operator[1:]
        result = retrieve_number(index)
        if result is not None:
            print(f"Retrieved number: {result}")
            temp_result = result
            last_result = result  # Assign retrieved result to last_result for subsequent calculations

    else:
        print("Invalid operator. Choose a correct operator, try again.")
