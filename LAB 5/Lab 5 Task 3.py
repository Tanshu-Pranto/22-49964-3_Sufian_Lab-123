def find_max_min(numbers):
    if not numbers:
        return None, None
    
    max_val = numbers[0]
    min_val = numbers[0]
    
    for num in numbers:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
            
    return max_val, min_val

user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]

max_v, min_v = find_max_min(nums)
print("Max:", max_v)
print("Min:", min_v)