

while True:
    x = int(input("Type a positive integer:"))
    fact = 1

    if x > 0:
        for i in range(1, x + 1):
            fact *= i
        print(f"The factorial of {x} is: {fact}")
        break
    else:
        print("ERROR")
        print("Try again") 
        continue