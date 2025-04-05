try:
    num = int(input("Enter a number: "))
    print(f"Your number is {num}")
except ValueError:
    print("Oops! That's not a valid number.")
