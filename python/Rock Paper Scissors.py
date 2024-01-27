import random

def play():
    user = input("Enter r for rock, p for paper , s for scissors")
    computer = random.choice(['r','p','s'])
    print(computer)

    if user == computer:
        return "it is a tie"
    
    if is_win(user,computer):
        return "youve won , Hurray"

    return "you lost"


def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

print(play())