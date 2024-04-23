list = [1, 2, 3, 4, 2, 4, 24, 244]


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            return 'pass'
        else:
            return 'fail'


abir = Student('abir', 49)
kabir = Student('kabir', 79)
sabir = Student('sabir', 19)
pabir = Student('pabir', 75)
samir = Student('samir', 39)


students = [abir, kabir, sabir, pabir, samir]
passStudent = []
failStudent = []

for x in students:
    if x.result() == 'pass':
        passStudent.append(x.name)
    else:
        failStudent.append(x.name)

print("These our brilient student")
for x in passStudent:
    print(x)

print("These are looser")
for x in failStudent:
    print(x)
