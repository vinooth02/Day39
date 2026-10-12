class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def get_result(self):
        if self.marks >= 35:
            return "Pass"
        else:
            return "Fail"


if __name__ == "__main__":
    student = Student("Riya", 21, 85)

    print("Name:", student.name)
    print("Age:", student.age)
    print("Marks:", student.marks)
    print("Result:", student.get_result())