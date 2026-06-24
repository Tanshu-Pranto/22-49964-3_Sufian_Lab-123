
starts_with = lambda s, sub: s.startswith(sub)

main_string = input("Enter the main string: ")
sub_string = input("Enter the sub-string to check: ")

if starts_with(main_string, sub_string):
    print(f"Yes! '{main_string}' starts with '{sub_string}'.")
else:
    print(f"No! '{main_string}' does not start with '{sub_string}'.")