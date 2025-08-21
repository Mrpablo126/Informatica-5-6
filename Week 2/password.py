import getpass

def main():
    password = getpass.getpass("Set password:")
    input("Press enter to log in.")
    check_password(password)

def check_password(p):

    guess = input("Enter password:")
    if p == guess:
        print("correct password")
    print("The program has ended.")

main()
