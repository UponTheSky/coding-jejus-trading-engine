from distutils.file_util import write_file
from queue import Queue
import threading
from datetime import datetime
import os

from ._interface import AbstractLogger
from ._logger_types import LogLevel, LoggerType
from ._config import LoggingConfig
from ._log_info import LogInformation

class TextLogger(AbstractLogger):
  _logger_config: LoggingConfig
  _log_queue: Queue
  _event: threading.Event

  def __init__(self, *, logger_config: LoggingConfig) -> None:
    if logger_config.logger_type != LoggerType.TEXT:
      raise AttributeError("The given logger config object is not for a text logger")

    self._logger_config = logger_config.text_logger_config
    self._log_queue = Queue()
    self._event = threading.Event()

    # run the logging process
    log_dir = f"{self._logger_config.directory}/{datetime.now().strftime('%Y-%m-%d')}"
    base_log_name = f"{self._logger_config.filename}-{datetime.now().strftime('%H:%M:%S')}{self._logger_config.file_extention}"
    try:
      os.makedirs(log_dir)

    except FileExistsError:
      ...

    def worker() -> None:
      self._log_sync(
        filepath=f"{log_dir}/{base_log_name}",
        log_queue=self._log_queue,
        event=self._event
      )

    threading.Thread(target=worker, daemon=True).start()

  def _log(self, *, level: LogLevel, module: str, message: str) -> None:
    current_thread = threading.current_thread()
    self._log_queue.put(LogInformation(
      level,
      module,
      message,
      datetime.now(),
      current_thread.native_id,
      current_thread.getName()
    ))

  @property
  def event(self) -> threading.Event:
    return self._event

  @staticmethod
  def _log_sync(*, filepath: str, log_queue: Queue, event: threading.Event) -> None:
    """
    Remark: compared to what Coding Jesus implemented, this function is NOT async.
    This is because Python doesn't have thread-safe asynchronous queue APIs.
    But still, this synchronous process suits our needs, so we simply implement it as a synchronous one.

    Reference: https://docs.python.org/3/library/queue.html#module-queue
    """
    with open(filepath, "w") as write_filestream:
      while not event.is_set():
        try:
          log_item = log_queue.get(block=True, timeout=300)
          write_filestream.write(TextLogger._format_log_item(log_item=log_item))
          write_filestream.flush()
          log_queue.task_done()

        except:
          break

      log_queue.join()

  @staticmethod
  def _format_log_item(*, log_item: LogInformation) -> str:
    return (
      f"[{log_item.now.strftime('%Y-%m-%d %H:%M:%S.%f')}] [{log_item.thread_name}:{log_item.thread_id:03d}]"
      + f"[{log_item.log_level}] {log_item.message}"
    )


  def _dispose() -> None:
    """
    Skip this implementation because there is no corresponding APIs in Python
    """
    ...
