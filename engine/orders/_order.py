from ._order_core import OrderCore


class Order:
  _order_core: OrderCore
  _price: int
  _initial_quantity: int
  _current_quantity: int
  _is_buy_side: bool

  def __init__(
    self,
    *,
    order_core: OrderCore,
    price: int,
    quantity: int,
    is_buy_side: bool
  ) -> None:
    self._order_core = order_core
    self._price = price
    self._initial_quantity = self.current_quantity = quantity
    self._is_buy_side = is_buy_side

  @property
  def price(self) -> int:
    return self._price

  @property
  def initial_quantity(self) -> int:
    return self._initial_quantity

  @property
  def current_quantity(self) -> int:
    return self._current_quantity

  @property
  def is_buy_side(self) -> bool:
    return self._is_buy_side

  @property
  def order_id(self) -> int:
    return self._order_core.order_id

  @property
  def username(self) -> str:
    return self._order_core.username

  @property
  def security_id(self) -> int:
    return self._order_core.security_id

  def increase_quantity(self, delta: int) -> None:
    self._current_quantity += delta

  def decrease_quantity(self, delta: int) -> None:
    """
    Remark: in the video <delta> is an unsigned integer which has a possible overflow problem.

    However, here Python doesn't have such a problem so we would like to ignore that case.
    """
    self.increase_quantity(-delta)


class OrderStatus:
  ...
