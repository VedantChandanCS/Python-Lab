# Function to count lines, words, and characters in a file
def count_stats(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        num_lines = len(lines)
        
        words = []
        num_words = 0
        for line in lines:
            words += line.split()
        num_words = len(words)
        
        num_chars = sum(len(word) for word in words)
        
        print("\nStatistics for", file_name, ":")
        print("Number of lines:", num_lines)
        print("Number of words:", num_words)
        print("Number of characters:", num_chars)

# File name
file_name = "source_file.txt"

# Create a file to store data for counting statistics
with open(file_name, "w") as file:
    file.write("This is a sample sentence.\n")
    file.write("Another sentence for testing.\n")
    file.write("And a third line to count.\n")

# Call the function to count statistics
count_stats(file_name)
