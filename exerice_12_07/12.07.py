class Student:
    # Constructor
    def __init__(self, name, age, student_id, gpa):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.gpa = gpa


        @property
        def student_name(self):
            print(f'"{self.name}"was accessed.')
            return self.name

        @student_name.setter
        def student_name(self, value):
            print(f'"{self.name}"is now"{value}".')
            self.name = value

        @student_name.deleter
        def student_name(self):
            print(f'"{self.name}" was deleted')
            del self.name
        
        #Example of usage
        if __name__ == "__main__":
            #Creating a new student object
            student1 = Student("Tom Doe",20, "4b0g0066",3.5)

            print(student1.student_name)
            student1.student_name = "Peter Pan"
            del student1.student_name
            print(student1.student_name)