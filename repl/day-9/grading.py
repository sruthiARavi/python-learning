student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    grade = ""
    score = student_scores[name]
    if(score<=70):
        grade = "Fail"
    elif(score<=80):
        grade = "Acceptable"
    elif(score<=90):
        grade = "Exceeds Expectations"
    else:
        grade = "Outstanding"
    student_grades[name] = grade

print(student_grades)
