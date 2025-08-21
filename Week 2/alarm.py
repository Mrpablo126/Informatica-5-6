def main():
    is_armed = False
    motinon_detected = False
    door_open = False
    is_afternoon = True
    display_alarm(is_armed, motinon_detected, door_open, is_afternoon)

def display_alarm(iar, ms, dop, an):
    if iar:
        if ms: 
            print("WIUWIUWIUWIUWIUWIUWIUWIUWIUWIUWIUWIU!!!!!!!!!")
        if dop:
            print("door is open")
    else:
        if an and ms:
            print("Welcome home! Turning the light on!")

main()