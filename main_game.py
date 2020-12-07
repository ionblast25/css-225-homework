#Remember to put all your files into the same folder on your computer!
#Otherwise, these import statements won't be able to find them properly

#Import all files you'll need to run this properly
import main_character as mc
import section_1_huge_update_2
import section_2
import section_3


#Create our player character from our main_character class
player = mc.main_character()

#Intro text to the user
#The empty input functions are only here so the player has to type something to move on
#(like pressing a button in a video game to move the dialogue along)
print("Hello there!")
print("Welcome to my game")
input()

#And do/say anything else to get your game started

#Then call your first section.
#Be sure to pass in your player character
section_1_huge_update_2.start(player)
section_2.start(player)
section_3.start(player)
