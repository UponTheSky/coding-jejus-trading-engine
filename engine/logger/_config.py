from __future__ import annotations

from dataclasses import dataclass

from ._logger_types import LoggerType


class LoggingConfig:
  _logger_type: LoggerType
  _logger_config: LoggerConfig

  def __init__(self, *, logger_type: LoggerType, logger_config: LoggerConfig) -> None:
    self._logger_type = logger_type
    self._logger_config = logger_config

  @property
  def logger_type(self) -> LoggerType:
    return self._logger_type

  @property
  def text_logger_config(self) -> LoggerConfig:
    return self._logger_config

@dataclass
class LoggerConfig:
  directory: str
  filename: str
  file_extention: str
