# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    
    if prev_play:
        opponent_history.append(prev_play)

    if not opponent_history:
        return 'R'
 r_count = opponent_history.count('R')
    p_count = opponent_history.count('P')
    s_count = opponent_history.count('S')

predicted = max(('R', r_count), ('P', p_count), ('S', s_count), key=lambda x: x[1])[0]

  if predicted == 'R':
        return 'P'  # Paper beats Rock
    elif predicted == 'P':
        return 'S'  # Scissors beats Paper
    else:
        return 'R'  # Rock beats Scissors




