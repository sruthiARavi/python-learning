import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

output = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

                  
if user_choice < 0 or user_choice > 2:
  print("You entered an invalid number. You lose!")
                  
computers_choice = random.randint(0,2)

print(output[user_choice])
print("Computer chose:")
print(output[computers_choice])

#user results are stored
#user against computer 

against_rock = [0,-1,1]
against_paper = [1,0,-1]
against_scissor = [-1,1,0]

verdict = [against_rock, against_paper, against_scissor]

result = verdict[user_choice][computers_choice]
result_str = ""
if(result == 0):
    print("It's a draw!")
elif(result == 1):
    print("You win!")
else:
    print("You lose!")
    

