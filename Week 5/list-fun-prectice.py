def main():  
    values()

def values():
    value_list = []
    while True:
        value = int(input("Select a value:"))
        if (value != 0):
            value_list.append(value)
            print(value_list)    
            continue
        else:
            break
    
        


main()