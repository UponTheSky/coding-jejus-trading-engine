from typing import Literal
import logging


def get_logger(
  *,
  classname: str,
  environment: Literal["development", "production"]
) -> logging.Logger:
  logger = logging.getLogger(name=classname)
  logger.setLevel(logging.INFO if environment == "production" else logging.DEBUG)
  return logger
