import random 

rock = 'rock'
paper = 'paper'
scissors = 'scissors'

choices = [rock, paper, scissors]
positive = [[rock, scissors], [scissors, paper], [paper, rock]]
negative = [[rock, paper], [scissors, rock], [paper, scissors]]


def get_comp_move():
    move = random.choice(choices)
    return move

def get_winner(user_move, computer_move):
    if [user_move, computer_move] in positive:
        return 1
    elif [user_move, computer_move] in negative:
        return -1
    return 0

print('===== LETS PLAY A GAME =====')

while 1: 
        move = input('Enter your move (rock, paper, scissors): ').lower()

        if 'rock' in move or 'paper' in move or 'scissors' in move:

            if move == 'rock':
                    user_move = rock
            elif move == 'paper': 
                user_move = paper
            else: user_move = scissors
        
            computer_move = get_comp_move()

            result = get_winner(user_move, computer_move)

            if result == 1:
                print('User won, congrats!')
            elif result == -1:
                print('Computer won, better luck next time!')
            elif result == 0: 
                print('Its a tie!')
                
            playAgain = input('Want to play again?')
            if playAgain.lower() != 'yes': break
        
        else: print('Invalid choice, try again!')

        
            



    
    


