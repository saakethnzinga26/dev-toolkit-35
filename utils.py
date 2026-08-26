import sys
import functools
import traceback

class DevToolkitError(Exception):
    pass

def resilient_execution(default_return=None, log_errors=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (TypeError, ValueError, ZeroDivisionError) as e:
                if log_errors:
                    sys.stderr.write(f"⚠ [EdgeCase] {func.__name__}: {type(e).__name__} -> {e}\n")
                return default_return
            except Exception as e:
                tb = traceback.format_exc()
                raise DevToolkitError(f"Critical failure in {func.__name__}: {e}\n{tb}") from e
        return wrapper
    return decorator

@resilient_execution(default_return=0)
def parse_numeric_safely(val):
    if val is None:
        raise ValueError("Value cannot be None")
    if isinstance(val, str) and not val.strip():
        return 0
    return float(val)

@resilient_execution(default_return="")
def extract_nested_key(data, keys):
    for key in keys:
        data = data[key]
    return str(data)
