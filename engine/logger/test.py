from typing import ClassVar

class Singleton:
  _is_instantiated: ClassVar[bool] = False

  def __init__(self):
    if self._is_instantiated:
      raise RuntimeError("A singleton instance is already generated")

    self.__class__._is_instantiated = True
    print("singleton generated!")

t = Singleton()
s = Singleton()
