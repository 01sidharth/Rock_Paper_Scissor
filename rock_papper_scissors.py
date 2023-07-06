import random     

def play():
    user = input("Your choice 'r' for Rock ,'s' for Scissors,'p' for Paper \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You Win'
    
    return 'You Lose'

def is_win(player, opponent):
    #return true if player wins
    # r > s, s > p, p > r
     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')  or (player == 'p' and opponent == 'r'):
        return True
    
print(play())    