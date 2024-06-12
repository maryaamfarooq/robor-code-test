import random

board = ['S', '1' , '2' , '3' , '4' , '5' , '6' , '1' , '2' , '3' , '4' , '5' , '6' , '1' , '2' , '3' , '4' , '5' , '6' , '1' , '2' , '3' , '4' , '5' , '6' , 'E']

print(len(board))

game_end = False

# Keeps track of players' current positions
players_position_index = [0, 0]

dice1 = 0
dice2 = 0

while not game_end:

    # Runs twice, once for each player
    for i in range(2):
        inp = input("Player " + str(i + 1) + " turn. Press enter")

        # Dice roll
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)

        print('Dice 1:', dice1)
        print('Dice 2:', dice2)

        # If player is at 'S'
        if players_position_index[i] == 0:
            current_position = 0
        else:
            current_position = int(board[players_position_index[i]])
            
        # If dice rolls are different, choose the max value
        if(dice1 != dice2):
            next_position = max(dice1, dice2)
        # If dice roll are same, add six to go to the second occurence of the dice value
        else:
            next_position = dice1 + 6

        if next_position > current_position:
            players_position_index[i] = players_position_index[i] + (next_position - current_position)
        else:
            players_position_index[i] = players_position_index[i] + ((6 - current_position) + next_position)
        
        if(players_position_index[i] >= len(board)):
            print("Winner: Player ", i+1)
            game_end = True
            break
        
        print("Player ", i + 1, " current position: ", board[next_position], '\t\t\t\tIndex:', players_position_index[i])
        

        

