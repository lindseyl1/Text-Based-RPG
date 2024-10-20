'''BEFORE GAME STARTS'''
'''Define instructions:
Escape the Medieval Prison Game
Collect 6 items to prepare for your freedom
And most importantly... avoid the beast!

Move commands: go north, go south, go east, go west
Add to inventory: get 'item name'
'''

'''
Define invalid inputs as anything that's not a move command or 
an get item command.
'''

'''
Define status of player as:
displaying the current room the player is in 
& all items in inventory
'''

'''
Define inventory as a list and make empty at start of the game.
'''

'''
Define room locations as a dict.
With linking the rooms together by direction of each other.
Ex: 'Cell Room' : {'West': 'Hallway'}
'''



'''
enter the game inside this statement:
while != 'quit'
'''
########################################
'''
INSIDE GAME:

Display instructions &
Prompt user to begin game by inputting 'begin'
or to exit game by inputting 'quit'
'''

'''
Create function to start player in cell room.
Prompt the user to move into the next room by the move commands.
Based on the move commands, enter the room in that direction.
'''

'''
Display descriptions of the player's surroundings
so they can find all of the items.

Once an item is found, its entered into the inventory
'''
###########################
'''
ENCOUNTER THE BEAST:
Display descriptions and how the beast attacks you.

Display:
Game Over. Unfortunately you have been eaten by the beast. Type 'begin'
to play again or 'quit' to exit the game.

begin = start game over
quit = exit game
'''
##################################
'''END OF GAME'''

'''
condition: if all of the items aren't found, the player cannot leave.
Display: 
Wait. Not all of the items are found. Let's go back.

else:
  Display:
  Congratulations! You've safely escaped the prison! 
  Your hard work has payed off!

'''
