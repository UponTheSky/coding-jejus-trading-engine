from typing import final, Final, Any

from engine.utils.logger import get_logger, Logger

from ._interface import TradingEngineServerInterface
from ._config import Config


@final
class TradingEngineServer(TradingEngineServerInterface):
  _logger: Final[Logger]
  _config: Final[Config]

  def __init__(self, *, config: Config):
    self._logger = get_logger(
      classname=self.__class__.__name__,
      environment="development"
    )
    self._config = config

  async def run(self) -> Any:
    return self._execute_async()

  def _execute_async(self) -> Any:

    while True:
      print("hey!")
      break
      ...
