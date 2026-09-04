import os
import json
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any], env_prefix: str = "APP_"):
        self._data = defaults
        self._env_prefix = env_prefix

    def load(self, path: str = "config.json") -> None:
        if os.path.exists(path):
            with open(path, "r") as f:
                file_data = json.load(f)
                self._data.update(file_data)
        
        for key in self._data:
            env_key = f"{self._env_prefix}{key.upper()}"
            if env_key in os.environ:
                self._data[key] = os.environ[env_key]

    def __getattr__(self, name: str) -> Any:
        return self._data.get(name)

    def __repr__(self) -> str:
        return f"<ConfigLoader: {list(self._data.keys())}>"

def get_config(defaults: Dict[str, Any]) -> ConfigLoader:
    loader = ConfigLoader(defaults)
    loader.load()
    return loader