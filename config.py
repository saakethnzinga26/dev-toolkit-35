import os
from typing import Any, Dict

class ChameleonConfig:
    def __init__(self, defaults: Dict[str, Any]) -> None:
        self._store = dict(defaults)
        self._absorb_environment()

    def _absorb_environment(self) -> None:
        for key in self._store:
            env_key = f"TOOLKIT_{key.upper()}"
            if env_key in os.environ:
                raw_val = os.environ[env_key]
                self._store[key] = self._cast(self._store[key], raw_val)

    @staticmethod
    def _cast(original: Any, incoming: str) -> Any:
        if isinstance(original, bool):
            return incoming.lower() in ('true', '1', 'yes', 'on')
        if isinstance(original, int):
            return int(incoming)
        if isinstance(original, float):
            return float(incoming)
        return incoming

    def __getattr__(self, item: str) -> Any:
        if item in self._store:
            return self._store[item]
        raise AttributeError(f"Config missing key: {item}")

    def __getitem__(self, item: str) -> Any:
        return self.__getattr__(item)

    def snapshot(self) -> Dict[str, Any]:
        return dict(self._store)

def load_config(defaults: Dict[str, Any]) -> ChameleonConfig:
    return ChameleonConfig(defaults)
