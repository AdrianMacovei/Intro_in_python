student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] in range (91, 100):
        student_grades[key] = "Outstanding"
    elif  student_scores[key] in range (81, 90):
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] in range (71, 80):
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)