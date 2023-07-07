from typing import Union
from abc import ABC, abstractmethod
import traceback

from ._logger_types import LogLevel


class LoggerInterface(ABC):
  @abstractmethod
  def debug(self, *, module: str, content: Union[str, Exception]) -> None:
    ...

  @abstractmethod
  def info(self, *, module: str, content: Union[str, Exception]) -> None:
    ...

  @abstractmethod
  def warning(self, *, module: str, content: Union[str, Exception]) -> None:
     ...

  @abstractmethod
  def error(self, *, module: str, content: Union[str, Exception]) -> None:
    ...

class AbstractLogger(LoggerInterface, ABC):
  def debug(self, *, module: str, content: Union[str, Exception]) -> None:
    self._log(
      level=LogLevel.DEBUG,
      module=module,
      message=self._get_content_string(content=content)
    )

  def info(self, *, module, content) -> None:
    self._log(
      level=LogLevel.INFO,
      module=module,
      message=self._get_content_string(content=content)
    )

  def warning(self, *, module, content) -> None:
    self._log(
      level=LogLevel.WARNING,
      module=module,
      message=self._get_content_string(content=content)
    )

  def error(self, *, module, content) -> None:
    self._log(
      level=LogLevel.ERROR,
      module=module,
      message=self._get_content_string(content=content)
    )

  @abstractmethod
  def _log(self, *, level: LogLevel, module: str, message: str) -> None:
    ...

  @staticmethod
  def _get_content_string(*, content: Union[str, Exception]) -> str:
    if isinstance(content, str):
      return content

    if isinstance(content, Exception):
      return traceback.extract_tb(content.__traceback__).format()

    raise TypeError("The content argument should be either a string or an exception")
