def can_get_funding(grades):
    if (sum(grades)/len(grades))>80 and min(grades)>=60:
        return True
    else:
        return False
    pass

students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]

value_list = []

for i in range(len(students_grades)):
    value_list.append(can_get_funding(students_grades[i]))

print(value_list)
print(f"How many students got funding: {value_list.count(True)}")

gpa_list=[]

for i in range(len(students_grades)):
    gpa_list.append(sum(students_grades[i])/len((students_grades[i])))

print(gpa_list)
print(f"Average gpa: {sum(gpa_list)/len(gpa_list)}")

gpa_passed_list=[]

for i in range(len(students_grades)):
    if can_get_funding(students_grades[i])==True:
        gpa_passed_list.append(sum(students_grades[i])/len(students_grades[i]))

print(gpa_passed_list)
print(f"Average GPA among those, who got funding: {sum(gpa_passed_list)/len(gpa_passed_list)}")

# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding

#   o
# / | \
#  / \
