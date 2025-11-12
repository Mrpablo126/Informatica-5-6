food = [
    {"almond milk": 30, "skim": 45},
    {"sour cream, light": 16, "plain, low-fat": 77},
    {"egg": 75, "egg white": 16},
    {"cream cheese": 51, "american pasteurized": 79},
    {"peanuts, roasted": 170, "cashews, dry roasted": 163},
    {"lentils, boiled": 115, "edamame, boiled": 127},
    {"catfish, baked": 111, "swai, baked": 89},
    {"celery": 1, "corn": 59},
    {"pears": 20, "kiwi": 0},
    {"ranch": 73, "ranch, fat free": 17}
]
print(food)
print("Select two foods:")

a = input("First food:").lower()
b = input("Second food:").lower()
c = 0
for item in food:
    if a in item:
        c += item[a]
    if b in item:
        c += item[b]
print(f"The total of calories is:{c}")