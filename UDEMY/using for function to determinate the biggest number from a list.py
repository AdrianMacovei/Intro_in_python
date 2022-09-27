# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
heights_score = 0
for heights in student_scores:
    if heights_score < heights:
        heights_score = heights
print (f"The highest score in the class is: {heights_score}")


