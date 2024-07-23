print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name = name1 + name2
name = name.upper()

tcount = name.count("T")
rcount = name.count("R")
ucount = name.count("U")
ecount = name.count("E") 
lcount = name.count("L")
ocount = name.count("O")
vcount = name.count("V")

score1 = tcount + rcount + ucount + ecount
score2 = lcount + ocount + vcount + ecount

score_str = str(score1) + str(score2)
score = int(score_str)

if(score < 10 or score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif(score > 40 and score < 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
