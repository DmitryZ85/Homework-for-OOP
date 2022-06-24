# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_rate(self):
        if len(self.grades) > 0:
            sum_grades = 0
            for course, grade_course in self.grades.items():
                sum_grade_course = 0
                for grade in grade_course:
                    sum_grade_course += grade
                ave_grade_course = sum_grade_course / len(grade_course)
                sum_grades += ave_grade_course
            ave_rate = sum_grades / len(self.grades)
            return ave_rate
        else:
            print('Лектор еще не получил оценок за лекции')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print(f'{other} не Студент')
            return
        return self._avg_rate() < other._avg_rate()

    def __str__(self):
        avg = self._avg_rate()
        c_progress = ",".join(self.courses_in_progress)
        c_finished = ",".join(self.finished_courses)

        res = f'\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {avg}\nКурсы в процессе изучения: {c_progress}\nЗавершенные курсы: {c_finished}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}

    def _avg_rate(self):
        if len(self.grades) > 0:
            sum_grades = 0
            for course, grade_course in self.grades.items():
                sum_grade_course = 0
                for grade in grade_course:
                    sum_grade_course += grade
                ave_grade_course = sum_grade_course / len(grade_course)
                sum_grades += ave_grade_course
            ave_rate = sum_grades / len(self.grades)
            return ave_rate
        else:
            print('Лектор еще не получил оценок за лекции')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f'{other}Не Лектор')
            return
        return self._avg_rate() < other._avg_rate()

    def __str__(self):
        avg = self._avg_rate()
        res = f'\nИмя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {avg}'
        return res


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
        res = f'\nИмя: {self.name} \nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Введение в Программирование']
second_student = Student('Paul', 'Feldman', 'your_gender')
second_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']

master_lecturer = Lecturer('Big', 'Grumpy')
master_lecturer.courses_attached += ['Python']
master_lecturer.courses_attached += ['Java']
second_lecturer = Lecturer('Small', 'But_Happy')
second_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(second_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Java', 9)
cool_reviewer.rate_hw(best_student, 'Java', 8)


best_student.rate_lect(master_lecturer, 'Python', 10)
best_student.rate_lect(master_lecturer, 'Python', 9)
best_student.rate_lect(master_lecturer, 'Java', 7)
best_student.rate_lect(second_lecturer, 'Python', 9)
second_student.rate_lect(second_lecturer, 'Python', 8)


def rate_lect_course(lecturer, course):
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            n_rate = 0
            for rate in lecturer.grades[course]:
                n_rate += rate
            average_rate = n_rate / len(lecturer.grades[course])
            return (f'\nУ лектора {lecturer.name} {lecturer.surname} средняя оценка по курсу {course} - {average_rate}')
        else:
            return ('\nУ лектора еще нет оценок по данному курсу')

def rate_student_course(student, course):
    if isinstance(student, Student) and course in student.grades:
        n_rate = 0
        for rate in student.grades[course]:
            n_rate += rate
        average_rate = n_rate / len(student.grades[course])
        return (f'\nУ Студента {student.name} {student.surname} средняя оценка по курсу {course} - {average_rate}')
    else:
        return ('\nУ студента еще нет оценок по данному курсу')

print(best_student.grades)
print(master_lecturer.grades)
print(cool_reviewer)
print(master_lecturer)
print(best_student)
print(best_student > second_student)
print(master_lecturer > second_lecturer)
print(rate_lect_course(master_lecturer, 'Python'))
print(rate_student_course(best_student, 'Python'))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
