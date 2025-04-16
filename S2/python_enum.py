from enum import Enum

class ROLE(Enum):
    STUDENT = 1
    TEACHER = 2
    STAFF = 3


role = ROLE.STUDENT # Student, Teacher, Staff
print(role)