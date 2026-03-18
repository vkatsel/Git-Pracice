def can_get_funding(grades):
    for grade in grades:
        if grade < 60:
            return False
    return sum(grades)/len(grades) > 80


students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]


# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding
print(can_get_funding(students_grades[0]))
print(can_get_funding(students_grades[1]))
print(can_get_funding(students_grades[2]))