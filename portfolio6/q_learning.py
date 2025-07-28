import numpy as np
import random

# Ambiente 4x4
n_states = 16
actions = ['up', 'down', 'left', 'right']
q_table = np.zeros((n_states, len(actions)))
rewards = np.full(n_states, -1)
rewards[15] = 10  # Estado final com recompensa positiva

def get_next_state(state, action):
    row, col = divmod(state, 4)
    if action == 'up' and row > 0:
        row -= 1
    elif action == 'down' and row < 3:
        row += 1
    elif action == 'left' and col > 0:
        col -= 1
    elif action == 'right' and col < 3:
        col += 1
    return row * 4 + col

# Q-Learning
alpha = 0.1
gamma = 0.9
epsilon = 0.1
episodes = 500

for _ in range(episodes):
    state = 0
    while state != 15:
        if random.uniform(0, 1) < epsilon:
            action_idx = random.randint(0, 3)
        else:
            action_idx = np.argmax(q_table[state])
        next_state = get_next_state(state, actions[action_idx])
        reward = rewards[next_state]
        old_value = q_table[state, action_idx]
        next_max = np.max(q_table[next_state])
        q_table[state, action_idx] = old_value + alpha * (reward + gamma * next_max - old_value)
        state = next_state

# Caminho aprendido
state = 0
path = [state]
while state != 15:
    action_idx = np.argmax(q_table[state])
    state = get_next_state(state, actions[action_idx])
    path.append(state)

print("\n\nCaminho encontrado pelo agente:\n")
print(" -> ".join(map(str, path)))
print(f"\n\nNúmero total de passos: {len(path) - 1}\n\n")