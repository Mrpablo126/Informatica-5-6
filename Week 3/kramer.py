def main():
#condition = True

#while Condition:    
 #   number = int(input("Please type in a number, -1 to quit:"))

  #  if number == -1:
    #    condition = False
   # else:
     #   print(number ** 2)
#print("Bye")


    condition = True
    while condition:
        number = input("Say hello:")

        if number.startswith("h"):
            print("Take $20 bucks")
    
        elif number.startswith("hello"):
            print("You have $0 bucks")
        else:
            print("Take $100 bucks")
            break

main()