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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


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


student = Student('Алёхина', 'Ольга', 'Ж')
student.courses_in_progress += ['Python', 'Java']

lecturer = Lecturer('Иван', 'Иванов')
lecturer.courses_attached += ['Python', 'C++']

reviewer = Reviewer('Пётр', 'Петров')
reviewer.courses_attached += ['Python', 'C++']

print("=== ДЕМОНСТРАЦИЯ rate_lecture ===\n")

print("1. Успешная оценка (студент на Python, лектор ведёт Python):")
print(student.rate_lecture(lecturer, 'Python', 7))  # None

print("\n2. Ошибка: студент НЕ записан на курс Java:")
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка

print("\n3. Ошибка: лектор НЕ ведёт курс С++:")
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка

print("\n4. Ошибка: передан Reviewer, а не Lecturer:")
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

print("\n5. Итоговые оценки лектора (только за Python):")
print(lecturer.grades)  # {'Python': [7]}