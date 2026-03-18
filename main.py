students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]
def can_get_funding(grades):
    # TODO: Implement function to check 1 student
    sum = 0
    less = 0
    for i in range(6):
        sum += grades[i]
    GPA = sum/6
    for p in range(6):
        if grades[p] < 60:
            less += 1
    if GPA >= 80 and less == 0:
        return True
    else: return False

print(can_get_funding(students_grades[2]))




# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding