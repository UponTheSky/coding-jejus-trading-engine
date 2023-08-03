from typing import Mapping
from sortedcontainers import SortedSet

from ._interface import RetrievalOrderBookInterface, OrderBookSpread
from ._order_book_entry import OrderBookEntry, bid_limit_comparer, ask_limit_comparer, Limit
from ._order import Order
from ._modify_order import ModifyOrder
from ._cancel_order import CancelOrder


class Security:
  ...


class OrderBook(RetrievalOrderBookInterface):
  _instrument: Security
  _orders: dict[int, OrderBookEntry]
  _ask_limits: SortedSet
  _bid_limits: SortedSet

  def __init__(self, *, instrument: Security) -> None:
    self._instrument = instrument
    self._orders = {}
    self._ask_limits = SortedSet([], key=ask_limit_comparer)
    self._bid_limits = set([], key=bid_limit_comparer)

  def count(self) -> int:
    return len(self._orders)

  def contains_order(self, order_id: int) -> bool:
    return order_id in self._orders

  def add_order(self, order: Order) -> None:
    base_limit = Limit(order.price)
    self._add_order(
      order=order,
      base_limit=base_limit,
      limit_levels=self._bid_limits if order.is_buy_side else self._ask_limits,
      internal_book=self._orders
    )

  @staticmethod
  def _add_order(
    *,
    order: Order,
    base_limit: Limit,
    limit_levels: SortedSet,
    internal_book: Mapping[int, OrderBookEntry]
  ) -> None:
    order_book_entry = OrderBookEntry(current_order=order, parent_limit=base_limit)

    if base_limit in limit_levels:
      if not base_limit.head:
        base_limit.head = base_limit.tail = order_book_entry

      else:
        tail_prev = base_limit.tail.previous

        tail_prev.next = order_book_entry
        order_book_entry.previous = tail_prev

        order_book_entry.next = base_limit.tail
        base_limit.tail.previous = order_book_entry

    else:
      limit_levels.add(base_limit)
      base_limit.head = base_limit.tail = order_book_entry

      internal_book[order.order_id] = OrderBookEntry

  def change_order(self, modify_order: ModifyOrder) -> None:
    if modify_order.order_id in self._orders:
      self.remove_order(modify_order.to_cancel_order())
      self._add_order(
        order=modify_order.to_new_order(),
        base_limit=self._orders[modify_order.order_id].parent_limit,
        limit_levels=self._bid_limits if modify_order.is_buy_side else self._ask_limits,
        internal_book=self._orders
      )

  def remove_order(self, cancel_order: CancelOrder) -> None:
    if cancel_order.order_id in self._orders:
      order_book_entry = self._orders[cancel_order.order_id]
      self._remove_order(order=cancel_order, order_book_entry=order_book_entry, internal_book=self._orders)

  @staticmethod
  def _remove_order(
    *,
    cancel_order: CancelOrder,
    order_book_entry: OrderBookEntry,
    internal_book: Mapping[int, OrderBookEntry]
  ) -> None:
    obe_prev, obe_next = order_book_entry.previous, order_book_entry.next
    obe_prev.next = obe_next
    obe_next.previous = obe_prev

    del internal_book[cancel_order.order_id]

  def get_spread(self) -> OrderBookSpread:
    best_ask = best_bid = None

    if self._ask_limits.count() != 0:
      best_ask = self._ask_limits[0]

    if self._bid_limits.count() != 0:
      best_bid = self._bid_limits[-1]

    return OrderBookSpread(bid=best_bid, ask=best_ask)

  def get_ask_orders(self) -> list[OrderBookEntry]:
    order_book_entries = []

    for limit in self._ask_limits:
      if self._ask_limits.count() > 0:
        curr = limit.head
        while curr:
          order_book_entries.append(curr)
          curr = curr.next

    return order_book_entries

  def get_bid_orders(self) -> list[OrderBookEntry]:
    order_book_entries = []

    for limit in self._bid_limits:
      if self._bid_limits.count() > 0:
        curr = limit.head
        while curr:
          order_book_entries.append(curr)
          curr = curr.next

    return order_book_entries
