from enum import Enum

from ._order_core import OrderCore


class RejectionReason(str, Enum):
  UNKNOWN = 0
  ORDER_NOT_FOUND = 1
  INSTRUMENT_NOT_FOUND = 2
  ATTEMPTING_TO_MODIFY_WRONG_SIDE = 3


class Rejection:
  _order_core: OrderCore
  _rejection_reason: RejectionReason

  def __init__(self, *, rejected_order: OrderCore, rejection_reason: RejectionReason) -> None:
    self._order_core = rejected_order

  @property
  def order_id(self) -> int:
    return self._order_core.order_id

  @property
  def username(self) -> str:
    return self._order_core.username

  @property
  def security_id(self) -> int:
    return self._order_core.security_id

  @property
  def rejection_reason(self) -> RejectionReason:
    return self._rejection_reason
