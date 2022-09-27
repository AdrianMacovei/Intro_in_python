# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
#split function for transform fata into a list (separate data)
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# for function for transform every data to int
  
total_heights = 0
for heights in student_heights:
    total_heights += heights 
# sum of list elements with for not sum

number_of_students = 0
for number in student_heights:
    number_of_students +=1
# len function using for

avarage = round(total_heights/number_of_students)
print (avarage)

