from ..utils.logger import get_logger

from ._interface import TradingEngineServerInterface


class TradingEngineServer(TradingEngineServerInterface):
  def __init__(self):
    self._logger = get_logger(
      classname=self.__class__.__name__,
      environment="development"
    )

