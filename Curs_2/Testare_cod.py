from random import randint


class Student:
    student_object_list = []

    def __init__(self):
        self.grade = 0

    @classmethod
    def create_students_objects(cls):
        student_name_list = []
        number_of_students = int(input("Please select the number of students"))
        for i in range(1, number_of_students + 1):
            student_name_list.append(f"student{i}")
        print(student_name_list)

        # acest for iti va umple lista student_object_list cu obiecte de tipul student + numar unde cel mai mare numar va fi
        #inputul dat iar  cel mai mic 1

        for student in student_name_list:
            student = Student()
            Student.student_object_list.append(student)

        # acest for il poti pastra aici sau in afara clasei, poti sa il lasi aici daca vrei ca automat cand chemi
        # Student.create_students_objects sa-le dea zi grade la studenti
        # sau o poti scoate din clasa si sa creezi doar lista de obiecte cand chemi Student.create_students_objects
        # iar dupa daca vrei sa le dai grade scrii forul asta in afara clasei
        for student in Student.student_object_list:
            student.generate_grade()
            print(student.grade)

    def generate_grade(self):
        self.grade = randint(1, 10)
        return self.grade

    # def generate_student_dictionary(self):
    #     for i in range(self.number_of_students):
    #         self.student_dictionary.update({self.generate_student_name(): self.generate_grade()})

    # def find_grade_above_7(self):
    #     grades_above_7 = []
    #     for i in self.student_dictionary.values():
    #         if i > 6:
    #             grades_above_7.append(i)
    #     return len(grades_above_7)

    # def find_percentage(self):
    #     return self.find_grade_above_7() / self.number_of_students * 100


Student.create_students_objects()