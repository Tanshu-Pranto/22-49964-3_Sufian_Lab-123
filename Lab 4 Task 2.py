from collections import Counter

# Original dictionary
original_dict = {
    'V': 10, 
    'VI': 10, 
    'VII': 40, 
    'VIII': 20, 
    'IX': 70, 
    'X': 80, 
    'XI': 40, 
    'XII': 20
}

# Count the frequency of values
value_frequencies = Counter(original_dict.values())

# Display the result
print("Original Dictionary:", original_dict)
print("Count the frequency of the said dictionary:", value_frequencies)