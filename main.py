from numpy.ma.core import true_divide


def can_get_funding(grades):
    a = sum(grades)/len(grades)>80
    b = True
    for grade in grades:
        if grade<60:
            b = False
    return a and b

# def gpa(grades):
#     return
students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]
# c = 0
for student in students_grades:
    print(can_get_funding(student))
    # c+=1

# TODO: Write a simple algorithm to find out:

# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding