from dataclasses import dataclass


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
    name (str):
  """
  x: float
  y: float
  size: int
  intensity: float
  channel: float
  reward: float
  name: str
  pass


