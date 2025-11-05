
print("Type a positive integer:")
x = int(input())
fact = 1
for i in range(1, x + 1):
    fact *= i
    while x < 0:
        print("ERROR")
        return 
print("The factorial of", x ,"is: ", fact)


