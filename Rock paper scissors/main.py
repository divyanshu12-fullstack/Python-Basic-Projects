import random


def play():
    user = input("What's Your move 'r' for Rock, 'p' for Paper and 's' for Scissors: ").lower()
    pc = random.choice(['r', 'p', 's'])
    if user == pc:
        return "It's a Tie"

    return winning_scenarios(user, pc)


def winning_scenarios(user, pc):
    if (user == 'r' and pc == 's') or (user == 'p' and pc == 'r') or (user == 's' and pc == 'p'):
        return "You Win!!"
    else:
        return "You Lose"


print(play())
