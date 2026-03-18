students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]

def can_get_funding(grades):
    avg_grade = sum(grades)/len(grades)
    if avg_grade <= 80:
        return False
    else:
        return True

passed = can_get_funding(students_grades[0])
if passed:
    print("Students gets funding")
else:
    print("No")