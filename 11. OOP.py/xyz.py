class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __str__(self):
        return f"My name is {self.name} and marks is {self.marks}"
s=Student("ABC",22)
print(s)
