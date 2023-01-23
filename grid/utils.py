from grid.element import Element
from grid.element_type import ElementType

def generate_element(coordinates: tuple, type: ElementType) -> Element:
  """
  Generate an element given the coordinates and the type.

  :param coordinates:  Tuple containing x, y coordinates for the element.
  :param type: Type of element to generate.

  :return:
  """
  x = coordinates[0]
  y = coordinates[1]

  if type == ElementType.HERO:
    return Element(x, y, 1, 1, 2, None, ElementType.HERO)
  elif type == ElementType.GOAL:
    return Element(x, y, 1, 1, 1, 1, ElementType.GOAL)
  elif type == ElementType.FIRE:
    return Element(x, y, 1, 1, 0, -1, ElementType.FIRE)
  else:
    raise ValueError
