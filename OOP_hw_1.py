class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress and (0 < grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка при внесении данных о курсе или оценке Лекции')
            return 'Ошибка'

    def get_average_grade(self):
        list_ = []
        for i, grades_list in self.grades.items():
            list_.extend(grades_list)
        if list_:
            avg_grade = sum(list_) / len(list_)
            return avg_grade
        return 0

    def __lt__(self, other):
        if (not isinstance(self, Student)) or (not isinstance(other, Student)):
            return 'Ошибка'
        if other.get_average_grade() < self.get_average_grade():
            print(f"Средний балл выше у студента: {self.name}")
        else:
            print(f"Средний балл выше у студента: {other.name}")

    def __str__(self):
        return (
            f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: "
            f"{self.get_average_grade()}\nКурсы в "
            f"процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные "
            f"курсы: {', '.join(self.finished_courses)}")


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        list_ = []
        for i, grades_list in self.grades.items():
            list_.extend(grades_list)
        if list_:
            avg_grade = sum(list_) / len(list_)
            return avg_grade
        return 0.

    def __lt__(self, other):
        if (not isinstance(self, Lecturer)) or (not isinstance(other, Lecturer)):
            return 'Ошибка'
        if other.get_average_grade() < self.get_average_grade():
            print(f"Средний балл выше у лектора: {self.name}")
        else:
            print(f"Средний балл выше у лектора: {other.name}")

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}"


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and (
                0 < grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка при внесении данных о курсе или оценке ДЗ')
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Создаем студентов
student_1 = Student("Ivan", "Ivanov", "male")
student_1.add_courses("Введение в программирование")
student_1.courses_in_progress += ["Python", "Git"]

student_2 = Student("Oleg", "Olegov", "male")
student_2.add_courses("Введение в программирование")
student_2.courses_in_progress += ["Python", "Git"]

# Создаем лекторов
lecturer_1 = Lecturer("Some", "Buddy")
lecturer_1.courses_attached += ["Python"]

lecturer_2 = Lecturer("Buddy", "Some")
lecturer_2.courses_attached += ["Git"]

# Создаем проверяющих
reviewer_1 = Reviewer("Py", "Thon")
reviewer_1.courses_attached += ["Python"]

reviewer_2 = Reviewer("Git", "Hub")
reviewer_2.courses_attached += ["Git"]

# Выставляем оценки лекторам
student_1.rate_lecturer(lecturer_1, "Python", 10)
student_1.rate_lecturer(lecturer_1, "Python", 8)
student_1.rate_lecturer(lecturer_2, "Git", 8)
student_1.rate_lecturer(lecturer_2, "Git", 9)

student_2.rate_lecturer(lecturer_1, "Python", 9)
student_2.rate_lecturer(lecturer_1, "Python", 10)
student_2.rate_lecturer(lecturer_2, "Git", 10)
student_2.rate_lecturer(lecturer_2, "Git", 6)

# Выставляем оценки студентам
reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_1.rate_hw(student_1, "Python", 10)

reviewer_2.rate_hw(student_1, "Git", 8)
reviewer_2.rate_hw(student_1, "Git", 9)

reviewer_1.rate_hw(student_2, "Python", 9)
reviewer_1.rate_hw(student_2, "Python", 8)

reviewer_2.rate_hw(student_2, "Git", 10)
reviewer_2.rate_hw(student_2, "Git", 9)

# Студенты
print(f"Список студентов:\n\n{student_1}\n\n{student_2}")
print()

# Лекторы
print(f"Список лекторов:\n\n{lecturer_1}\n\n{lecturer_2}")
print()

# Проверяющие
print(f"Список проверяющих:\n\n{reviewer_1}\n\n{reviewer_2}")
print()
print()

# Сравниваем студентов и сравниваем лекторов
student_1.__lt__(student_2)
print()
lecturer_1.__lt__(lecturer_2)
print()

students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]


def students_rating(some_students_list, course_name):
    sum_grades = 0
    total = 0
    for student in students_list:
        if course_name in student.courses_in_progress:
            for grade in student.grades[course_name]:
                sum_grades += grade
                total += 1
    average_all_students = float(sum_grades / total)
    return f"{average_all_students:.2f}"


def lecturers_rating(some_lecturers_list, course_name):
    sum_grades = 0
    total = 0
    for lecturer in lecturers_list:
        if course_name in lecturer.courses_attached:
            for grade in lecturer.grades[course_name]:
                sum_grades += grade
                total += 1
    average_all_lecturers = float(sum_grades / total)
    return f"{average_all_lecturers:.2f}"


print(f"Средняя оценка всех студентов по курсу {'Python'}: {students_rating(students_list, 'Python')}")
print()
print(f"Средняя оценка всех студентов по курсу {'Git'}: {students_rating(students_list, 'Git')}")
print()
print(f"Средняя оценка всех лекторов по курсу {'Python'}: {lecturers_rating(lecturers_list, 'Python')}")
print()
print(f"Средняя оценка всех лекторов по курсу {'Git'}: {lecturers_rating(lecturers_list, 'Git')}")
