import collections
from grid.element import Element


class ElementCollection(collections.MutableSequence):

  def __init__(self):
    """
    Initialize the collection.
    """
    self.list = list()
    pass

  def __len__(self) -> int:
    """
    Return the length of the collection.

    :return: int
    """
    return len(self.list)

  def __getitem__(self, i: int):
    """
    Returns an element at a specific position in the

    :param i: Given an index, returns the item at that specified index.

    :return: Element
    """
    return self.list[i]

  def __delitem__(self, i: int):
    """
    Deletes an element from the specified index.

    :param i: Index of the item to be deleted.

    :return: None
    """
    del self.list[i]

  def __setitem__(self, i: int, v: object) -> None:
    """
    Given an index, sets the item in that index.

    :param i: Index for which to set the item.
    :param v: Element to set for the index.

    :return: None
    """
    if not isinstance(v, Element):
      raise TypeError(f'Invalid element found.')

    self.list[i] = v

  def insert(self, i: int, v: object):
    """
    Given an index, inserts the item in that index.

    :param i: Index for which to set the item.
    :param v: Element to set for the index.

    :return: None
    """
    if not isinstance(v, Element):
      raise TypeError(f'Invalid element found.')

    self.list.insert(i, v)

  def __str__(self) -> str:
    """
    Converts the collection to a string.

    :return: str
    """
    return str(self.list)
