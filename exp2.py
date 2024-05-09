
def check_palindrome():
    user_str = input("Enter a string: ")
    reversed_str = user_str[::-1]
    if user_str == reversed_str:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

while True:
    print("\nSelect an option:")
    print("1. Check if a string is a palindrome")
    print("2. Calculate the factorial of a number")
    print("3. Exit")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        check_palindrome()
    elif choice == 2:
        num = int(input("Enter a number to find its factorial: "))
        fact = factorial(num)
        print("The factorial of", num, "is:", fact)
    elif choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
