dictionary = {
    "color": "black",
    "age": 29,
}

# Values
print(dictionary.values())
for v in dictionary.values():
    print (v)

# Keys
print(dictionary.keys())
for k in dictionary.keys():
    print(k)

#Items
print(dictionary.items())
for i in dictionary.items():
    print(i)

#Print key and value using methods
#to do

for d in dictionary:
    print(f"{d}: {dictionary[d]}" )

#Get
picnic_items = {"apples": 5, "cups": 2}
print(f"I'm bringing {picnic_items.get("cups")}")

print(f"I'm bringing {picnic_items.get("eggs",2)} eggs.")

#Setting Default Values

pet_info = {
    "name": "Dinamo",
    "age": "5 months"
}

pet_info.setdefault("color", "black")
print(pet_info)
for p in dictionary:
    print(f"{p}: {dictionary[p]}")