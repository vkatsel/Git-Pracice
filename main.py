def can_get_funding(grades):
    avg_grade = sum(grades) / len(grades)
    if avg_grade < 80:
        return False
    else:
        if min(grades)<60:
            return False
        else:
            return True

students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]
passed = can_get_funding(students_grades[0])
if passed:
    print("students get funding")
else:
    print("NO")
students_passed = 0
sum_gpa = 0
sum_pass_gpa = 0
for i in range(len(students_grades)):
    sum_gpa = sum_gpa + sum(students_grades[i])/len(students_grades[i])
    if can_get_funding(students_grades[i]):
        sum_pass_gpa = sum_pass_gpa + sum(students_grades[i])/len(students_grades[i])
        students_passed += 1
print(students_passed, round(sum_gpa, 2), round(sum_pass_gpa, 2))
# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding
