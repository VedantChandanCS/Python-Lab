import os

def display_files_in_current_directory():
    current_directory = os.getcwd()  # Get the current working directory
    print("Files available in the current directory:")
    
    for file_name in os.listdir(current_directory):
        if os.path.isfile(os.path.join(current_directory, file_name)):
            print(file_name)

# Call the function to display files in the current directory
display_files_in_current_directory()
