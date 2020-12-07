import section_3
import enemies
import random

def start(player):

    print("in the woods jack took a stroll around the woods.")
    input()
    print("The woods are a peaceful to relax at when you are stress or need to blow off some steam.")
    input()
    print("However, it is also dangerous becasue of the increase amount of monsters living in the woods.  somepeople would go missing and never to be found.")
    input()
    print("on Jack's path, he sees a bear that is bigger than a normal bear.")
    input()
    print("the path the bear is blocking is a short cut to another town that merchants go to sell their goods so they have less time to get to that town.")
    input()
    print("The second path is a long way to the next town, but it is more quiter and safer to go.")
    input()
    print("However this will take the merchants longer to get to the next town, and make the people in that town inpatient for their goods.")
    input()
    choice = input("what will you do?  A:go the longer path. B: take care of the bear and go to the shorter path.")
    if choice == ("A"):
        print("jack: ya I'm not dealing with that bear.  rater just go to the longer path.")
        input()
        print("ignoring the bear, Jack decided to go to the longer path.")
        input()
        print("this deciding might upset the merchants, but to him, his safty matter more.")
        input()

    if choice == ("B"):
        print("Jack: I better deal with that bear before someone gets hurts")
        input()
        bear = enemies.monsters("black bear")
        while player.hp > 0 and bear.hp > 0:
              action = input("what will you do? A:attack D:defend I:inventory")
              if action == ("A"):
                  print("jack swinges his sword at his oponent. random hp")
                  bear.hp -= random.randint(6,10)
              if action == ("D"):
                  print("defends up reudce damage by 1")
                  player.defend +=1
                  print("bear claws out the player.  player losses 15 hp")
              player.hp -= 16
              if action == ("I"):
                  items = input("what item do you want to use?")
                  if  items == ("potion") and items in player.inventory:
                      print("Jack drinks the potion. regains 100")
                      player.hp +=100
                  if items == ("thowing bomb") and items in player.inventory:
                      print("jack throws a bomb at the bear")
                      bear.hp -=20
              if player.hp < 0:
                  print("GAME OVER")
                  quit()
              if bear.hp < 0:
                  print("Jack: now the bear is out of the way.  now the merchants can cross this area without fear")
                  input()
                  print("you got 500 exp.")
                  input()
                  player.exp += 500
        
    print("Jack then arrives at a town that is smaller then the town he was last in, but the people here are peacful and firendly.")
    
                  
              
