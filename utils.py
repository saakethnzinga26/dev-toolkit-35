from typing import Any, Dict, List, Union

import copy

def flatten_nested_dict(data: Dict[str, Any], prefix: str = '') -> Dict[str, Any]:
    """Flatten nested dictionary using stack based iteration."""
    result: Dict[str, Any] = {}
    stack: List[tuple] = [(data, prefix)]
    while stack:
        current, path = stack.pop()
        for key, value in current.items():
            new_path = f"{path}.{key}" if path else key
            if isinstance(value, dict):
                stack.append((value, new_path))
            else:
                result[new_path] = value
    return result

def merge_data(*data_sources: Dict[str, Any]) -> Dict[str, Any]:
    """Merge dicts with deep merge using stack for nested keys."""
    if not data_sources:
        return {}
    merged = copy.deepcopy(data_sources[0])
    for source in data_sources[1:]:
        stack = [(merged, source)]
        while stack:
            target, src = stack.pop()
            for k, v in src.items():
                if k in target and isinstance(target[k], dict) and isinstance(v, dict):
                    stack.append((target[k], v))
                else:
                    target[k] = copy.deepcopy(v)
    return merged

def handle_general_data(data: Any, mode: str = 'flatten') -> Any:
    """General data handling utility supporting multiple modes."""
    if mode == 'flatten' and isinstance(data, dict):
        return flatten_nested_dict(data)
    elif mode == 'merge' and isinstance(data, (list, tuple)):
        return merge_data(*[d for d in data if isinstance(d, dict)])
    elif mode == 'normalize':
        if isinstance(data, dict):
            return {k: handle_general_data(v, 'normalize') for k, v in data.items()}
        elif isinstance(data, list):
            return [handle_general_data(item, 'normalize') for item in data]
        else:
            return data
    return data
