class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def display_details(self):
        print("Person ID:", self.person_id)
        print("Name:", self.name)


class Student(Person):
    def __init__(self, person_id, name, marks, *args):
        super().__init__(person_id, name)
        self.marks = marks
        if len(args) > 0:
            self.sport_marks = args[0]
        else:
            self.sport_marks = None

    def display_details(self):
        super().display_details()
        if self.sport_marks is not None:
            print("Sports Marks:", self.sport_marks)
        else:
            print("No sports marks available for this student")
        self.display_result()

    def display_result(self):
        if self.sport_marks is not None:
            total_marks = self.marks+ self.sport_marks
            # average_marks = total_marks / len(self.sport_marks)
            print("Total Marks:", total_marks)
            # print("Average Marks:", average_marks)
        elif self.sport_marks is None:
            print("Total Marks: ", self.marks)
        else:
            print("Student does not have any sports marks")


# Creating an instance of Student with sports marks
student1 = Student(101, "Alice", 72, 15)
student1.display_details()
print()

# Creating an instance of Student without sports marks
student2 = Student(102, "Bob", 88)
student2.display_details()


