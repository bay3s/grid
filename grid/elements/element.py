from dataclasses import dataclass
from .element_type import ElementType


@dataclass
class Element:
  """
  Dataclass for observations made in the environment by the agent navigating it.

  Args:
    x (float): X-coordinate of the current observation.
    y (float): Y-coordinate of the current observation.
    size (int): Size of the
    intensity (float):
    channel (float):
    reward (float):
    type (ElementType):
  """
  x: float
  y: float
  size: int
  intensity: float
  channel: float
  reward: float
  type: ElementType
  pass


