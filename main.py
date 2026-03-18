students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]
def can_get_funding(grades):
    avr_grade = sum(grades) / len(grades)
    if avr_grade <= 80:
        return False
    else:
        if min(grades) < 60:
            return False
        else:
            return True

# passed = can_get_funding(students_grades[2])
#
# funded = 0
# avr_gpa = 0
# avr_gpa_funded = 0
# for i in range(3):
#     if can_get_funding((students_grades[i])):
#         funded += 1

cnt_pass = 0
sum_gpa = 0
sum_cool_gpa = 0
for i in range(len(students_grades)):
    sum_gpa = sum_gpa + sum(students_grades[i])/len(students_grades[i])
    if can_get_funding(students_grades[i]):
        sum_cool_gpa = sum_cool_gpa + sum(students_grades[i])/len(students_grades[i])
        cnt_pass += 1

print(cnt_pass, sum_gpa/len(students_grades), sum_cool_gpa/cnt_pass)








# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding