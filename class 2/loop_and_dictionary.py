highest = 0
students = {
    "Alif":95,
    "Akash":100,
    "John":78
    }
for score in students.values():
    if score > highest:
        highest = score

print(students)
#print(max(students.values())
print(f"the highest score is {highest}")