def get_gpa(grades: list) -> float:
    gpa = round(sum(grades)/len(grades), 2)
    return gpa

def can_get_funding(grades: list) -> bool:
    for grade in grades:
        if grade < 60:
            return False
    if get_gpa(grades) >= 80:
        return True
    else:
        return False

students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]

amount_of_students_with_funding = 0
average_GPA = 0
average_GPA_funding = 0


# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding
for grade in students_grades:
    if can_get_funding(grade):
        amount_of_students_with_funding += 1
        average_GPA_funding += get_gpa(grade)
    average_GPA += get_gpa(grade)

average_GPA /= len(students_grades)
average_GPA_funding /= amount_of_students_with_funding

