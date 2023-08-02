from ._order_core import OrderCore
from ._reject import Rejection, RejectionReason


class RejectCreator:
  @staticmethod
  def generate_order_core_rejection(
    *,
    order_core: OrderCore,
    rejection_reason: RejectionReason
  ) -> Rejection:
    return Rejection(rejected_order=order_core, rejection_reason=rejection_reason)
