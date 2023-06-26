from typing import Any
from abc import ABC, abstractmethod


class TradingEngineServerInterface(ABC):
  @abstractmethod
  async def run(self) -> Any:
    ...
