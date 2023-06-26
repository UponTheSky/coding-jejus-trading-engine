"""
Remark: currently it is a bit daunting to implement a DI system
from scratch, here we gather all the necessary information to generate main objects
"""
from typing import Any

from ._config import get_config
from ._server import TradingEngineServer
from ._host_builder import TradingEngineServerHostBuilder
from ._service_provider import TradingEngineServiceProvider

trading_engine_service_provider = TradingEngineServiceProvider()
trading_engine_service_provider.service_provider = TradingEngineServer(config=get_config())

__all__ = [
  "get_config",
  "trading_engine_service_provider",
  "TradingEngineServiceHostBuilder"
]
