# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
sum = 0; 
students = 0; 
for height in student_heights:
  sum += height
  students += 1

average = round(sum/students)

print(f"total height = {sum}")
print(f"number of students = {students}")
print(f"average height = {average}")
