def reverse_words(text):
    words = text.split(" ")
    return " ".join([word[::-1] for word in words])

user_input = input("Enter a string: ")
print("Result:", reverse_words(user_input))