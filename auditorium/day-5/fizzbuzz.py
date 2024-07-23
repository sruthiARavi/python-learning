# Write your code here 👇
print("1")
for number in range(2, 101):
  output=""; 
  if(number%3 == 0):
    output += "Fizz"
  if(number%5 == 0):
    output += "Buzz"
  if(output == ""):
    output = str(number)
  print(output)
