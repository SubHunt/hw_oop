class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
                course in lecturer.courses_attached and \
                course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка!')

    def _middle_rate(self):
        average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return average

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        return f'Студент:\n' \
               f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self._middle_rate()}\n'\
               f'Курсы в процессе изучения: {courses_in_progress_string}\n' \
               f'Завершенные курсы: {finished_courses_string}\n'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Некорректное сравнение.')
            return
        print(self._middle_rate(), '<', other._middle_rate())
        return self._middle_rate() < other._middle_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}


class Lecturer(Mentor):
    def _middle_rate(self):
        average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return average

    def __str__(self):
        return f'Лектор:\n' \
               f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self._middle_rate()}\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректное сравнение.')
            return
        print(self._middle_rate(), '<',  other._middle_rate())
        return self._middle_rate() < other._middle_rate()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка!')

    def __str__(self):
        return f'Проверяющий:\n' \
               f'Имя: {self.name}\nФамилия: {self.surname}\n'


def average_lectors(all_lectors):
    total_mark = 0
    count = 0
    for lector in all_lectors:
        total_mark += sum(sum(lector.values(), []))
        count += len(sum(lector.values(), []))
    return round(total_mark / count, 1)


def average_students(all_students):
    total_mark = 0
    count = 0
    for student in all_students:
        total_mark += sum(sum(student.values(), []))
        count += len(sum(student.values(), []))
    return round(total_mark / count, 1)


# Creating 2 students, add full name, gender, courses in progress
first_student = Student('Иван', 'Иванов', 'мужской')
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['Git']
second_student = Student('Вася', 'Васечкин', 'мужской')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Введение в Python']

# Creating 2 reviewers, add full name, courses in progress
first_reviewer = Reviewer('Сидр', 'Сидоров')
first_reviewer.courses_attached += ['Python']
second_reviewer = Reviewer('Петр', 'Петров')
second_reviewer.courses_attached += ['Python']

# Creating 2 lecturers, add full name, courses in progress
first_lecturer = Lecturer('Стив', 'Джобс')
first_lecturer.courses_attached += ['Python']
second_lecturer = Lecturer('Гвидо', ' ван Россум')
second_lecturer.courses_attached += ['Python']

# Add marks for different students from different reviewrs
first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(second_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(second_student, 'Python', 9)

# Add marks for different lecturers from different students. Marks add different for better contrast only :)
first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(second_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 9)
second_student.rate_lecturer(first_lecturer, 'Python', 10)
second_student.rate_lecturer(second_lecturer, 'Python', 10)

# redefine function print
print(first_student)
print(second_student)

print(first_reviewer)
print(second_reviewer)

print(first_lecturer)
print(second_lecturer)

# Comparing average marks
print(first_student < second_student)
print(second_student < first_student)
print(first_lecturer < second_lecturer)

# average all marks lectors
lector_list = [first_lecturer.grades, second_lecturer.grades]
student_list = [first_student.grades, second_student.grades]
print(f'Средняя оценка всех лекторов: {average_lectors(lector_list)}')
print(f'Средняя оценка всех студентов: {average_students(student_list)}')
