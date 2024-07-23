#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwd_letters = []
pwd_symbols = []
pwd_numbers = []

for i in range(0, nr_letters):
  pwd_letters.append(letters[random.randint(0, len(letters)-1)])

for i in range(0, nr_symbols):
  pwd_symbols.append(symbols[random.randint(0, len(symbols)-1)])

for i in range(0, nr_numbers):
  pwd_numbers.append(numbers[random.randint(0, len(numbers)-1)])
  
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pwd_easy = pwd_letters + pwd_symbols + pwd_numbers
pwd_easy_str = ""
for i in range(0, len(pwd_easy)):
  pwd_easy_str += pwd_easy[i]
print(f"Your password is (easy): {pwd_easy_str}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#This is not the right implementation as there is no way to ensure that the requirements are respected. 
pwd_hard = []
for i in range(0, len(pwd_easy)):
  pwd_hard.append(pwd_easy[random.randint(0, len(pwd_easy)-1)])

pwd_hard_str = ""
for i in range(0, len(pwd_hard)):
  pwd_hard_str += pwd_hard[i]
  
print(f"Your password is (hard): {pwd_hard_str}")
