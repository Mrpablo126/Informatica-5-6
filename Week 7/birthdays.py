birthdays = {
   "Jose": "19/05/2008",
   "Noemi": "09/12/2008",
   "Luna": "22/01/2008"
}
print("1-Jose\n""2-Noemi\n""3-Luna")
name = input(print("Select a number:")).title

while True:
    if name is not birthdays:
        print("This name is not on the list")
        break
    
    if name in birthdays:
        print(f"{name} ")