from ._order_core import OrderCore


class CancelOrder:
  _order_core: OrderCore

  def __init__(self, *, order_core: OrderCore) -> None:
    self._order_core = order_core

  @property
  def order_id(self) -> int:
    return self._order_core.order_id

  @property
  def username(self) -> str:
    return self._order_core.username

  @property
  def security_id(self) -> int:
    return self._order_core.security_id


class CancelOrderStatus:
  ...
