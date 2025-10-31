def main():
    print("Type a positive integer:")
    x = int(input())
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    print("The factorial of", x ,"is: ", fact)

main()
