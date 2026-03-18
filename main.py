students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]
count = 0
avg_get_fund_gpa = 0
avg_gpa = 0

def can_get_funding(grades):
    avg_grade = sum(grades)/len(grades)
    if avg_grade <= 80:
        return False
    else:
        return True

for i in range(len(students_grades)):
    avg_gpa = avg_gpa + sum(students_grades[i]) / len(students_grades[i])
    if can_get_funding(students_grades[i]):
        avg_get_fund_gpa = avg_get_fund_gpa + sum(students_grades[i]) / len(students_grades[i])
        count += 1

print(count, round(avg_gpa/len(students_grades), 2), round(avg_get_fund_gpa/count, 2))