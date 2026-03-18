from numpy.ma.core import true_divide


def can_get_funding(grades):
    a = sum(grades)/len(grades)>=80
    b = True
    for grade in grades:
        if grade<=60:
            b = False
    return a and b

def gpa(grades):
    return sum(grades)/len(grades)

students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]
c = 0
for student in students_grades:
    print(can_get_funding(student), end = ' ')
    if can_get_funding(student):
        c+=1
print('\n')

grades_gpa = []
for grade in students_grades:
    grades_gpa.append(gpa(grade))

print(f"{c} students got funding grades")
print(f"{gpa(grades_gpa)} overall gpa")

passing_students = []

for student in range(len(students_grades)):
    if can_get_funding(students_grades[student]):
        passing_students.append(student)

sum = 0
for student in passing_students:
    sum += grades_gpa[student]

print(f"{sum/len(passing_students)} gpa of students, who have gotten funding grades")
# TODO: Write a simple algorithm to find out:

# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding