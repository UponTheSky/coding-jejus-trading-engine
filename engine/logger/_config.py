from __future__ import annotations

from dataclasses import dataclass

from ._logger_types import LoggerType


class LoggingConfig:
  _logger_type: LoggerType

  def __init__(self, *, logger_type: LoggerType) -> None:
    self._logger_type = logger_type

  @property
  def text_logger_config(self) -> TextLoggerConfig:
    ...


@dataclass
class TextLoggerConfig:
  directory: str
  filename: str
  file_extention: str
