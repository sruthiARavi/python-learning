# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
##print(names)
# 🚨 Remember to remove the print statement above when you submit.
import random 

upper_limit = len(names) - 1
choice = random.randint(0, upper_limit)
banker = names[choice]

print(f"{banker} is going to buy the meal today!")
