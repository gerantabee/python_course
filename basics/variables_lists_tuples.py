# Variables are loosely typed in Python, and dtype is flexible with assignment
var1 = 20
var1 = "Fred"
var1 = True

print(var1)

n1, n2, n3 = 10, 20, 40

print(n1, n2, n3)

# Strings added to int/floats will throw an error
# You can correct them or cast the string using int() or float()
# n1="10"


ntotal = n1 + n2 + n3
print(ntotal)

# Make a list from individual variables
nums = [n1, n2, n3]
nums_total = sum(nums)
print(nums_total)

# Make a list from raw ints
# 55, 65, 75, 80, 91, 62, 50, 70
grades = [55, 65, 75, 80, 91, 62, 50, 70]
# grades_average = sum(grades) / len(grades)
# Create a grades curve
# grades_average = sum(grades) + 120 / len(grades) #wtf??
# Order of operators!
grades_average = (sum(grades) + 120) / len(grades)
print(grades_average)
print(sorted(grades, reverse=True))

grades_updated = []

# "Sunday","Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday"
days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
print(days_of_week)
print(days_of_week[0])
print(days_of_week[:3])

print(sorted(days_of_week))

for day in days_of_week:
    print(day.upper())

# Debug this as we never actually update the main list
grades = [55, 65, 75, 80, 91, 62, 50, 70]
grades_updated = []

# Debug i (don't update at first)
# i = 0
# for grade in grades:
#     # Add 15 points to each grade
#     grade += 15
#     grades[i] = grade
#     # Make sure no grade goes above 100
#     i+=1

# OR

for i,grade in enumerate(grades):
    # Add 15 points to each grade
    grade += 15
    grades[i] = grade

print(grades)

# Use list comprehension
# grades_updated_lc = [x + 15 for x in grades]
grades_updated_lc = [x + 15 for x in grades if x <= 85]
grades_updated_lc.append(89)
print(grades_updated_lc)