
def swap_numbers(n1, n2):
    temp = n1
    n1 = n2
    n2 = temp
    print("After swapping:")
    print("Value of n1:", n1)
    print("Value of n2:", n2)

def check_number(n):
    if n > 0:
        print("The number is positive")
    elif n == 0:
        print("The number is zero")
    else:
        print("The number is negative")


n1 = int(input("Enter first number (n1): "))
n2 = int(input("Enter second number (n2): "))

swap_numbers(n1, n2)

check_number(n1)


