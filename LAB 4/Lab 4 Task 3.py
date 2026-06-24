def is_palindrome(string):
    # Clean the string: convert to lowercase and keep only alphanumeric characters
    cleaned_string = "".join(char.lower() for char in string if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Take dynamic string input from the user
user_input = input("Enter a string to check if it's a palindrome: ")

# Check and display the result
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome!')
else:
    print(f'"{user_input}" is NOT a palindrome.')