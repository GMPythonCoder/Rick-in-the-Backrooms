import os
import time
import sys
import random

def cls(): os.system('clear')

title = """

███████████████████████████████████████████████████████
█▄─▄▄▀█▄─▄█─▄▄▄─█▄─█─▄███▄─▄█▄─▀█▄─▄███─▄─▄─█─█─█▄─▄▄─█
██─▄─▄██─██─███▀██─▄▀█████─███─█▄▀─██████─███─▄─██─▄█▀█
▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▀▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄
███████████████████████████████████████████████████████
█▄─▄─▀██▀▄─██─▄▄▄─█▄─█─▄█▄─▄▄▀█─▄▄─█─▄▄─█▄─▀█▀─▄█─▄▄▄▄█
██─▄─▀██─▀─██─███▀██─▄▀███─▄─▄█─██─█─██─██─█▄█─██▄▄▄▄─█
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀
------------------------------------------------------- 
By Dehan Gunsinghe and Bobby Elmore
"""

input(f"{title}Press Enter...")
print("Hello There Young One, It seems like you have been taking to the backrooms! Well If you want to come back to the Frontrooms(Outside World) you need to escape. But it isn't easy though. There are monsters unthinkable inside here and the backrooms are infinate. There's only one exit so Good Luck Young One. But First before you start your journey I think you need a friend so you I give you Rick Astley! Good Luck on your Journey!")
print("Also when you want to go North then press N,South press S,West press W,East press E")


n = input('>')
if (n == "N"):
  print("You and Rick have arrived to this backroom, you see no monsters luckily but you hear a noise behind you what will you and Rick do?!")
        
elif (n == 'S'):
  print("You choose this backroom, as you and Rick arrived you guys saw a monster!, as you  tried to slowly go back, Rick started singing Hey monster I want to tell you something Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you" 'The monster sees you and Rick, You pull Rick and run which room will you choose and will you and Rick be safe')
elif (n == 'W'):
  print("Well Well Well Looks like you and Rick choose to this backroom you see dead boddies lying down you wonder what happened and you see your friend Rick gone! Where did he go will you find him or go with out him?")
      
elif (n == "E"):
  print("You came to this backroom looks like you and Rick look around it looks perfectly normal Rick and you hear a roar! You and Rick are worried you see a portal in the backroom north of you will go thorugh it?!")
elif (n != "N","S","W","E"): 
  print("Please put in one of these letters in Capital Form Thank You")

n2 = ""
if n == "N":
  n2 = input('N>')
  if (n2 == "N"):
    print("You and Rick went the northroom. You hear the roaring stop but hear loud stomps. You and Rick are afraid but you decided to keep going. But you didn't notice an mysterious shadow looking at you! ")
          
  elif (n2 == 'S'):
    print("You and Rick go back into the room we started in and saw nothing but behind you there was a monster and quickly killed both you and Rick ")
    print('You died')
  elif (n2 == 'W'):
    print("You and rick go west you hear the roaring stop you and Rick see a bed in the room you were about the sleep in it when you see bed bugs you go away from the bed and decided to go into another room")
        
  elif (n2 == "E"):
    print("You and Rick go east and see a key in the room. You wonder what that is. You get the key and put it into your pocket! ")

if n == "S":
  n2 = input('S>')
  if (n2 == "N"):
    print("You and Rick go north and the monster chases both of you, you and rick dodge the monsters killing blows. You see a sword that is in the room that you didn't see until now. You get the sword and kill the monster before it kills both you and Rick. ")
          
  elif (n2 == 'S'):
    print("You and Rick you south the monster chases you, you and Rick see many more monsters before you even start to run the monsters kill you and Rick")
    print('You died')
  elif (n2 == 'W'):
    print("You and Rick go west the monster follows you and Rick into the room suddenly theres no rooms to escape from. Looks like you and Ricks fath has been decided you and Rick try to lure the monster away to escape but the monster kills you and Rick as you and Rick got tired from running around from the monster")
    print("You died")
        
  elif (n2 == "E"):
    print("You and Rick go to east suddenly you see a button, you click the button and automaticly the backroom opening close in the way that you came in. The monster was about to come in when the metal plate from the door sliced the monster in half!") 

if n == 'W':
  n2 = input('W>')
  if (n2 == "N"):
      print("You go north you see nothing there. But you see blood everywhere. But luckly it's not recent. The blood seemed to spill a long time ago. You go and try to find Rick again when suddenly a monster that you didn't see comes and kills you")
      print("You died")
  elif (n2 == 'S'):
      print("You try to find rick when you see a map. You go to the map and pick it up. When you see the map it has a tracker of where you are and where rick and monsters are. When you look on it you see rick's position but there is also monsters in the postion surronding rick. You also see the portal to the portal room that you need to go. You decided that you should go to the portal room or go and save rick! But you before you make that decsion the map says that 2 people have to be in the portal room at the same time!")
  elif (n2 == 'W'):
      print("You go west to try to find rick but a monster comes and kils you ")
      print('You died')
  elif (n2 == "E"):
      print("You go east and check the room you see nothing but suddenly you see a key.  You grab the key to inspect it but before you can see inspect it more a monster comes behind you at lighting speed and kills you")
      print('You died')

if n == 'E':
  n2 = input('E>')
  if (n2 == "N"):
    print("You and rick go into the portal. In the portal it says that no monsters can come. You and rick and happy that no monsters can come inside the portal, outside there are many monsters waiting to eat you and kill you you and rick find a door  you try to open it but it's locked it looks like it needs a key. You can't go outside because of the monsters instead luckly their are other portals that can insert you and rick into the backrooms in other places! ")
          
  elif (n2 == 'S'):
    print("You and Rick didn't choose the portal so you decide to head south to look for the noise. You and rick saw nothing in the room. As you and Rick were about the turn around a monster did a battle cry of trumiph and killed you and Rick ")
    print('You died')
    
  elif (n2 == 'W'):
    print("You and Rick didn't choose the portal so you decide to head west to look for the noise. You and Rick saw a monster in the room but sadly the monster knew that you and Rick were comming into the room and did a battle cry and then suddenly monster sorunded you and Rick. You and Rick knew this is the end of their lifes so and you and Rick fought the monsters by hand. You and Rick fought bravely but the monsters just killed you and Rick before you guys could take a monsters life in battle")
    print('You died')
    
  elif (n2 == "E"):
    print("You and Rick didn't choose the portal so you decide to head east to look for the noise. There was nothing in the room. But there was hot water in the room. It was like this room was a bathroom because it had a really bad smell. Then suddenlly right behind you and rick a monster came to use the bathroom when he saw you and Rick the monster then did a big roar and slashed and killed you and Rick")
    print('You died')

n3 = ""
if n == "N" and n2 == "N":
  n3 = input('N>')
  
  if (n3 == "N"):
    print("You and Rick went north. You still hear the large stomping until you hear a fatel cry of death. You and Rick are shocked you wondered what was happening until you saw a mysterious figure staring into you as soon as the mysterious figure noticed you looking at you the myerterious figure reveled to you and Rick as the female dancer in the famous song of Rick Astleys life Kristin Seifert ")
          
  elif (n3 == 'S'):
    print("You and Rick went south. You see the monster. The monster saw and did a battle cry and was about to kill you and Rick when a myerterious figure came and killed the monster. As you and Rick were shocked the myerterious figure reveled to you and Rick as the female dancer in the famous song of Rick Astleys life Kristin Seifert ")
    
  elif (n3 == 'W'):
    print("Looks like You and Rick went west. You hear the monster's thundering steeps behind you then suddenly you see a myerterious figure killing the monster you tell Rick to see and both of you were in shock then when the myerterious figure saw you and Rick the myerterious figure releved to you and Rick as thefemale dancer in the famous song of Rick Astleys life Kristin Seifert")

        
  elif (n3 == "E"):
    print("You and Rick went East. Once in the room you hear a shriek of the monster and then thundering footsteps that disapered. Both of you were shocked to hear the monster terifed of something and you didn't have to find out long about who scared the monster. It was an ordinary human. the ordinary human relveled to you and Rick as the female dancer in the famous song of Rick Astleys life Kristin Seifert")

if n == "N" and n2 == "W":
  n3 = input('N>')
  
  if (n3 == "N"):
      print("You and Rick went north to see if there is a something that will help you get yu both home. But there's nothing")
            
  elif (n3 == 'S'):
      print("You and Rick went south. There's nothing in that room that will help you.")
      
  elif (n3 == 'W'):
      print("You and Rick went west and you saw water and food. You and Rick decided to eat the food and drink that water right now. It was delicious!")
  
          
  elif (n3 == "E"):
      print("You and Rick went east. There was a tripwire which you and Rick trip on. But luckly the tripwire didn't do anything harmless. When you and Rick inspect the tripwire. You see that the tripwire was active for like 1,0000000000000 years ago. You wonder who had setted up that tripwaire!!!!!!")

if n == "N" and n2 == "E":
  n3 = input('N>')
  
  if (n3 == "N"):
      print("You and Rick head north to find thing that could unlock with the key. But sadly there wasn't any portal and there was a monster instead. The monster saw you and did a killing swip and killed you and Rick.")
      print('You died')
            
  elif (n3 == 'S'):
      print("You and Rick head south to see if there is something to fit this key but there was nothing but a portal!!!!!")
      
  elif (n3 == 'W'):
      print("You and Rick head west to investigate if there is something to fit the key in something but there was nothing. ")
  
          
  elif (n3 == "E"):
      print("You and Rick head east to see if there is something to fit this key but there was nothing.")

if n == "S" and n2 == "N":
  n3 = input('N>')

  if (n3 == "N"):
      print("After you killed the monster and saved Rick. You and Rick went north. There was nothing there. Even monsters luckly ")
      
  elif (n3 == 'S'):
      print("After you killed the monster and saved Rick. You went back south to explore why the monster was there. In the room there was a nest Inside there was baby monsters sleeping. They were the size of a small bird. You and quickly relaize why the monster was gurading the room. You and Rick decided to kill the baby monsters so they wouldn't haunt any other travelers in the backrooms. As you lifted up the sword to kill the monster suddenly there was a roar. The monster of the one that you just killed came. It looks like monsters can heal andhave infinate lives. She comes to save her kids. She does a blood crying roar and Suddenly the Dad of the baby monsters arrived it's 2 against 2. What will happan to you and Rick!!!!!!!")
      
  elif (n3 == 'W'):
      print("You and Rick go west after killing the monster you look if theres anything that you and Rick need. But there was nothing ")
  
          
  elif (n3 == "E"):
      print("You and Rick go east after killing the monster. There were no monsters or anything in the room.")

if n == "S" and n2 == "E":
  n3 = input('N>')
  
  if (n3 == "N"):
      print("As you and Rick saw the fath of the monster both of you are in shock as you both saw the monster fath. You and Rick went north when suddenly the door was closing behind you and suddenly the entraces of the backrooms closed. No one in or out could escape Looks like you and Ricks fath were up as you 2 straved to death.")
      print('You died')
      
  elif (n3 == 'S'):
      print("As you and Rick saw the fath of the monster both of you are in shock as you both saw the monster fath. You and Rick went south when suddenly the door was closing behind you and suddenly the entraces of the backrooms closed. No one in or out could escape Looks like you and Ricks fath were up as you 2 straved to death.")
      print('You died')
      
  elif (n3 == 'W'):
      print("As you and Rick saw the fath of the monster both of you are in shoc as you both saw the monster fath. You and Rick went north when suddenly the door was closing behind you and suddenly the entraces of the backrooms closed. No one in or out could escape Looks like you and Ricks fath were up as you 2 straved to death.")
      print('You died')
  
          
  elif (n3 == "E"):
      print("As you and Rick saw the fath of the monster both of you are in shoc as you both saw the monster fath. You and Rick went north when suddenly the door was closing behind you and suddenly the entraces of the backrooms closed. No one in or out could escape Looks like you and Ricks fath were up as you 2 straved to death.")
      print('You died')
    
if n == "W" and n2 == "S": 
  n3 = input('N>')  

  if (n3 == "N"):
      print("Looks like you are taking an shortcut to save Rick! But sadly for you as you came into a room. A monster that you can't see or hear kills you.")
      print('You died')
      
  elif (n3 == 'S'):
      print("Looks like you are taking the origanal route to save Rick. Luckly there is no monsters in the room!")
      
  elif (n3 == 'W'):
      print("Looks like you were bold and daring to not follow the orignal route sadly for you a monster was there with a blood shrike cry the monster killed you")
      print('You died')
    
  elif (n3 == "E"):
      print("Looks like you don't to save Rick or follow the origanal path of the map. Luckly there were no monsters in the room!")

if n == "E" and n2 == "N":
  n3 = input('N>') 

  if (n3 == "N"):
      print("You and Rick went to the north because of the north portal. Theres no monsters in the room luckly. But you and Rick hear the blood cries and screams of the monsters!")
    
  elif (n3 == 'S'):
      print("Looks like you and Rick went south because of the south portal. You and Rick didn't see anything first then you saw a moving object like flying in the air. Then suddenly Rick fell on the floor and when you looked up a monster did a scream and killed you")
      print('You died')
      
  elif (n3 == 'W'):
      print("You and Rick went west because of the west portal. You and Rick sadly saw many monsters. As you tried to not make any noise. With absolutly luck the a monster saw you and did a blood pirecing cry with the other monsters turned around and did the same thing and then ran with lighting speed and killed you and Rick before you could even breathing for the last time")
      print('You died')
    
  elif (n3 == "E"):
      print("You and Rick went east because of the east portal. You and Rick saw no monsters luckly. You and Rick hear blood pirecing cries and screams of the monsters.")

if n == "N" and n2 == "N" and n3 == 'N' or n3 == "S" or  n3 == 'W' or n3 == 'E' :
  n4 = input('N>')

  if (n3 == "N"):
      print("You and Rick are shocked how Kristin Seifert is in the backrooms. You asked Kristin Seifert if she wants to come with you and Rick. She didn't replie and when you and Rick went north. Once in that backroom you didn't find anything. But Kristin Seifert followed you and Rick. You and Rick were glad at frist. But then she spoke in an ominous voice saying Rick I'm so glad that I found you and your partner then she reveled her true form a human toung speaking monster! Then she lunged really fast and killed you and Rick")
      print('You died')
  elif (n3 == 'S'):
      print("You and Rick are shocked how Kristin Seifert is in the backrooms. You asked Kristin Seifert if she wants to come with you and Rick. She didn't replie and when you and Rick went south. Once in that backroom you didn't find anything. But Kristin Seifert followed you and Rick. You and Rick were glad at frist. But then she spoke in an ominous voice saying Rick I'm so glad that I found you and your partner then she reveled her true form a human toung speaking monster! Then she lunged really fast and you and Rick and killed you and Rick")
      print('You died')
    
  elif (n3 == 'W'):
      print("You and Rick are shocked how Kristin Seifert is in the backrooms. You asked Kristin Seifert if she wants to come with you and Rick. She didn't replie and when you and Rick went west. Once in that backroom you didn't find anything. But Kristin Seifert followed you and Rick. You and Rick were glad at frist. But then she spoke in an ominous voice saying Rick I'm so glad that I found you and your partner then she reveled her true form a human toung speaking monster! Then she lunged really fast and killed you and Rick!")
      print('You died')

  elif (n3 == "E"):
      print("You and Rick are shocked how Kristin Seifert is in the backrooms. You asked Kristin Seifert if she wants to come with you and Rick. She didn't replie and when you and Rick went east. Once in that backroom you didn't find anything. But Kristin Seifert followed you and Rick. You and Rick were glad at frist. But then she spoke in an ominous voice saying Rick I'm so glad that I found you and your partner then she reveled her true form a human toung speaking monster! Then she lunged really fast and you and Rick and killed you and Rick")
      print('You died')

if n == "N" and n2 == "W" and n3 == "N":
  n4 = input('N>')

  if (n3 == "N"):
      print("You and Rick went north to see if theres anything that could help you 2. There was nothing in that room")
    
  elif (n3 == 'S'):
      print("You and Rick went south to see if there was anything that could help you and Rick sadly there was a monster who quickly killed you and Rick")
      print('You died')
    
  elif (n3 == 'W'):
      print("You and Rick went west to see if there was anything that could help you and Rick sadly there was a monster who quickly killed you and Rick")
      print('You died')
    
  elif (n3 == "E"):
      print("You and Rick went east to see if there was anything that could help you and Rick sadly there was a monster who quickly killed you and Rick")
      print('You died')

if n == "N" and n2 == "W" and n3 == "S" :
  n4 = input('N>')

  if (n3 == "N"):
      print("f")
      
  elif (n3 == 'S'):
      print("f")
    
  elif (n3 == 'W'):
      print("f")
    
  elif (n3 == "E"):
      print("f")
    
  