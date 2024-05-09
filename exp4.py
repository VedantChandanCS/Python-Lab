def add_student():
    num_students = int(input("Enter the number of students: "))
    students = []

    for _ in range(num_students):
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = tuple(float(input(f"Enter marks for Subject {i + 1}: ")) for i in range(3))
        student_info = (roll_no, name, marks)
        students.append(student_info)

    return students


def display_python_students(students):
    python_students = [student for student in students if "Python" in student[1]]
    if not python_students:
        print("No students with 'Python' in their name.")
    else:
        print("Students with 'Python' in their name:")
        for student in python_students:
            print(f"Roll Number: {student[0]}, Marks: {student[2]}")


def sort_by_name(students):
    sorted_students = sorted(students, key=lambda x: x[1])
    print("Students sorted by name:")
    for student in sorted_students:
        print(f"Roll Number: {student[0]}, Name: {student[1]}, Marks: {student[2]}")


def main():
    students = []

    while True:
        print("\nMenu:")
        print("1. Add Students")
        print("2. Display Python Students")
        print("3. Sort Students by Name")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            students.extend(add_student())
        elif choice == "2":
            display_python_students(students)
        elif choice == "3":
            sort_by_name(students)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()