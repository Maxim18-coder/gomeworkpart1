class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_courses = []

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def review_hw(self, student, course, grade):
        # Метод для выставления оценки студенту от эксперта
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Пример использования
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Jane', 'Smith')
cool_reviewer.courses_attached += ['Python']

# Оценка от лектора
cool_lecturer.rate_hw(best_student, 'Python', 10)
cool_lecturer.rate_hw(best_student, 'Python', 8)

# Оценка от эксперта
cool_reviewer.review_hw(best_student, 'Python', 9)

print(best_student.grades)


#Задача 2.
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
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
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
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Пример использования

# Создаем студента
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

# Создаем лектора и прикрепляем курс
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

# Создаем рецензента (Reviewer) и прикрепляем курс
cool_reviewer = Reviewer('John', 'Doe')
cool_reviewer.courses_attached += ['Python']

# Рецензент выставляет оценки студенту
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)

# Студент ставит оценки лектору
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

# Проверяем результаты 
print(f'Оценки студента {best_student.name}: {best_student.grades}')
print(f'Оценки лектора {cool_lecturer.name}: {cool_lecturer.grades}')

#Задача 3.
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
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_courses += len(grades)
        return total_grades / total_courses if total_courses > 0 else 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade():.1f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет"}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses) if self.finished_courses else "Нет"}')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented


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
        total_grades = 0
        total_courses = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_courses += len(grades)
        return total_grades / total_courses if total_courses > 0 else 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade():.1f}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

# Создаем студентов, лекторов и проверяющих
student1 = Student("Ruoy", "Eman", "male")
student1.courses_in_progress.append("Python")
student1.finished_courses.append("Введение в программирование")

lecturer1 = Lecturer("Some", "Buddy")
lecturer1.courses_attached.append("Python")

reviewer1 = Reviewer("Alice", "Smith")
reviewer1.courses_attached.append("Python")

# Выставляем оценки
reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student1, "Python", 9)

lecturer1.grades["Python"] = [8, 9, 10]

# Печатаем информацию
print(student1)
print(lecturer1)
print(reviewer1)

# Сравнение студентов и лекторов
print(student1 < Student("John", "Doe", "male"))  # False
print(lecturer1 < Lecturer("Another", "Lecturer"))  # Сравнение лекторов аналогично

#Задача 4
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
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_courses += len(grades)
        return total_grades / total_courses if total_courses > 0 else 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade():.1f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет"}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses) if self.finished_courses else "Нет"}')

class Lecturer:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []
        self.grades = {}
        
    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_courses += len(grades)
        return total_grades / total_courses if total_courses > 0 else 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade():.1f}')

class Reviewer:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_student_grade(students, course):
    total_grades = 0
    total_students = 0
    
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])
    
    return total_grades / total_students if total_students > 0 else 0

def average_lecturer_grade(lecturers, course):
    total_grades = 0
    total_lecturers = 0
    
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_lecturers += len(lecturer.grades[course])
    
    return total_grades / total_lecturers if total_lecturers > 0 else 0

# Создание экземпляров
student1 = Student("Иван", "Иванов", "мужской")
student1.courses_in_progress = ["Математика", "Физика"]
student1.finished_courses = ["Основы программирования"]

student2 = Student("Анна", "Петрова", "женский")
student2.courses_in_progress = ["Математика", "Химия"]
student2.finished_courses = ["Введение в философию"]

lecturer1 = Lecturer("Сергей", "Сергеев", "мужской")
lecturer1.courses_attached = ["Математика", "Физика"]

lecturer2 = Lecturer("Ольга", "Олегова", "женский")
lecturer2.courses_attached = ["Химия", "Физика"]

reviewer1 = Reviewer("Алексей", "Алексеев", "мужской")
reviewer2 = Reviewer("Мария", "Мариева", "женский")

# Оценки студентов лектору
student1.rate_lecturer(lecturer1, "Математика", 8)
student1.rate_lecturer(lecturer1, "Математика", 9)
student2.rate_lecturer(lecturer2, "Химия", 7)

# Оценка студентов рецензентами
reviewer1.rate_student(student1, "Математика", 10)
reviewer2.rate_student(student2, "Химия", 9)

# Вывод информации об студентах и лекторах
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)

# Подсчет средней оценки студентов по курсу "Математика"
students = [student1, student2]
average_math_grade = average_student_grade(students, "Математика")
print(f'Средняя оценка по курсу "Математика": {average_math_grade:.1f}')

# Подсчет средней оценки лекторов по курсу "Физика"
lecturers = [lecturer1, lecturer2]
average_physics_grade = average_lecturer_grade(lecturers, "Физика")
print(f'Средняя оценка по курсу "Физика": {average_physics_grade:.1f}')