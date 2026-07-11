def is_palindrome(text):
    clean_text = text.lower()
    return clean_text == clean_text[::-1]

user_input = input("Enter a string: ")
print("Is palindrome:", is_palindrome(user_input))