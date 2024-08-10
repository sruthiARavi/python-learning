my_dictionary = {
    "key1": "value1",
    "key2": "value2",
}
print(f"{my_dictionary['key2']}")
my_dictionary["key3"] = "value3"
print(my_dictionary["key3"])

empty_dictionary = {}
empty_dictionary["key"] = "value"
print(empty_dictionary)

#edit a dictionary
my_dictionary["key1"] = "1a"

#loop through a dictionary
#1. print keys
for key in my_dictionary:
    print(key)
#2. print vals
for key in my_dictionary:
    print(f"{key} --> {my_dictionary[key]}")

print(my_dictionary)
#wipe out a dictionary
my_dictionary = {}
print(my_dictionary)

#####################################

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#nested dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Stuttgart"],
}

for country in travel_log:
    if country == "France":
        city = travel_log[country][1]
        print(city)

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log["nest_list"] = nested_list
print(travel_log["nest_list"][2][1])

travel_log["France"] = {
    "num_times_visited": 8,
    "cities_visited": ["Paris", "Lille", "Dijon"],
}
travel_log["Germany"] = {
    "num_times_visited": 5,
    "cities_visited": ["Berlin", "Stuttgart"],
}
print(travel_log["Germany"]["cities_visited"][1])
