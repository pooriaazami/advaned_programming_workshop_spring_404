# Author: Pooria Azami
# Eamil: pooriaazami@gmail.com

# encapsulation
# inheritance
# polymorphism
# abstraction

# Student: name, family, student_id
# Professor: name, family, professor_id
# Subject: professor, name, credit, studnet_list

class Person:
    def __init__(self, name, fmaily):
        self.name = name
        self.family = family

class Student:
    def __init__(self, name, family, student_id):
        self.name = name
        self.family = family
        self.student_id = student_id

    def __str__(self):
        return f'Student({self.name}, {self.family}, {self.student_id})'

class Professor:
    def __init__(self, name, family, professor_id):
        self.name = name
        self.family = family
        self.professor_id = professor_id

class Subject:
    def __init__(self, name, credit, professor):
        self.name = name
        self.credit = credit
        self.professor = professor
        self.student_list = []

    def enroll(self, student):
        self.student_list.append(student)

    def print_names_list(self):
        for student in self.student_list:
            print(student)


stu1 = Student('name1', 'family1', 1)
stu2 = Student('name2', 'family2', 2)
stu3 = Student('name3', 'family3', 3)
stu4 = Student('name4', 'family4', 4)
stu5 = Student('name5', 'family5', 5)
stu6 = Student('name6', 'family6', 6)

prof1 = Professor('name1', 'family1', 1)
prof1 = Professor('name2', 'family2', 2)
prof1 = Professor('name3', 'family3', 3)

subject1 = Subject('s1', 3, prof1)
subject1.enroll(stu1)
subject1.enroll(stu2)
subject1.enroll(stu3)

subject2 = Subject('s2', 3, prof1)
subject2.enroll(stu3)
subject2.enroll(stu4)
subject2.enroll(stu5)

subject3 = Subject('s3', 3, prof1)
subject3.enroll(stu1)
subject3.enroll(stu5)
subject3.enroll(stu6)

s = str(stu1)

print('Subject 1:')
subject1.print_names_list()

print('Subject 2:')
subject2.print_names_list()

print('Subject 3:')
subject3.print_names_list()

