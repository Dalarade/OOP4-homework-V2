class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            return None
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if len(all_grades) == 0:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        avg = self.average_grade()
        courses_in_progress = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if len(all_grades) == 0:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        avg = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg:.1f}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return None
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")


student_1 = Student('Alice', 'Smith', 'female')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Bob', 'Johnson', 'male')
student_2.courses_in_progress += ['Python', 'Java']
student_2.finished_courses += ['Основы алгоритмов']

lecturer_1 = Lecturer('Ivan', 'Petrov')
lecturer_1.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Maria', 'Sidorova')
lecturer_2.courses_attached += ['Python', 'Java']

reviewer_1 = Reviewer('John', 'Doe')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Jane', 'Roe')
reviewer_2.courses_attached += ['Python', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 8)

reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 9)

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 9)

student_2.rate_lecture(lecturer_1, 'Python', 8)
student_2.rate_lecture(lecturer_1, 'Python', 7)

student_1.rate_lecture(lecturer_2, 'Python', 9)
student_2.rate_lecture(lecturer_2, 'Python', 8)

print("=== СТУДЕНТЫ ===")
print(student_1)
print()
print(student_2)
print()

print("=== ЛЕКТОРЫ ===")
print(lecturer_1)
print()
print(lecturer_2)
print()

print("=== РЕВЬЮЕРЫ ===")
print(reviewer_1)
print()
print(reviewer_2)
print()

print("=== СРАВНЕНИЕ ===")
print(f"student_1 > student_2: {student_1 > student_2}")
print(f"student_1 < student_2: {student_1 < student_2}")
print(f"student_1 == student_2: {student_1 == student_2}")

print(f"lecturer_1 > lecturer_2: {lecturer_1 > lecturer_2}")
print(f"lecturer_1 < lecturer_2: {lecturer_1 < lecturer_2}")
print(f"lecturer_1 == lecturer_2: {lecturer_1 == lecturer_2}")
print()

def average_student_grade(students_list, course_name):
    all_grades = []
    for student in students_list:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    if len(all_grades) == 0:
        return 0
    return sum(all_grades) / len(all_grades)


def average_lecturer_grade(lecturers_list, course_name):
    all_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    if len(all_grades) == 0:
        return 0
    return sum(all_grades) / len(all_grades)


print("=== СРЕДНИЕ ОЦЕНКИ ===")
print(f"Средняя оценка студентов по курсу Python: {average_student_grade([student_1, student_2], 'Python'):.1f}")
print(f"Средняя оценка лекторов по курсу Python: {average_lecturer_grade([lecturer_1, lecturer_2], 'Python'):.1f}")