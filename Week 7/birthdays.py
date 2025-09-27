def main():
   birthdays = {
      "Jose": "19/05/2008",
      "Noemi": "09/12/2008",
      "Luna": "22/01/2008"
   }
   print("1-Jose\n""2-Noemi\n""3-Luna")
   name = input("Enter a name:").title()


   while True:
      a = 0
      if name in birthdays:
         print(f"The birthday of",name, "is:",birthdays[name])
         break
      if name not in birthdays:
         print("This name is not in the list")
         m = input("Enter the new name:")
         n = input("Enter the birthday:")
         birthdays[m] = n
         print("Birthday added")
         print(birthdays)
   return 
         
main()  