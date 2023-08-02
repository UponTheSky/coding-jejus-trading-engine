from typing import final, Final, Any

from ._interface import TradingEngineServerInterface
from ..logger._interface import AbstractLogger
from ._config import Config


@final
class TradingEngineServer(TradingEngineServerInterface):
  _logger: Final[AbstractLogger]
  _config: Final[Config]

  def __init__(self, *, config: Config, logger: AbstractLogger):
    self._logger = logger
    self._config = config

  async def run(self) -> Any:
    self._execute_tasks()

  def _execute_tasks(self) -> Any:
    self._logger.info(module=__file__, content="Starting Trading Engine")
    logger_thread_event = self._logger.event

    while not logger_thread_event.is_set():
      print("hey!")
      break
      ...

    self._logger.info(module=__file__, content="Stopping Trading Engine")
