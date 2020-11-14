#Justine Rosado
#11/14/2020
#this problem is a game with arrows and a target.  This is supports to random the arrows shots on the target and see what the points is when it runs out of arrows.

import random

def archer():
    score= 0
    score_card = []
    arrows = 10

    while arrows > 0:
        target = random.randint(0,10)

        if target == 0:
            pass

        elif target == 10:
            score += 20
            arrows -=1

        else:

            score += target
            arrows -= 1 

    print("final score is",score,"points")



archer()
