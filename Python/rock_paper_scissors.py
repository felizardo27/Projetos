import random 

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if (user == computer):
        return "It\'s a tie"

    if is_win(user, computer):
        return f"You Win!! computer choice {computer}"

    return f"You lost! computer choice {computer}"

def is_win(user, opponent):
    # r > s, s > p, p > r
    if (user == 'r' and opponent == 's') or (user == 's' and opponent == 'p') or (user == 'p' and opponent == 'r'):
        return True

print(play())