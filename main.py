def can_get_funding(grades):
    if sum(grades)//len(grades) > 80 and min(grades) >= 60:
        return True
    else:
        return False


students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]

passed = can_get_funding(students_grades[1])
print(passed)

c_pass = 0
sum_g = 0
sum_c_g = 0
for i in range(len(students_grades)):
    sum_g += sum(students_grades[i])//len(students_grades[i])
    if can_get_funding(students_grades[i]):
        sum_c_g += students_grades[i]
        c_pass = c_pass + 1

# c = 0
# f=[]
# nf=[]
# for i in students_grades:
#     if can_get_funding(i):
#         c = c + 1
#         f.append(i)
#     else:
#         nf.append(i)
#
# a_nf = 0
# a_f = 0
# for i in nf:
# a_nf = a_nf + sum(students_grades[i])//len(students_grades[i])
# for i in
# a_f = a_f + sum(students_grades[i])//len(students_grades[i])
#
# a1 = a_nf // len(nf)
# a2 = a_f // len(f)

print(c, a1, a2)
# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding

