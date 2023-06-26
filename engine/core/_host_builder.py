from typing import final

import uvicorn

from ._config import Config


@final
class TradingEngineServerHostBuilder:
  @classmethod
  def build_trading_engine_server(
    cls,
    *,
    app_path: str = "main:app",
    config: Config
  ) -> uvicorn.Server:
    """
    Remark: why we stick to str for app_path:
    see https://www.uvicorn.org/deployment/#running-programmatically
    """
    uvicorn_config = uvicorn.Config(
      app_path,
      port=config.PORT,
      log_level=config.LOG_LEVEL
    )
    return uvicorn.Server(config=uvicorn_config)
