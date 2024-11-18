import numpy as np
import random
import matplotlib.pyplot as plt
from time import sleep

NUM_RESOURCES = 10  # Total resources to allocate
LEGIT_TRAFFIC = 50  # Base legitimate traffic requests
ATTACK_INTENSITY = [0, 10, 20, 30]  # Levels of attack intensity
EPISODES = 1000  # Number of episodes for training
ACTIONS = [0, 1, 2, 3, 4, 5]  # Actions: Resources to allocate to mitigate attack

# Q-Learning parameters
ALPHA = 0.1  # Learning rate
GAMMA = 0.9  # Discount factor
EPSILON = 0.8  # Initial exploration rate
EPSILON_MIN = 0.1  # Minimum exploration rate
EPSILON_DECAY = 0.99  # Decay rate for epsilon

# Initialize Q-table
q_table = np.zeros((len(ATTACK_INTENSITY), len(ACTIONS)))

# Environment function
def simulate_environment(attack_intensity, defense_resources):
    """
    Simulates the environment.
    Returns reward based on how well the RL agent allocates resources.
    """
    remaining_resources = NUM_RESOURCES - defense_resources
    legit_served = min(remaining_resources, LEGIT_TRAFFIC)
    attack_mitigated = min(defense_resources, attack_intensity)
    
    # Reward: legitimate traffic served minus penalty for unmitigated attack
    reward = legit_served - (attack_intensity - attack_mitigated)
    return reward

# Choose an action (epsilon-greedy)
def choose_action(state):
    global EPSILON  # Declare EPSILON as global so it can be modified
    if random.uniform(0, 1) < EPSILON:
        return random.choice(ACTIONS)  # Explore
    else:
        return np.argmax(q_table[state])  # Exploit

# Training
for episode in range(EPISODES):
    for intensity_level, attack_intensity in enumerate(ATTACK_INTENSITY):
        # RL agent's action
        action = choose_action(intensity_level)
        defense_resources = ACTIONS[action]
        
        # Simulate the environment
        reward = simulate_environment(attack_intensity, defense_resources)
        
        # Update Q-value
        next_state = intensity_level  # Environment is static, so next state = current state
        best_future_q = max(q_table[next_state])
        q_table[intensity_level, action] += ALPHA * (reward + GAMMA * best_future_q - q_table[intensity_level, action])

    # Decay epsilon
    EPSILON = max(EPSILON_MIN, EPSILON * EPSILON_DECAY)

print("Training complete! Trained Q-table:")
print(q_table)

# Live Simulation with Persistent Graph
def live_simulation():
    print("\nStarting live simulation... Press Ctrl+C to stop.")
    
    # Setup for dynamic bar graph (attack vs defense)
    plt.ion()
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    bars = ax1.bar(["Attack Intensity", "Defense Allocated"], [0, 0], color=["red", "green"])
    ax1.set_ylim(0, max(NUM_RESOURCES, max(ATTACK_INTENSITY)))
    ax1.set_title("Real-Time Attack vs. Defense Simulation")
    ax1.set_ylabel("Resources")
    ax1.grid()

    # Setup for dynamic line graph (reward tracking)
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    reward_line, = ax2.plot([], [], label="Reward", color="blue")
    ax2.set_xlim(0, 100)  # Limiting x-axis to show 100 data points
    ax2.set_ylim(-NUM_RESOURCES, NUM_RESOURCES)  # Reward range
    ax2.set_title("RL Agent's Performance Over Time")
    ax2.set_xlabel("Time (Episodes)")
    ax2.set_ylabel("Reward")
    ax2.legend(loc="upper right")
    ax2.grid()

    reward_history = []  # To store rewards over time for the line graph

    while True:
        attack_intensity = random.choice(ATTACK_INTENSITY)
        state = ATTACK_INTENSITY.index(attack_intensity)
        best_action = np.argmax(q_table[state])
        defense_resources = ACTIONS[best_action]
        reward = simulate_environment(attack_intensity, defense_resources)

        # Update the bar graph dynamically (showing attack intensity vs defense resources)
        bars[0].set_height(attack_intensity)
        bars[1].set_height(defense_resources)
        ax1.set_title(f"Attack Intensity: {attack_intensity} | Defense: {defense_resources} | Reward: {reward}")

        # Update the reward history and line graph
        reward_history.append(reward)
        if len(reward_history) > 100:  # Limit the history to 100 values
            reward_history.pop(0)
        
        reward_line.set_xdata(np.arange(len(reward_history)))
        reward_line.set_ydata(reward_history)

        # Pause to update the graphs in real-time
        plt.pause(0.5)  # Update graph every 0.5 seconds
        
if __name__ == "__main__":
    try:
        live_simulation()
    except KeyboardInterrupt:
        print("\nLive simulation ended.")
        plt.close('all')  
