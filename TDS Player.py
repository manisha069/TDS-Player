import random

print("Welcome to TDS Player, type 'leave' to exit game")

choices = ['Truth', 'Dare', 'Situation']

#enter statements according to your convinience
truths = ['Stat1', 'Stat2', 'Stat3']
dares = ['Stat1', 'Stat2', 'Stat3']
situations = ['Stat1', 'Stat2', 'Stat3']

while (input() != 'leave'):
    t = random.choice(choices)
    print(t)
    if t == "Truth":
        print(random.choice(truths))
    elif t == "Dare":
        print(random.choice(dares))
    else:
        print(random.choice(situations))