fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")  
print(fruits)

print("************")

for number in range(1, 11):
  print(number)

print("************")

#step size 3 
for number in range(1, 11, 3):
  print(number)

print("************")

total = 0
for number in range(1, 101):
  total += number
print(total)
