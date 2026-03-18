def can_get_funding(grades):
    # TODO: Implement function to check 1 student
    avg_grade = sum(grades) / len(grades)
    if avg_grade <= 80:
        return False
    else:
        return True
students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]

passed = can_get_funding(students_grades[0])
if passed:
    print("Student gets funding")
else:
    print("No")
student_with_fund = 0
average_grades = 0
average_student_with_fund = 0


for grades in range(len(students_grades)):
    average_grades = average_grades + sum(students_grades[grades]) / len(students_grades[grades])
    if can_get_funding(students_grades[grades]):
        average_student_with_fund = average_student_with_fund + sum(students_grades[grades]) / len(students_grades[grades])
        student_with_fund += 1








# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding