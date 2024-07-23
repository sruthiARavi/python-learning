# Write your code here 👇
for number in range(1, 101):
  if(number%3 == 0 and number%5 ==0):
    print("FizzBuzz")
  elif(number%3 == 0):
    print("Fizz")
  elif(number%5 == 0):
    print("Buzz")
  else:
    print(number)

#or 

#print("1")
#for number in range(2, 101):
  #output=""; 
  #if(number%3 == 0):
    #output += "Fizz"
  #if(number%5 == 0):
    #output += "Buzz"
  #if(output == ""):
    #output = str(number)
  #print(output)
