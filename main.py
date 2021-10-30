# higherLower.py
#
# Python Bootcamp Day 14 - Higher Lower Game
# Usage:
#      Pick who has more Instagram followers. 
#
# Marceia Egler Oct 7, 2021


import art
from game_data import data
import random
import os


score = 0
game = True
last = 0

print(art.logo)

def restart():
    '''Clear screen and re-display logo'''
    os.system("clear")
    print(art.logo)

def generator():
    '''Pick 2 profiles from data to compare.''' 
    #prevent random picks from duplicating with sample vs choice   
    random_index = random.sample(range(len(data)), 2) 
    if score > 0:
        random_index[0] = last

    return random_index

        
def right_wrong(choice: str, person_a: int, person_b: int) -> bool: 
    '''Decide if player has made correct choice.'''
    if person_a > person_b:
        restart()
        print("You're right!")
        return choice == 'a'
    else:
        restart()
        print("You're right!")
        return choice == 'b'

restart()
while game:    
    if score > 0:  
        print(f"Your current score is {score}")

    vs = generator() 

    person_a = data[vs[0]]['follower_count']
    person_b = data[vs[1]]['follower_count']

    print(f"Compare A: {data[vs[0]]['name']}, a {data[vs[0]]['description']} from {data[vs[0]]['country']}")

    print(art.vs)

    print(f"Against B: {data[vs[1]]['name']}, a {data[vs[1]]['description']} from {data[vs[1]]['country']}")

    pick = input("Who has more followers? Type 'A' or 'B': ") 

    if right_wrong(pick,  person_a,  person_b) == False:
        print(f"Sorry, that's wrong. Final score: {score}")
        game = False
    else:
        score += 1        
        last = vs[1]
        
    