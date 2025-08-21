def main():
    asu = input("Select a:")
    bu = input("Select b:")
    print("Select The Operation \n 1-sum\n 2-substract\n 3-multiplication\n 4-division")
    calculation = input("Select the operation:")
    operation(calculation,asu,bu)

def operation(s,a,b):
    if s == "1":
        print(int(a) + (b))
    if s == "2":
       print(int(a) - int(b))
    if s == "3":
       print(int(a) * int(b))
    if s == "4":
       print(int(a) / int(b))



main()