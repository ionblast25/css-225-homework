import section_2
import enemies
import random

def start(player):

    print("its the next day and jack wakes up from his sleep")
    input()
    print("since it was a beautiful day, jack decided to go for a walk.")
    input()
    print("while he was walking, jack see all the people around the town.  everyone is either greeting each other, relaxing, or going shoping for food or weapons.")
    input()
    print("suddenly your day is ruined by seeing a woman being robbed by some thef.")
    input()
    print("jack: uge can't these guys just stop robbing people?  its not helping.")
    input()
    choice = input("what will you do? A:ignore the problem.  B:get involed")
    if choice == ("A"):
        print("Jack: hell no. I am not geting hurt becasue of this.  She has to defend for herself.")
        input()
        
    if choice == ("B"):
          print("jack: *sigh* might as well do something about it.")
          input()
          print("jack Hey dude, let go of the woman and give here back here money NOW!?")
          input()
          print("thef: I need that money more then this woman.  get loss before you get hurt")
          input()
          print("jack: *draws sword* looks like you leave me with no choice")
          input()
          print("thef: find you ask for it!")
          input()
          rouge = enemies.humans("thef")
          while player.hp > 0 and rouge.hp > 0:
              action = input("what will you do? A:attack D:defend")
              if action == ("A"):
                  print("jack swinges his sword at his oponent. enemy losses random hp")
                  rouge.hp -= random.randint(6,10)
              if action == ("D"):
                  print("defends up reudce damage by 1")
                  player.defend +=1
                  print("rouge stebs player.  player losses 3 hp")
              player.hp -= 3
              if player.hp < 0:
                  print("GAME OVER")
                  quit()
              if rouge.hp < 0:
                  print("Rouge: Wait stop. I give up.  please don't kill me.")
                  input()
                  print("Jack: give me up one good reason why?")
                  input()
                  print("Rouge: I'm broke.  some of us poor people don't have a lot of money.  hell the jobs we get don't even pay us enough for a living.")
                  input()
                  print("Jack: what? I never thought the slums would be this bad.")
                  input()
                  print("Jack: Look I'll give back the momey I stole from that woman, but please do not arrest me?  I suffer enough as it is.")
                  input()
                  choice2 = input("What should I do to this thef?  A:turn him in?  B:let him go")
                  
                  if choice2 == ("A"):
                      print("Jack: I'm sorry but I cannot let this go.  you are under arrest.")
                      input() 
                      print("Rouge: I see.  well just do it.  I do not care anymore.")
                      input()
                      print("Jack arrested the thef and gave the money back to the woman.  however, hearing about the slum being this bad, was the arrest worth it?")
                      input()
                      print("you got the thowing bomb and 300 exp.")
                      input()
                      player.exp += 300
                      player.inventory.append("thowing bomb")
                      print("leavl up.  your hp is increased by 150")
                      input()
                      player.hp += 50 

                  if choice2 == ("B"):
                      print("Jack: leave")
                      input()
                      print("Rouge: what?  you are letting me go?")
                      input()
                      print("Jack: ya.  if what are you are saying is true, then I'm just going to let you be.  Just don't steel got it?")
                      input()
                      print("Rouge: yes sir.  I won't steel ever.  You have my word")
                      input()
                      print("you got potion and 300 exp.")
                      input()
                      player.exp += 300
                      player.money += 1000
                      player.inventory.append("potion")
                      print("leavl up.  your hp is increased by 120")
                      input()
                      player.hp += 50
    
    print("After dealing with the issue Jack has witness, he decided to go out of town and into the woods.")


    


                  
                  
                  
