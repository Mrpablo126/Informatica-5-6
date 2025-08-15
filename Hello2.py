def hello():
    print("Hello")

name = input("What is your name? ").strip().title()
hello()
print(f"hello, {name}")     