from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
import itertools

from grid.element_collection import ElementCollection
from grid.element_type import ElementType
from grid.utils import generate_element
from PIL import Image

@dataclass
class Grid:

  MOVE_DIRECTION_UP = 0
  MOVE_DIRECTION_DOWN = 1
  MOVE_DIRECTION_LEFT = 2
  MOVE_DIRECTION_RIGHT = 3

  """
  Dataclass for observations made in the environment by the agent navigating it.

  Args:
    size (int): Size of the Grid
    partial (bool): Whether to display the partial grid.
    actions (int): Number of actions
    elements (list): Objects in the Grid
    state (np.ndarray): Current state of the environment.
  """
  size: int
  partial: bool
  actions: int = 4
  elements: ElementCollection = ElementCollection()
  state: np.ndarray = None

  def __post_init__(self):
    a = self.reset()
    plt.imshow(a, interpolation = 'nearest')
    pass

  @property
  def action_space(self) -> np.array:
    """
    Returns an array containing a possible actions in the action space of this environment.

    Returns:
      np.ndarray
    """
    return np.array([
      self.MOVE_DIRECTION_UP,
      self.MOVE_DIRECTION_DOWN,
      self.MOVE_DIRECTION_LEFT,
      self.MOVE_DIRECTION_RIGHT
    ])

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

  def _move_character(self, direction: int) -> None:
    """
    Given a direction to move in, move the hero in that direciton.

    :param direction: The direction in which to move the hero.

    :return: None
    """
    hero = self.elements[0]

    if direction == self.MOVE_DIRECTION_UP and hero.y >= 1:
      hero.y -= 1
    elif direction == self.MOVE_DIRECTION_DOWN and hero.y <= self.size - 2:
      hero.y += 1
    elif direction == self.MOVE_DIRECTION_LEFT and hero.x >= 1:
      hero.x -= 1
    elif direction == self.MOVE_DIRECTION_RIGHT and hero.x <= self.size - 2:
      hero.x += 1

    self.elements[0] = hero
    pass

  def check_goal(self) -> [float, bool]:
    other_elements = list() # these can only be goals or fire

    for obj in self.elements:
      if obj.type == ElementType.HERO:
        hero = obj
      else:
        other_elements.append(obj)

    for other in other_elements:
      # check for element in the current position
      if hero.x != other.x or hero.y != other.y:
        continue

      self.elements.remove(other)
      if other.reward == 1:
        self.elements.append(generate_element(self._new_position(), ElementType.GOAL))
      elif other.reward == -1:
        self.elements.append(generate_element(self._new_position(), ElementType.FIRE))
      else:
        raise ValueError

      return other.reward, True

    return 0.0, False

  def render(self) -> np.ndarray:
    """
    Render the grid and return its current state.

    :return: np.ndarray
    """
    dim_a = self.size + 2
    a = np.ones([dim_a, dim_a, 3])

    a[1:-1, 1:-1, :] = 0
    hero = None

    for item in self.elements:
      a[item.y + 1:item.y + item.size + 1, item.x + 1:item.x + item.size + 1, item.channel] = item.intensity

      if item.type == ElementType.HERO:
        hero = item

    if self.partial:
      a = a[hero.y:hero.y + 3, hero.x:hero.x + 3, :]

    b = np.array(Image.fromarray(a[:, :, 0]).resize((84, 84), resample = Image.NEAREST))
    c = np.array(Image.fromarray(a[:, :, 1]).resize((84, 84), resample = Image.NEAREST))
    d = np.array(Image.fromarray(a[:, :, 2]).resize((84, 84), resample = Image.NEAREST))
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
      return state, reward, is_done

    return state, reward, is_done
