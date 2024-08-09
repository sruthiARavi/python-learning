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

print("******************")
#loop through a dictionary
#1. print keys
for key in my_dictionary:
    print(key)
#2. print vals
for key in my_dictionary:
    print(f"{key} --> {my_dictionary[key]}")
print("******************")

print(my_dictionary)
#wipe out a dictionary
my_dictionary = {}
print(my_dictionary)
