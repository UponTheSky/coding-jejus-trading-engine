from ._cancel_order import CancelOrder, CancelOrderStatus
from ._order import Order, NewOrderStatus
from ._modify_order import ModifyOrder, ModifyOrderStatus

class OrderStatusCreator:
  @staticmethod
  def generate_cancel_order_status(
    *,
    cancel_order: CancelOrder
  ) -> CancelOrderStatus:
    return CancelOrderStatus()

  @staticmethod
  def generate_new_order_status(*, order: Order) -> NewOrderStatus:
    return NewOrderStatus()


  @staticmethod
  def generate_modify_order_status(*, modify_order: ModifyOrder) -> ModifyOrderStatus:
    return NewOrderStatus()
