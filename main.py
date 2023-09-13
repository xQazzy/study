class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            # Проверяем, существует ли ключ для данного курса в словаре оценок лектора
            if course not in lecturer.grades:
                lecturer.grades[course] = []
            # Добавляем оценку в список оценок лектора
            lecturer.grades[course].append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        avg_hw_grade = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades)
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_hw_grade:.1f}\n" \
               f"Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() < other.calculate_average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() <= other.calculate_average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() > other.calculate_average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() >= other.calculate_average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() == other.calculate_average_grade()
        return False

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() != other.calculate_average_grade()
        return True

    def calculate_average_grade(self):
        # Рассчет средней оценки за домашние задания
        total_grade = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grade / total_count if total_count > 0 else 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_lecture_grade = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_lecture_grade:.1f}"

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() < other.calculate_average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() <= other.calculate_average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() > other.calculate_average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() >= other.calculate_average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() == other.calculate_average_grade()
        return False

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() != other.calculate_average_grade()
        return True

    def calculate_average_grade(self):
        # Рассчет средней оценки за лекции
        total_grade = sum(sum(grades) for grades in self.grades.values())
        total_count = sum(len(grades) for grades in self.grades.values())
        return total_grade / total_count if total_count > 0 else 0


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Примеры использования
student1 = Student('John', 'Doe', 'Мужской')
student1.courses_in_progress = ['Python', 'JavaScript']
student1.finished_courses = ['Web разработка']
student1.grades = {'Python': [8, 7, 9], 'JavaScript': [10, 9, 8]}

student2 = Student('Ruoy', 'Eman', 'your_gender')
student2.courses_in_progress = ['Python', 'Git']
student2.finished_courses = ['Введение в программирование']
student2.grades = {'Python': [9, 8, 7], 'Git': [10, 9, 9]}

# Создаем лекторов
lecturer1 = Lecturer('Professor', 'Short')
lecturer1.courses_attached = ['Python', 'JavaScript']
lecturer1.grades = {'Python': [9, 8, 10], 'JavaScript': [8, 9, 7]}

lecturer2 = Lecturer('Dr.', 'Johnson')
lecturer2.courses_attached = ['Python', 'Git']
lecturer2.grades = {'Python': [8, 9, 9], 'Git': [7, 8, 10]}

# Создаем рецензоров
reviewer1 = Reviewer('Mr.', 'Smith')
reviewer1.courses_attached = ['Python', 'JavaScript']

reviewer2 = Reviewer('Mrs.', 'Smith')
reviewer2.courses_attached = ['Python', 'Git']

# Вызываем методы
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'JavaScript', 8)
student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer1, 'JavaScript', 7)

student1.rate_lecturer(lecturer2, 'Python', 8)
student1.rate_lecturer(lecturer2, 'Git', 9)
student2.rate_lecturer(lecturer2, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Git', 10)

reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'JavaScript', 8)
reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'Git', 7)

reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'JavaScript', 9)
reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Git', 9)


# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def calculate_average_hw_grade(students, course):
    total_grade = 0
    total_count = 0
    for student in students:
        if course in student.courses_in_progress and course in student.grades:
            total_grade += sum(student.grades[course])
            total_count += len(student.grades[course])
    return total_grade / total_count if total_count > 0 else 0


# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def calculate_average_lecture_grade(lecturers, course):
    total_grade = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached and course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    return total_grade / total_count if total_count > 0 else 0


# Вызываем функции и выводим результаты
python_students = [student1, student2]
python_lecturers = [lecturer1, lecturer2]

average_hw_grade = calculate_average_hw_grade(python_students, 'Python')
average_lecture_grade = calculate_average_lecture_grade(python_lecturers, 'Python')

print(student1)
print(lecturer2)
print(reviewer1)
print(student1 < student2)
print(lecturer1 > lecturer2)
print(f"Средняя оценка за домашние задания по курсу 'Python': {average_hw_grade:.2f}")
print(f"Средняя оценка за лекции по курсу 'Python': {average_lecture_grade:.2f}")