def main():
    x = int(input("Enter a positive number:"))
    i = 1
    while 10 >= i:
        print(f"{x} * {i} =",x * i)
        i += 1
    if x < 0:
        print("ERROR")





main()