score = int(input("What was yout score: "))

grade_tag = lambda x: "Pass" if x >= 40 else "Fail"

print(grade_tag(score))