from enum import Enum


class LoggerType(str, Enum):
  TEXT = "TEXT"
  DATABASE = "DATABASE"
  TRACE = "TRACE"
  CONSOLE = "CONSOLE"


class LogLevel(str, Enum):
  DEBUG = "DEBUG"
  INFO = "INFO"
  WARNING = "WARNING"
  ERROR = "ERROR"
