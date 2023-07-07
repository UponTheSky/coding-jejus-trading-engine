from abc import ABC, abstractmethod

from ._interface import AbstractLogger
from ._logger_types import LogLevel
from ._config import TextLoggerConfig


class TextLoggerInterface(ABC):
  ...


class TextLogger(TextLoggerInterface, AbstractLogger):
  _logger_config: TextLoggerConfig

  def __init__(self, *, logger_config: TextLoggerConfig) -> None:
    self._logger_config = logger_config

  def _log(self, *, level: LogLevel, module: str, message: str) -> None:
    ...

