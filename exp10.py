import sqlite3

# Function to create a new SQLite database
def create_database():
    connection = sqlite3.connect("student_records.db")
    cursor = connection.cursor()
    
    # Create a table for student records
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        age INTEGER,
                        grade TEXT
                    )''')
    
    connection.commit()
    connection.close()
    print("Database and 'students' table created successfully.")

# Function to insert values into the 'students' table
def insert_values():
    connection = sqlite3.connect("student_records.db")
    cursor = connection.cursor()
    
    # User input to add new student records
    print("\nEnter student details:")
    name = input("Name: ")
    age = int(input("Age: "))
    grade = input("Grade: ")
    
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    
    connection.commit()
    connection.close()
    print("New student record added successfully.")

# Function to display all values in the 'students' table
def display_values():
    connection = sqlite3.connect("student_records.db")
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    print("\nStudent Records:")
    print("ID | Name     | Age | Grade")
    print("-" * 30)
    for row in rows:
        print(f"{row[0]:2} | {row[1]:8} | {row[2]:3} | {row[3]:5}")
    
    connection.close()

# Function to update values in the 'students' table
def update_values():
    student_id = int(input("Enter student ID to update grade: "))
    new_grade = input("Enter new grade: ")
    
    connection = sqlite3.connect("student_records.db")
    cursor = connection.cursor()
    
    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
    
    connection.commit()
    connection.close()
    print(f"Grade updated for student with ID {student_id}.")

# Main menu function
def main_menu():
    print("\n===== Student Records Management =====")
    print("1. Create Database")
    print("2. Insert Student Record")
    print("3. Display Student Records")
    print("4. Update Student Grade")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        create_database()
    elif choice == "2":
        insert_values()
    elif choice == "3":
        display_values()
    elif choice == "4":
        update_values()
    elif choice == "5":
        print("Exiting program.")
        exit()
    else:
        print("Invalid choice. Please try again.")

# Main loop
while True:
    main_menu()
