def count_element_frequencies(my_list):
    counts = {}
    
    for item in my_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
            
    for key, value in counts.items():
        print(f"{key} => {value}")

# --- Test with your sample data ---
sample_list = [10, 20, 30, 30, 30, 30, 20, 40]
count_element_frequencies(sample_list)