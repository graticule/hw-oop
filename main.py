class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Задание 3. __str__ для Student
    def __str__(self):
        return '\n'.join([f'Имя: {self.name}',
                          f'Фамилия: {self.surname}',
                          f'Средняя оценка за домашние задания: {self.__mean_grade():.1f}',
                          f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}',
                          f'Завершенные курсы: {", ".join(self.finished_courses)}'])

    def __mean_grade(self):
        result = 0
        all_grades = []
        for v in self.grades.values():
            all_grades.extend(v)
        if all_grades:
            result = sum(all_grades)/len(all_grades)
        return result

    # Задание 3. Сравнение для Student
    def __gt__(self, other):
        if isinstance(other, Student):
            return self.__mean_grade() > other.__mean_grade()
        else:
            return 'Ошибка' # ?

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.__mean_grade() < other.__mean_grade()
        else:
            return 'Ошибка' # ?

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.__mean_grade() >= other.__mean_grade()
        else:
            return 'Ошибка' # ?

    def __le__(self, other):
        if isinstance(other, Student):
            return self.__mean_grade() <= other.__mean_grade()
        else:
            return 'Ошибка' # ?

    # Задание 2. Student выставляет оценку Lecturer
    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            lecturer.grades.setdefault(course, []).append(grade)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Задание 1. Lecturer и Reviewer - наследники Mentor
class Lecturer(Mentor):
    # Задание 2. Lecturer получают оценки от студентов
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Задание 3. __str__ для Lecturer
    def __str__(self):
        return '\n'.join([f'Имя: {self.name}',
                          f'Фамилия: {self.surname}',
                          f'Средняя оценка за лекции: {self.__mean_grade():.1f}'])

    def __mean_grade(self):
        result = 0
        all_grades = []
        for v in self.grades.values():
            all_grades.extend(v)
        if all_grades:
            result = sum(all_grades)/len(all_grades)
        return result

    # Задание 3. Сравнение для Lecturer
    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.__mean_grade() > other.__mean_grade()
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.__mean_grade() < other.__mean_grade()
        else:
            return 'Ошибка'

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.__mean_grade() >= other.__mean_grade()
        else:
            return 'Ошибка'

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.__mean_grade() <= other.__mean_grade()
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    # Задание 2. Reviewer выставляет оценки студентам
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Задание 3. __str__ для Reviewer
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Задание 4. Функции для средних оценок
def mean_student_grade_for_course(students, course):
    result = 0
    grades = []
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            grades.extend(student.grades.get(course, []))
    if grades:
        result = sum(grades) / len(grades)
    return result


def mean_lecturer_grade_for_course(lecturers, course):
    result = 0
    grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            grades.extend(lecturer.grades.get(course, []))
    if grades:
        result = sum(grades) / len(grades)
    return result


# Задание 4
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Git', 'Введение в программирование']
student2 = Student('Hi', 'Howareyou', 'male')
student2.courses_in_progress += ['Python', 'Git']

reviewer1 = Reviewer('Good', 'Reviewer')
reviewer1.courses_attached += ['Python', 'Введение в программирование']
reviewer2 = Reviewer('Bad', 'Reviewer')
reviewer2.courses_attached += ['Python','Git']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 6)
reviewer2.rate_hw(student1, 'Python', 1)
reviewer2.rate_hw(student1, 'Python', 2)
reviewer2.rate_hw(student1, 'Python', 2)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 4)
reviewer2.rate_hw(student2, 'Python', 4)
reviewer2.rate_hw(student2, 'Python', 4)
reviewer2.rate_hw(student1, 'Git', 6)
reviewer2.rate_hw(student2, 'Git', 6)

print('student1\'s grades:')
print(student1.grades)
print('student2\'s grades:')
print(student2.grades)
print('mean student grade for Git:')
print(mean_student_grade_for_course([student1, student2], 'Git'))
print('mean student grade for Введение в программирование:')
print(mean_student_grade_for_course([student1, student2], 'Введение в программирование'))

lecturer1 = Lecturer('Cool', 'Lecturer')
lecturer1.courses_attached += ['Git', 'Python', 'Введение в программирование']
lecturer2 = Lecturer('Other', 'Lecturer')
lecturer2.courses_attached += ['Python', 'Введение в программирование']

student1.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Git', 9)

print('lecturer1\'s grades:')
print(lecturer1.grades)
print('lecturer2\'s grades:')
print(lecturer2.grades)
print('lecturer1 < lecturer2 =', lecturer1 < lecturer2)
print('lecturer1 < lecturer2 =', lecturer1 < reviewer2)

print(mean_lecturer_grade_for_course([lecturer1, reviewer1, lecturer2], 'Python'))

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)