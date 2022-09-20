import random


class Student:
    CAMPUS = ["A", "B", "C"]
    SCOLARSHIP_VALUES = [623, 680, 750]

    def __init__(self, first_name, last_name, age, domain_of_study, year_of_study):
        if not first_name or not last_name or not age or not domain_of_study or not year_of_study:
            raise ValueError("All fields need to be completed.")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.domain_of_study = domain_of_study
        self.year_of_study = year_of_study
        self.scolarship = 0
        self.anual_credits = 0

    def __str__(self) -> str:
        return f'First name: {self.first_name}, Last name: {self.last_name}, Age: {self.age}, ' \
               f'Domain of study: {self.domain_of_study}, Year of study: {self.year_of_study}'

    def present_himself(self):
        print(f"Hi!I am {self.first_name} {self. last_name} and I am {self.age} years old.")

    def take_a_scolarship(self, year_credits: int):
        if 80 < year_credits < 85:
            self.scolarship = Student.SCOLARSHIP_VALUES[0]
            print(f"Congratulations for your results! Now you win a scolarship in value of {self.scolarship}.")
        elif 85 <= year_credits < 95:
            self.scolarship = Student.SCOLARSHIP_VALUES[1]
            print(f"Congratulations for your results! Now you win a scolarship in value of {self.scolarship}.")
        elif 95 <= year_credits <= 100:
            self.scolarship = Student.SCOLARSHIP_VALUES[2]
            print(f"Congratulations for your results! Now you win a scolarship in value of {self.scolarship}.")

    def promote_a_year(self, year_credits: int):
        if year_credits > 50:
            if self.year_of_study < 3:
                self.year_of_study += 1
                print(f"You promote in year {self.year_of_study}. Congratulations!")
            else:
                print(f"Congratulations you finish your finish your degree in {self.domain_of_study}.")
        else:
            print(f"You need to repeat your year {self.year_of_study} again because you have insufficient credits"
                  f" to promote to year {self.year_of_study + 1}.")

    def change_domain_of_study(self, new_domain):
        self.domain_of_study = new_domain

    @staticmethod
    def want_stay_on_campus() -> bool:
        answer = input("Do you want to stay in our campus? (y/n)")
        answer = answer.lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid answer")

    @staticmethod
    def assign_to_a_group_of_students() -> int:
        return random.randint(1, 2)

    @staticmethod
    def create_a_txt_students(lst_1, lst_2):
        textfile = open("a_file.csv", "w")
        for element in lst_1:
            textfile.write(f"{element}\n")
        for element in lst_2:
            textfile.write(f"{element}\n")
        textfile.close()

    @classmethod
    def get_student(cls):
        first_name = input("First Name:")
        second_name = input("Second Name:")
        age = input("Age:")
        year_of_study = int(input("Year:"))
        domain_of_study = input("Domain of study:")
        return cls(first_name, second_name, age, domain_of_study, year_of_study)


# example of inheritance
class StudentOnCampus(Student):
    def __init__(self, first_name, second_name, age, domain_of_study, year_of_study):
        super().__init__(first_name, second_name, age, domain_of_study, year_of_study)
        self.campus_name = ""
        self.room_nr = 0

    def get_campus_and_room(self):
        self.campus_name = random.choice(Student.CAMPUS)
        self.room_nr = random.randint(0, 100)


group_1 = []
group_2 = []

while True:
    student = Student.get_student()
    student.present_himself()
    student.take_a_scolarship(88)
    group_number = student.assign_to_a_group_of_students()
    print(student)
    if group_number == 1 and len(group_1) <= 2:
        group_1.append(student)
    elif (group_number == 2 or group_number == 1) and len(group_2) <= 2:
        group_2.append(student)
    if len(group_1) == 3 and len(group_2) == 3:
        break

for i in range(1, (len(group_1) + 1)):
    print(f"Group 1, student{i}:{group_1[i-1]}")
for i in range(1, (len(group_2) + 1)):
    print(f"Group 2, student{i}:{group_2[i-1]}")

student.create_a_txt_students(group_1, group_2)

group_1[0].change_domain_of_study("Law")
print(group_1[0])
group_1[0].promote_a_year(55)
print(group_1[0])

student = Student("Mihai", "Popescu", 22, "biology", 2)
answer_given = student.want_stay_on_campus()
students_in_campus = []
if answer_given:
    student = StudentOnCampus.get_student()
    student.get_campus_and_room()
    print(f"You will stay on campus {student.campus_name} at room {student.room_nr}.")
    students_in_campus.append(student)
