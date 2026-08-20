my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Value:", my_list[index])

except IndexError:
    print("IndexError: Index is out of range.")

except ValueError:
    print("Please enter an integer index.")