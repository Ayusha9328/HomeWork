class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course not in lecturer.grades:
                lecturer.grades[course] = []  # Инициализируем список оценок
            lecturer.grades[course].append(grade)  # Добавляем оценку

    def average_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count > 0 else 0        

    def __str__(self):
        return (f"Имя: {self.name}, Фамилия: {self.surname}, "
                f"Средняя оценка за домашние задания: {self.average_grade()}, "
                f"Курсы в процессе изучения: {self.courses_in_progress}, "
                f"Завершенные курсы: {self.finished_courses}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} 

    def average_grade(self):
        total = 0
        count = 0
        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)
        return total / count if count > 0 else 0 

    def __str__(self):
        return (f"Имя: {self.name}, Фамилия: {self.surname}, "
                f"Средняя оценка за лекции: {self.average_grade()}")


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)  # Добавляем оценку
            else:
                student.grades[course] = [grade]  # Инициализируем список оценок
        else:
            return 'Ошибка'       
      
# Пример использования
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses = ['Введение в программирование']
print(best_student)

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

lecturer1 = Lecturer("Иванов", "И.И.")  # Добавляем surname
best_student.rate_lecturer(lecturer1, 'Python', 9)
best_student.rate_lecturer(lecturer1, 'Python', 5)
best_student.rate_lecturer(lecturer1, 'Python', 10)

# Проверка
print('Оценки студента:', best_student.grades)  
print('Оценки лектора:', lecturer1.grades)     

print(f'Средняя оценка студента: {best_student.average_grade()}')  # Вычисление средней оценки студента
print(f'Средняя оценка лектора: {lecturer1.average_grade()}')  # Вычисление средней оценки лектора
