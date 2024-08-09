#Function without input
def greet():
    print("Hello!")
    print("Welcome to day 8")
    print("Have a good day")

greet()

#Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"Welcome to day 8, {name}")
    print("Have a good day")

greet_with_name("Angela")

#Function with multiple parameters
def greet_with(name, day, location):
    print(f"Hello {name}!")
    print(f"Welcome to day {day}, {name}.")
    print(f"What is it like in {location}?")

#positional arguments 
greet_with("James", 8, "Derry")

#keyword arguments
greet_with(location="London", name="Orla", day=100)
