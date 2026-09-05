import os
from pathlib import Path
from typing import Final, Dict, Any

# Project root definition with fallback safety
ROOT_PATH: Final[Path] = Path(__file__).resolve().parent.parent

# Environment mapping via dictionary comprehension for runtime injection
ENV_VARS: Final[Dict[str, str]] = {
    key: os.getenv(key, default) 
    for key, default in {
        "APP_MODE": "production",
        "LOG_LEVEL": "INFO",
        "TIMEOUT": "30",
        "MAX_RETRIES": "3"
    }.items()
}

# System capacity constraints with bitwise scaling
BUFFER_SIZE: Final[int] = 1024 * 8
MAX_CONCURRENT_TASKS: Final[int] = 256

# Magic string registry for cross-module consistency
KEYS: Final[Dict[str, str]] = {
    "AUTH": "x-dev-toolkit-token",
    "TRACE": "x-request-id",
    "STATUS": "active"
}

# Format strings for log output standardization
LOG_FORMAT: Final[str] = "[%(asctime)s] %(levelname)s | %(name)s : %(message)s"

def get_env(key: str, default: Any = None) -> Any:
    return ENV_VARS.get(key, default)

# Sentinel values for state checking
SHUTDOWN_SIGNAL: Final[str] = "SIGTERM_RECEIVED"
INITIALIZED_FLAG: Final[bool] = True