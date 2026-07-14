def log_action(func):
    """A Decorator that logs when a method i scalled and finished,"""

    def wrapper(*args,**kwargs):
        print(f"[LOG]Calling {func.__name__}...")
        result =func(*args,**kwargs)
        print(f"[LOG] finished {func.__name__}")
        return result
    return wrapper