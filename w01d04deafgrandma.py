print("speak to grandma")

import random

granddaughter_Says = input()
all_Caps = granddaughter_Says.isupper()
rando_Year = random.randint(1930, 1951)

while granddaughter_Says != "BYE":
    if all_Caps == False:
        print("HUH?! SPEAK UP, GIRL!")
    else:
        print("NO, NOT SINCE " + str(random.randint(1930, 1950)))
    print()
    print("Say hello to Deaf Grandma!")
    granddaughter_Says = input()
    all_Caps = granddaughter_Says.isupper()