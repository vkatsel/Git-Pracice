def can_get_funding(grades):
    # TODO: Implement function to check 1 student
    if sum(grades)/len(grades)>=80 and min(grades)>=60: return True
    return False

students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]


# TODO: Write a simple algorithm to find out:
cnt_pass = 0
sum_gpa = 0
sum_cool_gpa = 0
for i in range(len(students_grades)):
    sum_gpa = sum_gpa + sum(students_grades[i])/len(students_grades[i])
    if can_get_funding(students_grades[i]):
        sum_cool_gpa = sum_cool_gpa + sum(students_grades[i])/len(students_grades[i])
        cnt_pass += 1

print(cnt_pass, round(sum_gpa/len(students_grades), 2), round(sum_cool_gpa/len(students_grades), 2))

# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding