def can_get_funding(grades):
    # TODO: Implement funcn to check 1 student
    #     # passtio
    ave_grade = sum(grades) / len(grades)
    if ave_grade <80:
        return False
    else:
        if min(grades) < 60:
            return False
        else:
            return True
students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]
passed = can_get_funding(students_grades[0])
if passed:
    print("student gets funded")
else:
    print("No")


# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding
count_pass=0
sum_pass=0
sum_cool_gpa=0
for i in range(len(students_grades)):
    sum_gpa = sum_pass + sum(students_grades[i])/len(students_grades[i])
    if can_get_funding(students_grades[i]):
        sum_cool_gpa = sum_pass + sum(students_grades[i])/len(students_grades[i])
            count_pass += 1
print(count_pass, round(sum_gpa/len(students_grades), 2)), round(sum_cool_gpa/len(count_pass), 2))

