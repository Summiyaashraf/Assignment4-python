# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a test file.")

# Reading from the file
with open("sample.txt", "r") as file:
    print(file.read())
