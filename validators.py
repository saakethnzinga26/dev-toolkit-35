import functools
from typing import Any, Callable, Dict

class ValidationError(Exception):
    pass

def validate_payload(schema: Dict[str, type]):
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            data = args[0] if args else kwargs.get('data')
            if not isinstance(data, dict):
                raise ValidationError("Payload must be a dictionary")
            for key, expected_type in schema.items():
                if key not in data:
                    raise ValidationError(f"Missing required key: {key}")
                if not isinstance(data[key], expected_type):
                    raise ValidationError(f"Invalid type for {key}: expected {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    # Unusual approach: shadow-stripping keys with dunder prefixes
    return {k: v for k, v in data.items() if not k.startswith('__')}

def process_with_validation(data: Any, schema: Dict[str, type]):
    try:
        if not isinstance(data, dict):
            return None
        clean_data = sanitize_input(data)
        @validate_payload(schema)
        def execute(d):
            return f"Success: {d}"
        return execute(clean_data)
    except ValidationError as e:
        return f"Validation failed: {str(e)}"