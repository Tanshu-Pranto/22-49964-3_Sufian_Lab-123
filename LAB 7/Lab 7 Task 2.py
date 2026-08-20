try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    if not num1.replace(".", "", 1).isdigit() or not num2.replace(".", "", 1).isdigit():
        raise TypeError("Inputs must be numerical.")

    num1 = float(num1)
    num2 = float(num2)

    print("Sum:", num1 + num2)

except TypeError as e:
    print("TypeError:", e)