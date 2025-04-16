class Student:
    def __init__(self, name, family, age):
        self.__name = name
        self.family = family
        self.__age = age

    @property
    def name(self):
        print('name(self) called')
        return self.__name

    @name.setter
    def name(self, new_value):
        print('name(self, new_value called)')
        self.__name = new_value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_value):
        # if new_value >= 0:
        #     self.__age = new_value
        # else:
        #     print('Error')

        assert new_value >= 0
        self.__age = new_value

    @property
    def full_name(self):
        return self.__name + ' ' + self.family

    def __str__(self):
        return f'Student(name = "{self.__name}", family="{self.family}")'


s = Student('name', 'family', 20)
print(s.name)
s.name = 'Another name'
print(s.name)

print('='*50)

print(s.family)
s.family = 'Another family'
print(s.family)

s.age = 10
print(s.age)
try:
    s.age = -10
except:
    print('There was an error')
print(s.age)

print(s)
print(s.full_name)