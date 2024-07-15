print("Welcome to the tip calculator!")
#If the bill was $150.00, split between 5 people, with 12% tip. 
bill = input("What is the total bill? ")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
people = input("How many people to split the bill? ")
#Write your code below this line 👇
bill_as_float = float(bill)
tip_percentage_as_float = float(tip_percentage)
people_as_int = int(people)
tip = (bill_as_float * tip_percentage_as_float / 100)
total_bill = bill_as_float + tip
bill_per_person = total_bill / people_as_int
final_amount = round(bill_per_person, 2)  
print(f"Each person should pay: ${final_amount}")
