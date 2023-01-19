from grid import Grid
import matplotlib.pyplot as plt


env = Grid(size = 9, partial = True)
prev_state = env.reset()
plt.imshow(prev_state)
pass
