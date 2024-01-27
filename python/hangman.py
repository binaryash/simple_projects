import random
nl = 0
d = []
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
b = random.choice(words)
f = len(b)
c = [x for x in b]
for y in range(0,f):
    d.append("-")
print(d)
while nl < 6:
    e = input("enter the letter")
    for i in range(0,f):
        if e == c[i]:
            d[i] = e
            print(d)
    if e not in c:
        nl+=1
        print(hangmanpics[nl])
    if '-' not in d:
        break
if nl == 6:
    print("\nBetter Luck Next Time !")
else:
    print("\nWow ! You Won")
