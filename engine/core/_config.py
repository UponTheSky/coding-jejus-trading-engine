from typing import NewType
import os
import functools
from dataclasses import dataclass


@dataclass(frozen=True)
class _Config:
  PORT: int = int(os.getenv("PORT", "8000"))
  LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")


@functools.cache
def get_config() -> _Config:
  return _Config()


Config = NewType("Config", _Config)
