from typing import Optional, Any
from abc import ABC, abstractmethod, abstractproperty


class OrderCoreInterface:
  _order_id: int
  _username: str
  _security_id: int

  def __init__(self, *, order_id: int, username: str, security_id: int) -> None:
    self._order_id = order_id
    self._username = username
    self._security_id = security_id

  @property
  def order_id(self) -> int:
    return self._order_id

  @property
  def username(self) -> str:
    return self._username

  @property
  def security_id(self) -> int:
    return self._security_id


class OrderBookSpread:
  _bid: int
  _ask: int

  def __init__(self, *, bid: Optional[int] = None, ask: Optional[int] = None) -> None:
    self._bid = bid
    self._ask = ask

  @property
  def bid(self) -> Optional[int]:
    return self._bid

  @property
  def ask(self) -> Optional[int]:
    return self._ask

  def spread(self) -> Optional[int]:
    if self.bid and self.ask:
      return self.ask - self.bid

    return None


class ReadOnlyOrderBookInterface(ABC):
  @abstractmethod
  def contains_order(self, order_id: int) -> bool:
    ...

  @abstractmethod
  def get_spread(self) -> OrderBookSpread:
    ...

  @abstractproperty
  def count(self) -> int:
    ...

class OrderEntryOrderBookInterface(ReadOnlyOrderBookInterface, ABC):
  @abstractmethod
  def add_order(self, order: Any) -> None:
    ...

  @abstractmethod
  def change_order(self, modify_order: Any) -> None:
    ...

  @abstractmethod
  def remove_order(self, cancel_order: Any) -> None:
    ...


class RetrievalOrderBookInterface(OrderEntryOrderBookInterface, ABC):
  @abstractmethod
  def get_ask_orders(self) -> list[Any]:
    ...

  @abstractmethod
  def get_bid_orders(self) -> list[Any]:
    ...


class MatchResult:
  ...


class MatchingOrderInterface(RetrievalOrderBookInterface, ABC):
  @abstractmethod
  def match(self) -> MatchResult:
    ...
