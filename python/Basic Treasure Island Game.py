print("Welcome to the Treasure Island\n")
a = input("You are at crossroads where do you wanna go ? left or right ")
if a == 'left':
  print("You have crossed the forest and are standing in front of a river")
  b = input("Do you want to swim or wait? Enter any one to continue ")
  if b == 'wait':
    print("A boat comes by and drops you near a house")
    c = input("You are currently in front of three doors, red, blue and yellow, Enter one colour to continue ")
    if c == 'yellow':
      print("You Win!!")
    else:
      print("You Died, Game Over")
  else:
    print("You were eaten by sharks, Game Over")
else:
  print("You fell down a pit, Game Over")
