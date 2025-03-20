class Employee:
    A = 1
    @classmethod
    def show(cls):
        print(f"The Class Alltributes of a is {cls.A}")

A = Employee()
A.A = 388


A.show()