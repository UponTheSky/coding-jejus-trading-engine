from dataclasses import dataclass
from datetime import datetime

from ._logger_types import LogLevel

@dataclass(frozen=True)
class LogInformation:
  log_level: LogLevel
  module: str
  message: str
  now: datetime
  thread_id: int
  thread_name: str
