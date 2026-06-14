class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def display_details(self):
        print("Student Name:",self.name)
        print("Student Roll No:",self.roll_no)
        print("Student marks:",self.marks)


    def calculate_grade(self):
        if self.marks >=90:
            grade="A"
        elif self.marks >=80:
            grade="B"
        elif self.marks >=70:
            grade="C"
        elif self.marks >=40:
            grade="D"
        elif self.marks <40:
            grade="Fail"
        else:
            print("Invalid Marks")

        print(f"Grade:{grade}")

s1=Student("Rambo",87,1)
s1.display_details()
s1.calculate_grade()

            
