#SyntaxError
# print("Hello, world)

#ValueError
# try:
#     x = int(input("What's x?"))
#     print(f"x is equial to {x}")
# except ValueError:
#     print("x is not a number")

# ZeroDivisionError
# def spam(divide_by):
#     try:    
#         return 42 / divide_by
#     except ZeroDivisionError:
#         print("Adriana salte 🗣️🗣️🗣️🗣️🔥🔥")
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))
                            #para decomentar el contro k + u


# while True:
#     try:
#         x = int(input("What's x?"))
        
#     except ValueError:
#         print("x is not a number")
#     else:
#         break
# print(f"x is equal to {x}")

def read_small_integer():
    while True:
        try:
            input_str = input("Please type in an integer:")
            number = int(input_str)
            if number < 100 and number >= 0:
                return number
        except ValueError:
            pass
        print("This input is invalid")    
number = read_small_integer()
print(number, "to the power of three is", number**3 )