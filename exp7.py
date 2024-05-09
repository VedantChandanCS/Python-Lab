
try:

    file_name = "nonexistent_file.txt"
    

    with open(file_name, 'r') as file:
        for line in file:
            print(line)

except FileNotFoundError as e:
    print("File was not found!\nPlease check that the file exists before running")

finally:
    print("Program execution complete.")
