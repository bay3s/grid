from grid import Grid
import matplotlib.pyplot as plt
import random
import imageio


env = Grid(size = 9, partial = False)
MAX_STEPS = 50

steps = 0
for i in range(20):
  prev_state = env.reset()
  is_done = False

  while not is_done and steps < MAX_STEPS:
    action = random.choice([0, 1, 2, 3])
    state, reward, is_done = env.step(action)
    plt.imshow(state)
    plt.savefig(f'./transitions/{steps}.png')
    steps += 1
    continue

with imageio.get_writer('episodes.gif', mode = 'I') as writer:
  for file_id in range(steps):
    file_name = f'./transitions/{file_id}.png'
    img = imageio.imread(file_name)
    writer.append_data(img)
    continue

pass
