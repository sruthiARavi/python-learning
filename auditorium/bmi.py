###############
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
###############
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
num_height = float(height)
num_weight = int(weight)
#ht_prod = num_height*num_height
#bmi = num_weight/ht_prod
bmi = num_weight/num_height ** 2
print(int(bmi))
