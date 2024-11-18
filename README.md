
# RL-Based Cloud DDoS Defense Simulation

This project demonstrates a **reinforcement learning (RL)** approach for defending against a simulated **Distributed Denial of Service (DDoS) attack** on a cloud system. The system dynamically allocates resources based on varying attack intensities, and the RL model learns how to effectively mitigate the attacks while balancing legitimate traffic demands.

### Project Features:
- **Q-Learning Model**: An RL-based agent learns to allocate resources optimally based on the intensity of simulated DDoS attacks.
- **Real-time Simulation**: Displays dynamic bar and line graphs showing attack intensity, defense resources, and the agent's performance (reward) over time.
- **Interactive Visualizations**: Two real-time graphs show the current attack vs. defense resources and track the agent's performance (reward) as it trains.

---

## Installation

### Requirements:
- Python 3.7+
- Required Python libraries: `numpy`, `matplotlib`

You can install the necessary libraries using `pip`:

```bash
pip install numpy matplotlib
```

### Running the Simulation:
To run the simulation, simply execute the Python file:

```bash
python Simulation.py
```

### Project Structure:
```
RL-Based-Cloud-DDoS-Defense/
├── Simulation.py       # Main simulation script with Q-Learning and real-time visualization
├── README.md           # Project overview, installation, and usage guide
```

---

## How It Works

1. **Q-Learning**: The agent interacts with a simulated environment where it has to defend against different levels of DDoS attacks using available resources.
2. **Simulation**: The environment simulates a range of attack intensities and rewards the agent based on how well it allocates defense resources.
3. **Graphs**: Real-time updates to show attack intensity vs defense resources allocated by the agent and track the agent's reward over time.

---

## How to Use

1. **Train the Agent**: The simulation runs through 1000 episodes where the agent learns to allocate resources effectively based on attack intensity using Q-learning.
2. **Live Simulation**: After training, the system runs in live mode, dynamically updating the bar graph to reflect real-time attack and defense conditions. The line graph tracks the agent's reward over time, showing how it adapts its strategy as the simulation progresses.

---

## Code Explanation

### Key Components:
- **Q-Learning Parameters**: 
  - `ALPHA`: Learning rate.
  - `GAMMA`: Discount factor.
  - `EPSILON`: Exploration rate (balance between exploration and exploitation).
- **Reward Calculation**: The agent receives a reward based on how well it defends against the attack while serving legitimate traffic.
- **Graph Updates**: Real-time updates to show the agent's decisions and performance in a visual format.

---

## Example Output

Once the script is running, you will see two windows:

1. **Bar Graph**: Displays the intensity of the attack and the defense allocated by the agent.
2. **Line Graph**: Tracks the agent's performance (reward) over time.

The agent adapts to allocate resources effectively and mitigate attacks, which can be seen by improvements in the reward graph.

---

## Contributions

**Contributions are not accepted for this project.**  
This is a personal project, and the code is not open for modification or contributions from the community. Please respect the integrity of the project.

---

## License

This project does not use any open-source license. It is a homemade project created for educational purposes, and it is not intended for distribution or commercial use.



