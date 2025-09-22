def main():
    receiver = ["Mario","Luigi","Daisy","Yoshi","Toad","Princess Peach","Bowser"]
    receiver.remove("Princess Peach")
    for sender in receiver:
        tilin(sender)
    
def tilin(a):
        
        print(f"""
        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
            Dear {a}
        
            You are cordially invited to a ball at
            Peach's Castle this evening, 7:00 PM.

            Sincerely, Princess Peach
        
            +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+ 
            """)  

main()