## Text Monster Game
## The goal of this game is to beat the monsters and claim the prize at the end of the dungeon.

# Map of the dungeon
# Feel free to adapt and design your own level. The whole map must be at least 3 floors and 15 rooms total, though.
floor0 = ['empty', 'sword', 'stairs up', 'monster', 'empty']
floor1 = ['magic stones', 'monster', 'stairs down', 'empty', 'stairs up']
floor2 = ['prize', 'boss monster', 'sword', 'sword', 'stairs down']

# Items in the player's possession
inventory = []

# Player's current position in the dungeon
# The player starts in the first room on floor 0
currentFloor = 0
currentRoom = 0

# Keep track of whether the game is in progress or over (so we know when to stop the game loop)
gameState = 'ongoing'

while gameState == 'ongoing':
  # Describe the room the player is in
  if currentFloor == 0:
    floor = floor0
  elif currentFloor == 1:
    floor = floor1
  else:
    floor = floor2
  room = floor[currentRoom]
  if room == 'empty':
    print('You are in an empty room.')
  # You need to handle describing the other cases..

  # Get command from the player
  choice = input('Command? ')

  # Respond to command
  if choice == 'help':
    # Help: display all commands
    # Note that the "pass" keyword in Python is a placeholder for lines where the interpreter would normally expect to see code. If control flow reaches the line with "pass", the interpreter "passes" over the line (i.e. does nothing).
    pass
  elif choice == 'left':
    # Player wants to move left
    pass
  elif choice == 'right':
    # Player wants to move right
    pass
  elif choice == 'up':
    # Player wants to go upstairs
    pass
  elif choice == 'down':
    # Player wants to go downstairs
    pass
  elif choice == 'grab':
    # Player wants to grab item from the room
    pass
  elif choice == 'fight':
    # Player wants to fight monster in the room
    pass
  else:
    print('Command not recognized. Type "help" to see all commands.')

if gameState == 'won':
  print('You won the game! :)')
else:
  print('You lost the game. :( Maybe next time.')
