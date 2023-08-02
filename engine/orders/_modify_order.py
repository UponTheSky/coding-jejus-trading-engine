from ._order_core import OrderCore
from ._cancel_order import CancelOrder
from ._order import Order


class ModifyOrder:
  _order_core: OrderCore
  _price: int
  _quantity: int
  _is_buy_side: bool

  def __init__(
    self,
    *,
    order_core: OrderCore,
    modify_price: int,
    modify_quantity: int,
    is_buy_side: bool
  ) -> None:
    self._order_core = order_core
    self._price = modify_price
    self._quantity = modify_quantity
    self._is_buy_side = is_buy_side

  @property
  def price(self) -> int:
    return self._price

  @property
  def quantity(self) -> int:
    return self._quantity

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

  def to_cancel_order(self) -> CancelOrder:
    """
    Remark: whereas in the video all the order classes inherits OrderCore,
    we see no needs for such inheritances, because those classes already has
    self._order_core when they are initailized. Thus, we simply pass self._order_core here.
    """
    return CancelOrder(order_core=self._order_core)

  def to_new_order(self) -> Order:
    """
    Remark: here we won't implement an overloaded constructor of the Order class.
    """
    return Order(
      order_core=self._order_core,
      price=self.price,
      quantity=self.quantity,
      is_buy_side=self.is_buy_side
    )


class ModifyOrderStatus:
  ...
