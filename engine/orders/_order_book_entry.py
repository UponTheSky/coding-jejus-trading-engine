from __future__ import annotations

from typing import Optional
from datetime import datetime, timezone
from enum import Enum
from dataclasses import dataclass

from ._order import Order
from ._order_core import OrderCore


class Side(Enum):
  UNKNOWN = 0
  BID = 1
  ASK = 2


@dataclass(frozen=False)
class OrderRecord:
  order_id: int
  quantity: int
  price: int
  is_buy_side: bool
  username: str
  security_id: int
  theoretical_queue_position: int


def _make_dummy_order_book_entry() -> OrderBookEntry:
  return OrderBookEntry(Order(OrderCore(order_id=0, username="", security_id=0)))


class Limit:
  price: int
  head: OrderBookEntry
  tail: OrderBookEntry
  _side: Side

  def __init__(self) -> None:
    self.head = _make_dummy_order_book_entry()
    self.tail = _make_dummy_order_book_entry()
    self._side = Side.UNKNOWN

    self.head.next = self.tail
    self.tail.previous = self.head

  def is_empty(self) -> bool:
    return self.head.next == self.tail

  @property
  def side(self) -> Side:
    if self.is_empty():
      return Side.UNKNOWN

    return Side.BID if self.head.next.current_order.is_buy_side else Side.ASK

  def get_level_order_count(self) -> int:
    order_count = 0
    curr = self.head.next
    while curr:
      if curr.current_order.current_quantity != 0:
        order_count += 1

      curr = curr.next

    return order_count

  def get_level_order_quantity(self) -> int:
    order_quantity = 0
    curr = self.head.next
    while curr:
      order_quantity += curr.current_order.current_quantity
      curr = curr.next

    return order_quantity

  def get_level_order_records(self) -> list[OrderRecord]:
    order_records = []
    curr = self.head.next
    theoretical_queue_position = 0

    while curr:
      curr_order = curr.current_order
      if curr_order.current_quantity != 0:
        order_records.append(OrderRecord(
          order_id=curr_order.order_id,
          quantity=curr_order.current_quantity,
          price=curr_order.price,
          is_buy_side=curr_order.is_buy_side,
          username=curr_order.username,
          security_id=curr_order.security_id,
          theoretical_queue_position=theoretical_queue_position
        ))

      theoretical_queue_position += 1
      curr = curr.next

    return order_records


def limit_comparer(x: Limit, y: Limit, is_bid: bool = True) -> int:
  ret = 0

  if x.price < y.price:
    ret = 1

  elif x.price > y.price:
    ret = -1

  if not is_bid:
    ret *= -1

  return ret


class OrderBookEntry:
  _creation_time: datetime
  _current_order: Order
  _parent_limit: Limit
  _previous: Optional[OrderBookEntry]
  _next: Optional[OrderBookEntry]

  def __init__(self, *, current_order: Order, parent_limit: Limit) -> None:
    self._creation_time = datetime.now(timezone.utc)
    self._parent_limit = parent_limit
    self._current_order = current_order
    self._previous = self._next = None


  @property
  def creation_time(self) -> datetime:
    return self._creation_time

  @property
  def current_order(self) -> Order:
    return self._current_order

  @property
  def parent_limit(self) -> Limit:
    return self._parent_limit

  @property
  def previous(self) -> OrderBookEntry:
    return self._previous

  @property
  def next(self) -> OrderBookEntry:
    return self._next
