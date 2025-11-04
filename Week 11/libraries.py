#Como usar al libreria de random
#Funciona para hacer decisiones random
# import random

# coin = random.choice(["heads", "tails"])
# print(coin)

# number = random.randint(1,10)
# print(number)

# cards = ["jack","queen","king","ace"]
# random.shuffle(cards)
# for card in cards:
#     print(card)

#para estadisticas
# import statistics
# import sys
# # print(statistics.mean([int(sys.argv[1]),int(sys.argv[2])]))
# import sys
# print("Hello, my name is", sys.argv[1])

import sys
import cowsay
try:
    cowsay.cow("Hello,", sys.argv[1])
except IndexError:
    # print("Too few arguments")
    sys.exit()