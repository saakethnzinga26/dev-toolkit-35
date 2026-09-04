import sys
from typing import Callable, Any, Dict
from collections import Counter

class AdaptiveCoreDispatcher:
    """
    Dynamically optimizes method lookup overhead by maintaining an
    interned cache of frequently accessed execution paths.
    """
    def __init__(self, target_instance: Any):
        self._target = target_instance
        self._hot_threshold = 5
        self._call_counts: Counter[str] = Counter()
        self._optimized_paths: Dict[str, Callable[..., Any]] = {}

    def execute(self, action_name: str, *args: Any, **kwargs: Any) -> Any:
        # Intern strings to reduce dictionary lookup overhead
        key = sys.intern(action_name)
        
        # Fast path bypasses getattr
        if key in self._optimized_paths:
            return self._optimized_paths[key](*args, **kwargs)

        self._call_counts[key] += 1
        
        target_method = getattr(self._target, key, None)
        if not target_method or not callable(target_method):
            raise AttributeError(f"Executable action '{key}' not found on core")

        # Promote to optimized lookup after frequent hits
        if self._call_counts[key] >= self._hot_threshold:
            self._optimized_paths[key] = target_method
            del self._call_counts[key]

        return target_method(*args, **kwargs)

    def clear_optimization_metrics(self) -> None:
        self._call_counts.clear()
        self._optimized_paths.clear()