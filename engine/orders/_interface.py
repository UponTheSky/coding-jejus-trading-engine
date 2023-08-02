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
