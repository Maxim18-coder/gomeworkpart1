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