capitals = {
    "Mexico": "Mexico City",
    "Canada": "Ottawa",
    "Brazil": "Brasilia",
    # "Canada": "Montreal" #Use unique keys
}

capitals["Italy"] = "Rome" #Add a new key and value
del capitals["Brazil"] #Deletes key and value
print(capitals)
capitals.pop("Canada") #Is the same that line 8
capitals.clear()

# Houses = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }

# for student in Houses:
#     s = Houses[student]
#     print(f"{student}: {s}")

# students =[
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None}
# ]
# for element in students:
#     print(f" {element["name"]}, {element["house"]}, {element["patronus"]}")