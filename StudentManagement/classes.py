def get_next_id(role):
    filename = f"{role}_id.txt"
    try:
        with open(filename, "r") as f:
            current_id = int(f.read())
    except FileNotFoundError:
        current_id = 0

    with open(filename, "w") as f:
        f.write(str(current_id + 1))

    return current_id




class Person:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def input(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def save(self):
        return f"{self.id},{self.name},{self.age}"



class Student(Person):
    def __init__(self, name='', age=0):
        super().__init__(name, age)
        self.marks = {} 
        self.average = 0
        self.grade = 'F'
        self.id = get_next_id("student")

    def input(self):
        super().input()
        num_subjects = int(input("Enter the number of subjects: "))
        for _ in range(num_subjects):
            subject = input("Enter subject name: ")
            mark = int(input(f"Enter mark for {subject}: "))
            self.marks[subject] = mark
        self.calculate_grade()

    def calculate_average(self):
        total_marks = sum(self.marks.values())
        self.average = total_marks / len(self.marks) if self.marks else 0
        return self.average

    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            self.grade = 'A'
        elif average >= 80:
            self.grade = 'B'
        elif average >= 70:
            self.grade = 'C'
        elif average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def display(self):
        super().display()
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print(f"Average: {self.average}")
        print(f"Grade: {self.grade}")


    def save(self):
        person_data = super().save()
        marks_data = ';'.join([f"{subject}:{mark}" for subject, mark in self.marks.items()])
        return f"{person_data},{marks_data},{self.average},{self.grade}"







class Teacher(Person):
    def __init__(self, name='', age=0):
        super().__init__(name, age)
        self.subject = ''
        self.id = get_next_id("teacher")
 

    def input(self):
        super().input()
        self.subject = input("Enter subject name: ")


    def display(self):
        super().display()
        print(f"Subject: {self.subject}")
        


    def save(self):
        person_data = super().save()
        return f"{person_data},{self.subject}"
    


        
class ManagementSystem:
    def __init__(self):
        self.students = []
        self.teachers=[]
    def add_student(self):
        student = Student()
        student.input() 
        self.students.append(student)
        print("Student added successfully.")
        self.save_to_file()

    def save_to_file(self):
        with open("students.txt", "a") as file:
            for student in self.students:
                file.write(student.save() + "\n")

    def display_students(self):
     with open("students.txt", "r") as file:
        lines = file.readlines()  
        if not lines:
            print("There are no students.")
            return
        
        print("\nStudents")
        for line in lines:
            if line.strip() == "":
                continue

            data = line.strip().split(",")
            if len(data) < 6:
                print("Skipping malformed line:", line.strip())
                continue 

            student_id = data[0]
            name = data[1]
            age = data[2]
            marks = data[3]
            average = data[4]
            grade = data[5]

            print(f"\nStudent ID: {student_id}")
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"Average: {average}")
            print(f"Grade: {grade}")
            
            print("Marks:")
            subjects = marks.split(";")
            for subject in subjects:
                if ":" in subject:
                    subject_name, mark = subject.split(":")
                    print(f"  {subject_name}: {mark}")


    def add_teacher(self):
        teacher = Teacher()
        teacher.input()
        self.teachers.append(teacher)
        print("Teacher added successfully.")
        self.save_teachers_to_file()

    def save_teachers_to_file(self):
        with open("teachers.txt", "a") as file:
            for teacher in self.teachers:
                file.write(teacher.save() + "\n")

    def display_teachers(self):
     with open("teachers.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print("There are no teachers.")
            return

        print("\nTeachers")
        for line in lines:
            if line.strip() == "":
                continue 

            data = line.strip().split(",")
            if len(data) < 4:
                print("Skipping malformed line:", line.strip())
                continue 

            teacher_id = data[0]
            name = data[1]
            age = data[2]
            subject = data[3]

            print(f"\nTeacher ID: {teacher_id}")
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"Subject: {subject}")





