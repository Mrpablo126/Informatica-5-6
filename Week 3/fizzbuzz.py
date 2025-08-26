def main():

    integer_number = int(input("write a number:"))
    integer_number
    a = integer_number %3 == 0
    b = integer_number %5 == 0
    c = a and b

    if integer_number %2 == 0:
        print("prime number")

    if c:
        print("FizzBuzz")

    elif b:
        print("Buzz")
    elif a:
        print("Fizz")
    else:
        print(integer_number)

main()