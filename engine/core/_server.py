from typing import final, Final, Any

from engine.logger import TextLoggerInterface

from ._interface import TradingEngineServerInterface
from ._config import Config


@final
class TradingEngineServer(TradingEngineServerInterface):
  _logger: Final[TextLoggerInterface]
  _config: Final[Config]

  def __init__(self, *, config: Config, logger: TextLoggerInterface):
    self._logger = logger
    self._config = config

  async def run(self) -> Any:
    return self._execute_async()

  def _execute_async(self) -> Any:

    while True:
      print("hey!")
      break
      ...
