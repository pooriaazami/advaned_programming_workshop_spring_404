# encapsulation
# inheritance
# polymorphism
# abstraction

# Golang - Rust

# Student: name, family, student_id
# Professor: name, family, professor_id
# Course: name, professor, credit, student_list

# __new__
# __init__

# __add__ __radd__ __iadd__
# __sub__ rsub__ __isub__
# __mul__
# __div__
# __divfloor__
# __pow__

# __xor__
# __or__

# __str__
# __repr__
# __len__
# __getitem__ c[0]
# __setitem__ c[0] = 10

# __eq__ ==
# __ne__ !=
# __ lt__ <
# __gr__ >
# __le__ <=
# __ge__ >=

# __hash__

# __next__ for x in <MY_OBJECT>
# __iter__

# __contains__

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

class Course:
    def __init__(self, name, credit, professor):
        self.name = name
        self.credit = credit
        self.professor = professor
        self.student_list = []

    def enroll(self, student):
        self.student_list.append(student)

    def show(self):
        for stu in self.student_list:
            print(stu)

stu1 = Student('name1', 'family1', 1)
stu2 = Student('name2', 'family2', 2)
stu3 = Student('name3', 'family3', 3)
stu4 = Student('name4', 'family4', 4)
stu5 = Student('name5', 'family5', 5)
stu6 = Student('name6', 'family6', 6)

prof1 = Professor('name1', 'family1', 1)
prof2 = Professor('name2', 'family2', 2)
prof3 = Professor('name3', 'family3', 3)

course1 = Course('c1', 3, prof1)
course2 = Course('c2', 3, prof1)
course3 = Course('c3', 3, prof2)
course4 = Course('c4', 3, prof3)

course1.enroll(stu1)
course1.enroll(stu2)
course1.enroll(stu3)

course2.enroll(stu4)
course2.enroll(stu5)
course2.enroll(stu6)

course3.enroll(stu1)
course3.enroll(stu5)
course3.enroll(stu6)

print('Course 1:')
course1.show()

print('Course 2:')
course2.show()

print('Course 3:')
course3.show()

