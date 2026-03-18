def can_get_funding(grades):
   if min(grades)<60: return False
   elif sum(grades)/len(grades)>80: return True
   else: return False

students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]

k=0
# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
# 2. What was the average GPA
# 3. What was the average GPA among those, who got funding
if can_get_funding(students_grades[0])==True:k+=1
if can_get_funding(students_grades[1])==True:k+=1
if can_get_funding(students_grades[2])==True:k+=1
print(k," students got funding")
print("Average:",sum(students_grades[0]+students_grades[1]+students_grades[2])/len(students_grades[0]+students_grades[1]+students_grades[2]))
for grades in students_grades:
    if can_get_funding(grades)==True:print(sum(grades)/len(grades))