from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
import itertools
import scipy.misc
from .elements import ElementCollection, Element, ElementType, generate_element


@dataclass
class Grid:
  """
  Dataclass for observations made in the environment by the agent navigating it.

  Args:
    size (int): Size of the Grid
    actions (int): Number of actions
    elements (list): Objects in the Grid
    partial (bool): Whether to display the partial grid.
    state (np.ndarray): Current state of the environment.
  """
  size: int
  actions: int
  elements: ElementCollection
  partial: bool
  state: np.ndarray

  def __post_init__(self):
    a = self.reset()
    plt.imshow(a, interpolation = 'nearest')
    pass

  def _new_position(self) -> [int , int]:
    """
    Returns a new viable position given the position of other elements on the grid.

    :return: [int, int]
    """
    iterables = [range(self.size), range(self.size)]
    points = []

    for t in itertools.product(*iterables):
      points.append(t)

    current_positions = []
    for obj in self.elements:
      if (obj.x, obj.y) not in current_positions:
        current_positions.append((obj.x, obj.y))

    for pos in current_positions:
      points.remove(pos)

    location = np.random.choice(range(len(points)), replace = False)

    return points[location]

  def reset(self) -> np.ndarray:
    """
    Reset the environment and return its current state.

    :return: np.ndarray
    """
    self.elements = ElementCollection()

    self.elements.append(generate_element(self._new_position(), ElementType.HERO))
    self.elements.append(generate_element(self._new_position(), ElementType.GOAL))
    self.elements.append(generate_element(self._new_position(), ElementType.FIRE))
    self.elements.append(generate_element(self._new_position(), ElementType.GOAL))
    self.elements.append(generate_element(self._new_position(), ElementType.FIRE))
    self.elements.append(generate_element(self._new_position(), ElementType.GOAL))
    self.elements.append(generate_element(self._new_position(), ElementType.GOAL))

    self.state = self.render()

    return self.state

  def move_character(self, direction: int) -> None:
    """
    Given a direction to move in, move the hero in that direciton.

    :param direction: The direction in which to move the hero.

    :return: None
    """
    hero = self.elements[0]

    if direction == 0 and hero.y >= 1:
      hero.y -= 1

    if direction == 1 and hero.y <= self.size - 2:
      hero.y += 1

    if direction == 2 and hero.x >= 1:
      hero.x -= 1

    if direction == 3 and hero.x <= self.size - 2:
      hero.x += 1

    self.elements[0] = hero
    pass

  def check_goal(self) -> [float, bool]:
    others = list()

    for obj in self.elements:
      if obj.name == ElementType.HERO:
        hero = obj
      else:
        others.append(obj)

    for other in others:
      if hero.x != other.x or hero.y != other.y:
        continue

      self.elements.remove(other)
      if other.reward == 1:
        self.elements.append(generate_element(self._new_position(), ElementType.GOAL))
      else:
        self.elements.append(generate_element(self._new_position(), ElementType.FIRE))

      return other.reward, False

    return 0.0, False

  def render(self) -> np.ndarray:
    """
    Render the grid and return its current state.

    :return: np.ndarray
    """
    dim_a = self.size + 2
    a = np.ones([dim_a, dim_a])

    a[1:-1, 1:-1, :] = 0
    hero = None

    for item in self.elements:
      a[item.y + 1:item.y + item.size + 1, item.x + 1:item.x + item.size + 1, item.channel] = item.intensity

      if item.name == ElementType.HERO:
        hero = item

    if self.partial:
      a = a[hero.y:hero.y + 3, hero.x:hero.x + 3, :]

    b = scipy.misc.imresize(a[:, :, 0], [84, 84, 1], interp = 'nearest')
    c = scipy.misc.imresize(a[:, :, 1], [84, 84, 1], interp = 'nearest')
    d = scipy.misc.imresize(a[:, :, 2], [84, 84, 1], interp = 'nearest')
    a = np.stack([b, c, d], axis = 2)

    return a

  def step(self, direction: int) -> [np.ndarray, float, bool]:
    """
    Take a single step in the environment.

    :param direction: The action to take in the current state of the environment.

    :return: [np.ndarray, float, bool]
    """
    self.move_character(direction)
    reward, is_done = self.check_goal()

    state = self.render()

    if reward is None:
      print(is_done, reward, state)
      return state, reward, is_done
    else:
      return state, reward, is_done
