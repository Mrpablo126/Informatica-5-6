def main():
    
    while True:
        
        try:
            fuel = input("Write a fraction:").split("/")
            print(fuel)
            fuel_porcent = (int(fuel[0]) / int(fuel[1])) * 100
            if fuel[0] == fuel[1]:
                print("F")
            elif fuel == 0/fuel[1]:
                print("E")
            else:
                print(fuel_porcent)
                
        except:
            print("Try again")
            

main()