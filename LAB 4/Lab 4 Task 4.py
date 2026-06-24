def get_unique_items(original_list):
    unique_list = []
    
    for item in original_list:
        if item not in unique_list:
            unique_list.append(item)
            
    return unique_list

sample_data = [1, 2, 3, 3, 3, 3, 4, 5]
result = get_unique_items(sample_data)

print("Original list:", sample_data)
print("Cleaned list :", result)