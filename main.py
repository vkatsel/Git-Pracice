def can_get_funding(grades):
    for grade in grades:
        if grade < 60:
            return False
    return sum(grades)/len(grades) > 80


students_grades = [[100, 90, 71, 60, 61, 95],
                   [85, 80, 87, 98, 95, 78],
                   [59, 70, 67, 88, 65, 58]]


# TODO: Write a simple algorithm to find out:
# 1. How many students got funding
got_funding = []
for student in students_grades:
    if can_get_funding(student):
        got_funding.append(student)

print(f"{len(got_funding)} student got funding")

# 2. What was the average GPA

def avr(list):
    return sum(list)/len(list)

avrgs = list(map(avr, students_grades))
print(avr(avrgs))
# 3. What was the average GPA among those, who got funding

avrgs_passed = list(map(avr, got_funding))
print(avr(avrgs_passed))