
# coding: utf-8

# In[20]:

max_snakes=15
max_ladders=15
board_size =(10,10)

total_test_cases = 0
test_cases = {}
import random


# In[21]:

def read_input(filename):
    with open(filename, 'r') as fd:
        inputs = fd.readlines()
    total_test_cases = int(inputs.pop(0).strip('\n'))
    for i in range(total_test_cases):
        die_probabilities = list(map(float, inputs[4*i + 0].strip('\n').split(',')))
        assert len(die_probabilities == 6)
        n_ladders, n_snakes = list(map(int, inputs[4*i + 1].strip('\n').split(',')))

        ladders = [tuple(list(map(int, each.split(',')))) for each in inputs[4*i + 2].strip('\n').split(' ')]
        snakes = [tuple(list(map(int,each.split(',')))) for each in inputs[i*4 + 3].strip('\n').split(' ')]
        assert(len(ladders) == n_ladders)
        assert(len(snakes) == n_snakes)
        test_cases[i+1] = [die_probabilities, (n_ladders, n_snakes), ladders, snakes]
    assert len(test_cases) == total_test_cases



# In[ ]:

def update_snakes_and_ladders(game, die_end_pos):
    ladders = game[2]
    snakes = game[3]
    #Nicely the input data has ladders in right (low start to high end ) and snakes in ulta. so I can pull this off
    for lad in ladders + snakes:
        if lad[0] == die_end_pos:
            return lad[1]
    return die_end_pos

    pass

def choose_die_value(die_probs):
    # Assuming two decimal point accuracy
    source =''.join([ str(i+1)*int(100*each)  for i,each in enumerate(die_probs)])
    chosen = random.choice(source)
    return chosen


# Simulate 5000 games and  find mean game end time
def simulate_game(game):
    n_simulations = 5000
    #n_simulations = 10000
    all_moves_total = 0
    all_comp_games_cnt = 0
    for i in range(n_simulations):
        player_pos=0
        moves = 0
        die_probs = game[0]
        while (moves <=1000):
            die_choose = choose_die_value(die_probs)
            moves += 1
            prev_pos = player_pos
            player_pos += int(die_choose)
            player_pos = update_snakes_and_ladders(game, player_pos)
            # If the die move ends up > 100. ignore it
            if player_pos > 100:
                player_pos = prev_pos
                moves -= 1
            if player_pos==100:
                all_moves_total += moves
                all_comp_games_cnt += 1
                break
    print(all_moves_total/all_comp_games_cnt)



# In[ ]:

read_input('./snakes_and_ladders_input.txt')
for each in test_cases.values():
    simulate_game(each)

#import pdb; pdb.set_trace()
#simulate_game(test_cases[1])

# Hmm.. looks like the 2nd test case falls out of the +/- 10% range in my simulation.
# Ah well. for now just shrugging shoulders.... later should construct more test cases and test.

# Ironically doubling the num. of simulations doesn't change a thing.. still same 120 or so moves
# for second board/test case...

# should try keep the probabilities and change the num. of snakes and ladders(or difference between num.of
# snakes and ladders)
#hmmm... Should try same num. of snakes and ladders next time changing the probabilities
