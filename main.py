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

passed = can_get_funding(students_grades[2])
if passed:
    print("Student can get funding")
else:
    print("No")






# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding