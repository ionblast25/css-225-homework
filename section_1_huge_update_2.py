import section_1_huge_update_2

def start(player):

   print("Jack is in a battle with a enemy knight")
   input()
   print("Jack fight his opponent")
   input()
   print("Jack beats his opponent")
   input()
   choice = input("what will you do? A:spare the Knight.  B:kill the Knight.")

   if choice == ('A'):
        print("Enemy Knight: Why spare me brave hero of the nexes kingdom?")
        input()
        print("jack: I'm not a blood tustry killer knight.  Sometime, not everyone needs to die.")
        input()
        print("Enemy Knight: I do not know your ways and I do not care.  however I am a generist man.  Here take the rest of my gold.")     
        input()
        print("Jack: You sure thats a good idea?")
        input()
        print("Enemy Knight: just take the dam gold and leave me be.")
        input()
        print("Jack: Find if that is what you want.")
        input()
        player.money += 1000
   elif choice == ("B"):
        print("Jack: Die villian!")
        input()
        player.exp += 150


   print("Jack Goes to the castle to report on his victory")
   input()
   print("The king ask if Jack has killed him")
   input()
   choice = input("what do I tell him?  A:tell the truth(or lie if the Knight is dead).  B:lie(or tell the truth if the Knight is alive,)")

   if choice == ("A"):
        print("Jack: I beat him, but I spare him death.")
        input()
        print("King: why did you not kill him?!  We are at war here!")
        input()
        print("Jack: What is the point. I only kill if people deserve it.")
        input()
        print("King: Whatever as long as we win this, nothing matter as of now.  leave Jack.")
        input()        
        print("jack: As you wish my King.")
        input()

   elif choice == ("B"):
        print("Jack: Yes, he is dead.")
        input()
        print("King: Very good my hero.  we just steps away from vitory from this war.")
        input()      
        print("Jack: Of couse my King.")
        input()
        print("King: Go and gets some rest.  you earn it.")
        input()
        print("Jack: that I will do.")
        input()
    
   print("Jack goes to his home to rest")
   input()
   print("Jack goes to sleep on his bed.")


