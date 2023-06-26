from ._interface import TradingEngineServerInterface


class TradingEngineServiceProvider:
  _service_provider: TradingEngineServerInterface

  @property
  def service_provider(self) -> TradingEngineServerInterface:
    return self._service_provider

  @service_provider.setter
  def service_provider(self, new_value: TradingEngineServerInterface) -> None:
    self._service_provider = new_value
