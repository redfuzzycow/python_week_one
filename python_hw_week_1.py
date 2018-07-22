#hours in a year
print(24*365)

#minutes in a decade
print(60*24*365*10)

#age in seconds
print(60*60*24*365*30)

#andreea's age
print(48618000/31536000)

#angry boss

print("What do you want?")
employee_says = input()
print("WHADDAYA MEAN " + employee_says + "?!? YOU'RE FIRED!!")

#bottle of beers on the wall

num_bottles = 99
while num_bottles >0:
	if num_bottles==1:
		print(str(num_bottles) + " bottle of beer on the wall")
	else:
		print(str(num_bottles) + " bottles of beer on wall")
	num_bottles = num_bottles-1
	print(1+2)response = ""

#deaf grandma

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

 #sortedlist

word=input("enter a word ")
word_list = []
while word != "":
	word_list.append(word)
	word=input()

word_list.sort()

print(word_list)