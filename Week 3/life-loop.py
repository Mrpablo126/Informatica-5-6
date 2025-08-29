import time
 
print("WAKE UP")
time.sleep(1.5)
print("1-Monday\n2-Tuesday\n3-Wednesday\n4-Thursday\n5-Friday\n6-Saturday\n7-Sunday")
b = int(input("Select a day:"))

Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
saturday = 6
sunday = 7
while b == Monday or Tuesday or Wednesday or Thursday or Friday:
    print("It's time to school")
    break
if b ==sunday:
    print("Wake up you need to go to church")
while b == saturday:
    print("Laburo time")
