import numpy as np

start_states = ['Rock', 'Paper', 'Scissors']
start_probabilities = [0.34, 0.33, 0.33]

transitions = start_states
transition_matrix = {
    #       R    P    S
    'Rock': [0.2, 0.5, 0.3],
    'Paper': [0.46, 0.36, 0.18],
    'Scissors': [0.375, 0.125, 0.5]
}

emissions = ['Won', 'Tied', 'Lost']
emissions_probabilities = {
    #       W     T    L
    'Rock': [0.6, 0.2, 0.2],
    'Paper': [0.36, 0.36, 0.28],
    'Scissors': [0.22, 0.56, 0.22]
}

state = np.random.choice(start_states, replace=True, p=start_probabilities)

games = 10

for game in range(1, games + 1):
    print(f'Game {game}')
    print(f'I choose: {state}')

    result = np.random.choice(emissions, replace=True, p=emissions_probabilities[state])
    state = np.random.choice(transitions, replace=True, p=transition_matrix[state])

    print(f'I {result}\n')
