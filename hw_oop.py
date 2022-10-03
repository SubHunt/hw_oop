class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'такой лектор не найден'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}


class Lecturer(Mentor):
    pass
    # def __init__(self, name, surname):
    #     self.name = name
    #     self.surname = surname
    #     self.grades = {}
# class Lecturer(Mentor):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.grades = {}

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'такой студент не найден'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

best_student2 = Student('Ruoy2', 'Eman2', 'your_gender2')
best_student2.courses_in_progress += ['Python']


cool_reviewer = Reviewer('Neo', 'Matrix')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

best_lecturer = Lecturer('Urfin', 'Juss')
best_lecturer.courses_attached += ['Python']
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 10)

best_lecturer2 = Lecturer('Urfin2', 'Juss2')
best_lecturer2.courses_attached += ['Python2']
best_student2.rate_lecturer(best_lecturer, 'Python', 10)
best_student2.rate_lecturer(best_lecturer, 'Python', 20)
best_student2.rate_lecturer(best_lecturer, 'Python', 10)
print(best_lecturer.surname)
print(best_lecturer.grades)
print(best_lecturer2.grades)
