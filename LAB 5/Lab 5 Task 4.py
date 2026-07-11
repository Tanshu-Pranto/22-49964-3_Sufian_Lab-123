def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

items_input = input("Enter values separated by spaces: ")
items = items_input.split()

target = input("Enter the value to search for: ")

index = linear_search(items, target)

if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")