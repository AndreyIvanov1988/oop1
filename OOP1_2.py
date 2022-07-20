print('________________________________Задание 1_________________________________')

# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
        
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
        
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'

# class Lecturer(Mentor):
#   def __init__(self, name, surname):
#     super().__init__(name, surname)
#   pass

# class Rewiewer(Mentor):
#   def __init__(self, name, surname):
#     super().__init__(name, surname)
#   pass
 
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)

print('________________________________Задание 2_________________________________')

# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}

#     def rate_lec(self, lecturer, course, grade):
#         if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
#             if course in lecturer.grades:
#                 lecturer.grades[course] += [grade]
#             else:
#                 lecturer.grades[course] = [grade]
#         else:
#             return 'Ошибка'    
        
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
        
    

# class Lecturer(Mentor):
#   def __init__(self, name, surname):
#     super().__init__(name, surname)
#     self.grades = {}
  

# class Rewiewer(Mentor):
#   def __init__(self, name, surname):
#     super().__init__(name, surname)

#   def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
  
 
# student1 = Student('Harry', 'Potter', 'male')
# student1.courses_in_progress += ['Python']
# student1.courses_in_progress += ['Git']
# student1.finished_courses += ['Программирование для начинающих']

# student2 = Student('Hermione' , 'Granger', 'female')
# student2.courses_in_progress += ['Python']
# student2.courses_in_progress += ['Git']
# student2.courses_in_progress += ['Веб-дизайн для новичков']

# rewiewer1 = Rewiewer('Severus', 'Snape')
# rewiewer1.courses_attached += ['Python']

# rewiewer2 = Rewiewer('Albus', 'Dumbledore')
# rewiewer2.courses_attached += ['Git']

# rewiewer1.rate_hw(student1, 'Python', 7)
# rewiewer1.rate_hw(student1, 'Python', 6)
# rewiewer1.rate_hw(student1, 'Python', 8)

# rewiewer1.rate_hw(student2, 'Python', 9)
# rewiewer1.rate_hw(student2, 'Python', 10)
# rewiewer1.rate_hw(student2, 'Python', 8)

# rewiewer2.rate_hw(student1, 'Git', 5)
# rewiewer2.rate_hw(student1, 'Git', 8)
# rewiewer2.rate_hw(student1, 'Git', 7)

# rewiewer2.rate_hw(student2, 'Git', 7)
# rewiewer2.rate_hw(student2, 'Git', 9)
# rewiewer2.rate_hw(student2, 'Git', 10)


# lecturer1 = Lecturer('Minerva', 'Mcgonagal')
# lecturer1.courses_attached += ['Python']
# lecturer1.courses_attached += ['Git']

# lecturer2 = Lecturer('Remus', 'Lupin')
# lecturer2.courses_attached += ['Python']
# lecturer2.courses_attached += ['Git']

# student1.rate_lec(lecturer1, 'Python', 8)
# student1.rate_lec(lecturer1, 'Python', 9)
# student1.rate_lec(lecturer1, 'Python', 8)
# student1.rate_lec(lecturer1, 'Git', 10)
# student1.rate_lec(lecturer1, 'Git', 9)
# student1.rate_lec(lecturer1, 'Git', 6)

# student2.rate_lec(lecturer2, 'Git', 10)
# student2.rate_lec(lecturer2, 'Git', 9)
# student2.rate_lec(lecturer2, 'Git', 10)
# student2.rate_lec(lecturer1, 'Python', 5)
# student2.rate_lec(lecturer1, 'Python', 6)
# student2.rate_lec(lecturer1, 'Python', 8)

# students = [student1, student2]
# lecturers = [lecturer1, lecturer2]


# print(student1)
# print(student2)
# print(rewiewer1)
# print(rewiewer2)
# print(lecturer1)
# print(lecturer2)


print('________________________________Задание 3_________________________________')

# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}

#     def rate_lec(self, lecturer, course, grade):
#         if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
#             if course in lecturer.grades:
#                 lecturer.grades[course] += [grade]
#             else:
#                 lecturer.grades[course] = [grade]
#         else:
#             return 'Ошибка'   

#     def average_hw(self):
#         count = 0
#         for grades_key in self.grades:
#             count += len(self.grades[grades_key])
#         self.average_homework = round((sum(map(sum, self.grades.values())) / count), 2)
#         return self.average_homework

#     def __lt__(self, other):
#       if not isinstance(other, Student):
#             print('Not a Student!')
#             return
#       return self.average_hw() < other.average_hw()

#     def __str__(self):
#         res = f'''Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_hw()}
# Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
# Завершенные курсы: {', '.join(self.finished_courses)}'''
#         return res
        
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
        
    

# class Lecturer(Mentor):
#   def __init__(self, name, surname):
#     super().__init__(name, surname)
#     self.grades = {}

#   def average_rating(self):
#         count = 0
#         for grades_key in self.grades:
#             count += len(self.grades[grades_key])
#         self.average_grades = round((sum(map(sum, self.grades.values())) / count), 2)
#         return self.average_grades

#   def __lt__(self, other):
#         if not isinstance(other, Lecturer):
#             print('Not a Lecturer!')
#             return
#         return self.average_rating() < other.average_rating()
  
#   def __str__(self):
#         res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'
#         return res


# class Rewiewer(Mentor):
#   def __init__(self, name, surname):
#     super().__init__(name, surname)

#   def __str__(self):
#         res = f'Имя: {self.name} \nФамилия: {self.surname}'
#         return res

#   def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
  
 
# student1 = Student('Harry', 'Potter', 'male')
# student1.courses_in_progress += ['Python']
# student1.courses_in_progress += ['Git']
# student1.finished_courses += ['Программирование для начинающих']

# student2 = Student('Hermione' , 'Granger', 'female')
# student2.courses_in_progress += ['Python']
# student2.courses_in_progress += ['Git']
# student2.courses_in_progress += ['Веб-дизайн для новичков']

# rewiewer1 = Rewiewer('Severus', 'Snape')
# rewiewer1.courses_attached += ['Python']

# rewiewer2 = Rewiewer('Albus', 'Dumbledore')
# rewiewer2.courses_attached += ['Git']

# rewiewer1.rate_hw(student1, 'Python', 7)
# rewiewer1.rate_hw(student1, 'Python', 6)
# rewiewer1.rate_hw(student1, 'Python', 8)

# rewiewer1.rate_hw(student2, 'Python', 9)
# rewiewer1.rate_hw(student2, 'Python', 10)
# rewiewer1.rate_hw(student2, 'Python', 8)

# rewiewer2.rate_hw(student1, 'Git', 5)
# rewiewer2.rate_hw(student1, 'Git', 8)
# rewiewer2.rate_hw(student1, 'Git', 7)

# rewiewer2.rate_hw(student2, 'Git', 7)
# rewiewer2.rate_hw(student2, 'Git', 9)
# rewiewer2.rate_hw(student2, 'Git', 10)


# lecturer1 = Lecturer('Minerva', 'Mcgonagal')
# lecturer1.courses_attached += ['Python']
# lecturer1.courses_attached += ['Git']

# lecturer2 = Lecturer('Remus', 'Lupin')
# lecturer2.courses_attached += ['Python']
# lecturer2.courses_attached += ['Git']

# student1.rate_lec(lecturer1, 'Python', 8)
# student1.rate_lec(lecturer1, 'Python', 9)
# student1.rate_lec(lecturer1, 'Python', 8)
# student1.rate_lec(lecturer1, 'Git', 10)
# student1.rate_lec(lecturer1, 'Git', 9)
# student1.rate_lec(lecturer1, 'Git', 6)

# student2.rate_lec(lecturer2, 'Git', 10)
# student2.rate_lec(lecturer2, 'Git', 9)
# student2.rate_lec(lecturer2, 'Git', 10)
# student2.rate_lec(lecturer1, 'Python', 5)
# student2.rate_lec(lecturer1, 'Python', 6)
# student2.rate_lec(lecturer1, 'Python', 8)

# students = [student1, student2]
# lecturers = [lecturer1, lecturer2]


# print(student1)
# print(student2)
# print(rewiewer1)
# print(rewiewer2)
# print(lecturer1)
# print(lecturer2)
# print(student1 > student2)
# print(lecturer1 < lecturer2)

print('________________________________Задание 4_________________________________')

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'   

    def average_hw(self):
        count = 0
        for grades_key in self.grades:
            count += len(self.grades[grades_key])
        self.average_homework = round((sum(map(sum, self.grades.values())) / count), 2)
        return self.average_homework

    def __lt__(self, other):
      if not isinstance(other, Student):
            print('Not a Student!')
            return
      return self.average_hw() < other.average_hw()

    def __str__(self):
        res = f'''Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_hw()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''
        return res
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    

class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.grades = {}

  def average_rating(self):
        count = 0
        for grades_key in self.grades:
            count += len(self.grades[grades_key])
        self.average_grades = round((sum(map(sum, self.grades.values())) / count), 2)
        return self.average_grades

  def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_rating() < other.average_rating()
  
  def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'
        return res


class Rewiewer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)

  def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

  def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
  
 
student1 = Student('Harry', 'Potter', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Программирование для начинающих']

student2 = Student('Hermione' , 'Granger', 'female')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Git']
student2.courses_in_progress += ['Веб-дизайн для новичков']

rewiewer1 = Rewiewer('Severus', 'Snape')
rewiewer1.courses_attached += ['Python']

rewiewer2 = Rewiewer('Albus', 'Dumbledore')
rewiewer2.courses_attached += ['Git']

rewiewer1.rate_hw(student1, 'Python', 7)
rewiewer1.rate_hw(student1, 'Python', 6)
rewiewer1.rate_hw(student1, 'Python', 8)

rewiewer1.rate_hw(student2, 'Python', 9)
rewiewer1.rate_hw(student2, 'Python', 10)
rewiewer1.rate_hw(student2, 'Python', 8)

rewiewer2.rate_hw(student1, 'Git', 5)
rewiewer2.rate_hw(student1, 'Git', 8)
rewiewer2.rate_hw(student1, 'Git', 7)

rewiewer2.rate_hw(student2, 'Git', 7)
rewiewer2.rate_hw(student2, 'Git', 9)
rewiewer2.rate_hw(student2, 'Git', 10)


lecturer1 = Lecturer('Minerva', 'Mcgonagal')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Git']

lecturer2 = Lecturer('Remus', 'Lupin')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']

student1.rate_lec(lecturer1, 'Python', 8)
student1.rate_lec(lecturer1, 'Python', 9)
student1.rate_lec(lecturer1, 'Python', 8)
student1.rate_lec(lecturer1, 'Git', 10)
student1.rate_lec(lecturer1, 'Git', 9)
student1.rate_lec(lecturer1, 'Git', 6)

student2.rate_lec(lecturer2, 'Git', 10)
student2.rate_lec(lecturer2, 'Git', 9)
student2.rate_lec(lecturer2, 'Git', 10)
student2.rate_lec(lecturer1, 'Python', 5)
student2.rate_lec(lecturer1, 'Python', 6)
student2.rate_lec(lecturer1, 'Python', 8)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]


print(student1)
print(student2)
print(rewiewer1)
print(rewiewer2)
print(lecturer1)
print(lecturer2)
print(student1 > student2)
print(lecturer1 < lecturer2)

def average_grade(list, course):
    grades_all = []
    for current_student in list:
        for key, value in current_student.grades.items():
            if key == 'Python':
                for grade in value:
                    grades_all.append(grade)
    average_grades = round(sum(grades_all) / len(grades_all), 2)
    if list == students:
        print(f'Средняя оценка для всех студентов по курсу "Python": {average_grades}')
    if list == lecturers:
        print(f'Средняя оценка для всех лекторов по курсу "Python": {average_grades}')


average_grade(students, 'Python')
average_grade(lecturers, 'Python')

def average_grade(list, course):
    grades_all = []
    for current_student in list:
        for key, value in current_student.grades.items():
            if key == 'Git':
                for grade in value:
                    grades_all.append(grade)
    average_grades = round(sum(grades_all) / len(grades_all), 2)
    if list == students:
        print(f'Средняя оценка для всех студентов по курсу "Git": {average_grades}')
    if list == lecturers:
        print(f'Средняя оценка для всех лекторов по курсу "Git": {average_grades}')


average_grade(students, 'Git')
average_grade(lecturers, 'Git')