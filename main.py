print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

#Introduction
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_question = input("Would you like to turn left or right? ").lower()
if first_question == "left":
  second_question = input("Would you like to swim to find the treasure or wait until something happens? (Type swim or wait) ").lower()
  if second_question == "wait":
    third_question = input("Woah! Two doors have just appeared! Which do you choose red, blue, or yellow? ").lower()
    if third_question == "yellow":
      print("Congratulations you found the treasure! You win!")
    elif third_question == "red":
      print("You've just been burned to flames by dragons. Game over.")
    elif third_question == "blue":
      print("A pack of hungry wolves ate you. Game over.")
    else: 
      print("You chose a door that doesn't exist. Game over.")
  else:
    print("You've just been eaten by sharks. Game over.")
else: 
  print("Oh no! You fell into a hole. Game over.")