"""
Name: Mitansh
Date: 05/03/2024
Description: This program calculates the average of three exam grades,
             determines the corresponding letter grade, and indicates whether
             the student is passing or failing based on the average.
"""

exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
    sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg >= 70 and avg < 80:
    letter_grade = "C"
elif avg >= 60 and avg < 70:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg))
print("Grade: " + letter_grade)

if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")