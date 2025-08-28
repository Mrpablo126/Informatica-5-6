name = input("Insert your name:")

coin = int(input("Insert money:"))
coca = 50
cambio = coin - coca

while coin == coca:
    print("Take your product")
    
    if coin < coca:
        print("Error")
    elif coin > coca:
            print(cambio)
    else:
            print("Error")
            break