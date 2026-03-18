def can_get_funding(grades):
    # TODO: Implement function to check 1 student
    avg=sum(grades)/len(grades)
    if avg<=80:
        return False
    else:
        if min(grades)<60:
            return False
        else:
            return True


students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]
passed = can_get_funding(students_grades)
if passed:
    print("Students gets funding")
else:
    print("No")
# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding

cnt_pass=0
sum_gpa=0
sum_col_gpa=0
for i in range(len(students_grades)):
    sum_gpa+=sum_gpa+sum(students_grades[i])/len(students_grades)
    if can_get_funding(students_grades[i]):
        sum_col_gpa+=sum(students_grades[i])/len(students_grades)
        cnt_pass+=1

print(cnt_pass, round(sum_gpa/cnt_pass, 3), round(sum_col_gpa/cnt_pass, 3))
