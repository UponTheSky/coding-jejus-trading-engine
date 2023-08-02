"""
Remark: currently it is a bit daunting to implement a DI system
from scratch, here we gather all the necessary information to generate main objects
"""
from ._config import get_config
from ._server import TradingEngineServer
from ._host_builder import TradingEngineServerHostBuilder
from ._service_provider import TradingEngineServiceProvider

from ..logger import LoggingConfig, LoggerConfig, LoggingConfig, LoggerType, TextLogger


text_logger_config = LoggerConfig(
  directory="logger_test",
  filename="trading_engine_server",
  file_extention=".txt"
)

logging_config = LoggingConfig(logger_type=LoggerType.TEXT, logger_config=text_logger_config)
logger = TextLogger(logger_config=logging_config)

print(text_logger_config.directory)

trading_engine_service_provider = TradingEngineServiceProvider()
trading_engine_service_provider.service_provider = TradingEngineServer(
  config=get_config(),
  logger=logger
)

__all__ = [
  "get_config",
  "trading_engine_service_provider",
  "TradingEngineServiceHostBuilder"
]
