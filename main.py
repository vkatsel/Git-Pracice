def can_get_funding(grades):
    # TODO: Implement function to check 1 student
    if min(grades)<60:
        return False
    elif sum(grades)/len(grades)>80:
        return True
    else:
        return False



students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]


# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
count=0
for i in range(len(students_grades)):
    passed = can_get_funding(students_grades[i])
    if passed:
        print(f"Student {i} gets funding")
        count+=1
print(f"Overall {count} student(s) got funding")
# 2. What was the average GPA
gpa=[]
for i in range(len(students_grades)):
    gpa.append(sum(students_grades[i])/len(students_grades[i]))
print(f"\nAverage GPA is {sum(gpa)/len(gpa)}")
# 3. What was the average GPA among those, who got funding
gpa_cool=[]
for i in range(len(students_grades)):
    if can_get_funding(students_grades[i]):
        gpa_cool.append(sum(students_grades[i])/len(students_grades[i]))
print(f"\nAverage GPA among those, who got funding is {sum(gpa_cool)/len(gpa_cool)}")