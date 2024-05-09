# Function to put even and odd elements into two different lists
def separate_even_odd(even_list, odd_list):
    numbers = even_list + odd_list
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    print("\nEven numbers list:", even_numbers)
    print("Odd numbers list:", odd_numbers)

# Function to merge and sort two lists
def merge_sort_lists(even_list, odd_list):
    merged_list = even_list + odd_list
    merged_list.sort()
    print("Merged and sorted list:", merged_list)

# Function to update first element with X value and delete the middle element
def update_delete_elements(merged_list):
    if len(merged_list) >= 1:
        merged_list[0] = 'X'
    
    if len(merged_list) % 2 != 0:
        mid_index = len(merged_list) // 2
        del merged_list[mid_index]
    
    print("Updated list:", merged_list)

# Function to find max, min, and occurrences of elements
def find_max_min_occurrences(merged_list):
    print("Maximum number:", max(merged_list))
    print("Minimum number:", min(merged_list))

    search_word = "Python"
    if search_word in merged_list:
        print(f"'{search_word}' is present in the list.")
    else:
        print(f"'{search_word}' is not present in the list.")

# Main program

# Taking input for two lists
even_list = []
odd_list = []

num_elements = int(input("Enter the number of elements for the first list: "))
for i in range(num_elements):
    num = int(input(f"Enter element {i + 1} for the even list: "))
    even_list.append(num)

num_elements = int(input("Enter the number of elements for the second list: "))
for i in range(num_elements):
    num = int(input(f"Enter element {i + 1} for the odd list: "))
    odd_list.append(num)

# Main menu
while True:
    print("\nSelect an option:")
    print("1. Put even and odd elements into two different lists")
    print("2. Merge and sort the two lists")
    print("3. Update first element with 'X' value and delete the middle element")
    print("4. Find max and min element from the list and check for 'Python'")
    print("5. Exit")

    choice = int(input("Enter your choice (1/2/3/4/5): "))

    if choice == 1:
        separate_even_odd(even_list, odd_list)
    elif choice == 2:
        merge_sort_lists(even_list, odd_list)
    elif choice == 3:
        merged_list = even_list + odd_list
        update_delete_elements(merged_list)
    elif choice == 4:
        merged_list = even_list + odd_list
        find_max_min_occurrences(merged_list)
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


