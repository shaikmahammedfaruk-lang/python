from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def get_details(self):
        pass


class Student(Person):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_details(self):
        return f"Student Name: {self.name}, Grade: {self.grade}"


class Teacher(Person):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def get_details(self):
        return f"Teacher Name: {self.name}, Subject: {self.subject}"


s = Student("Faruk", "A")
t = Teacher("Ali", "Python")

print(s.get_details())
print(t.get_details())