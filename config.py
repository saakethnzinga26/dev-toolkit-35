import os
import json
from typing import Any, Dict, Optional
class ConfigLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None, config_path: Optional[str] = None, env_prefix: str = 'APP_'):
        self._data = defaults.copy() if defaults else {}
        if config_path:
            self._load_file(config_path)
        self._load_env(env_prefix)
        self._normalize()
    def _load_file(self, path: str):
        try:
            with open(path) as f:
                data = json.load(f)
                self._deep_merge(self._data, data)
        except Exception:
            pass
    def _load_env(self, prefix: str):
        for k, v in os.environ.items():
            if not k.startswith(prefix):
                continue
            key = k[len(prefix):].lower()
            self._data[key] = self._parse_value(v)
    def _parse_value(self, val: str) -> Any:
        if val.lower() == 'true': return True
        if val.lower() == 'false': return False
        try: return int(val)
        except: pass
        try: return float(val)
        except: pass
        return val
    def _deep_merge(self, base: Dict, update: Dict):
        for k, v in update.items():
            if k in base and isinstance(base[k], dict) and isinstance(v, dict):
                self._deep_merge(base[k], v)
            else:
                base[k] = v
    def _normalize(self):
        self._data = {k.lower(): v for k, v in self._data.items()}
    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key.lower(), default)
    def __getattr__(self, item: str) -> Any:
        if item in self._data:
            return self._data[item]
        raise AttributeError(item)
    def set(self, key: str, value: Any):
        self._data[key.lower()] = value
    def to_dict(self) -> Dict[str, Any]:
        return self._data.copy()
    def reload(self, defaults: Optional[Dict] = None, path: Optional[str] = None):
        if defaults:
            self._data = defaults.copy()
        if path:
            self._load_file(path)
        self._normalize()