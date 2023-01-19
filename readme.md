This repo implements a Gridworld environment that can be used to train Reinforcement Learning (RL) agents.

An agent can navigate the grid, learn to collect rewards, and avoid obstacles.

# Demo

<img src="https://raw.githubusercontent.com/bay3s/grid/main/assets/episodes.gif" width='400'>

#### Local installation

```sh
pip install git+https://github.com/bay3s/grid.git@main
```

## Usage:

```python
from grid import Grid
import matplotlib.pyplot as plt
import random


env = Grid(size = 9, partial = False)

MAX_STEPS = 50
MAX_EPISODES = 100

for i in range(NUM_EPISODES):
  prev_state = env.reset()
  is_done = False
  steps = 0

  while not is_done and steps < MAX_STEPS:
    action = random.choice([0, 1, 2, 3])
    state, reward, is_done = env.step(action)
    steps += 1
```

### Action spaces:
The actions that an agent is able to take in the environment are as follows:

  * 0 - step up
  * 1 - step down
  * 2 - step left
  * 3 - step right 

For each movement action, the agent takes one step in the said direction. 

### Reward calculation

Each step, the reward is calculated based on the "tile" on which the agent lands after taking an action.

The rewards given for each action are based on the following criteria:
  * 0 - empty tile (one without fire / goal) 
  * 1 - goal
  * -1 - fire 
