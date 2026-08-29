import functools
from typing import Any, Callable, Dict, List

class CoreModule:
    def __init__(self) -> None:
        self._cache: Dict[str, Any] = {}
        self._access_count: Dict[str, int] = {}

    def _make_key(self, func: Callable, args: tuple, kwargs: Dict) -> str:
        return "{}_{}_{}".format(func.__name__, hash(args), hash(tuple(sorted(kwargs.items()))))

    def optimize(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = self._make_key(func, args, kwargs)
            if key in self._cache:
                self._access_count[key] = self._access_count.get(key, 0) + 1
                return self._cache[key]
            result = func(*args, **kwargs)
            self._cache[key] = result
            self._access_count[key] = 1
            return result
        return wrapper

    def get_cache_stats(self) -> Dict[str, int]:
        return {k: v for k, v in self._access_count.items()}

    def clear_cache(self) -> None:
        self._cache.clear()
        self._access_count.clear()

    def batch_optimize(self, func: Callable, data: List[Any], batch_size: int = 50) -> List[Any]:
        results = []
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]
            results.extend([self.optimize(func)(item) for item in batch])
        return results