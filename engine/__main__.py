from typing import Any

from .core import (
  trading_engine_service_provider,
  get_config,
  TradingEngineServerHostBuilder
)

from .logger import LoggingConfig, TextLoggerConfig, LoggerType


text_logger_config = TextLoggerConfig(
  directory="",
  filename="trading_engine_server",
  file_extention=".log"
)

logging_config = LoggingConfig(logger_type=LoggerType.TEXT)


async def app(scope, receive, send) -> None:
  # TODO: refactor this function
  await send({
    "type": "http.response.start",
    "status": 200,
    "headers": [[b"content-type", b"text/plain"]]
  })

  await send({
    "type": "http.response.body",
    "body": b"hey"
  })

  service = trading_engine_service_provider.service_provider
  await service.run()
  return None


if __name__ == "__main__":
  background_engine = TradingEngineServerHostBuilder.build_trading_engine_server(
    app_path="__main__:app",
    config=get_config()
  )
  background_engine.run()
