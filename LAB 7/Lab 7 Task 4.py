import os

file_path = "sample.txt"

try:
    # Write
    with open(file_path, "w") as file:
        file.write("Hello Python!\n")
        file.write("This is the write operation.\n")

    print("File written successfully.")

    # Read
    with open(file_path, "r") as file:
        data = file.read()

    print("\nFile contents after writing:")
    print(data)

    # Append
    with open(file_path, "a") as file:
        file.write("This line was added using append.\n")

    print("Data appended successfully.")

    # Read again
    with open(file_path, "r") as file:
        data = file.read()

    print("\nFile contents after appending:")
    print(data)

    # Create
    new_file = "newfile.txt"

    with open(new_file, "x") as file:
        file.write("This is a newly created file.")

    print("New file created successfully.")

except FileExistsError:
    print("The file already exists.")

except FileNotFoundError:
    print("The specified file was not found.")

except Exception as e:
    print("An unexpected error occurred:", e)