```python
import time
import cProfile
import pstats
import io
from functools import wraps

def performance_timer(func):
    """
    Decorator to measure the execution time of a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def profile_function(func):
    """
    Decorator to profile a function using cProfile.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return result
    return wrapper

def check_performance(code_string, context_globals=None):
    """
    Function to check the performance of a code snippet.
    :param code_string: str, the code to be executed and analyzed.
    :param context_globals: dict, the global context in which the code will be executed.
    :return: dict, containing performance metrics.
    """
    if context_globals is None:
        context_globals = {}
    local_vars = {}
    exec(code_string, context_globals, local_vars)
    performance_data = {}

    for func_name, func in local_vars.items():
        if callable(func):
            wrapped_func = profile_function(func)
            wrapped_func = performance_timer(wrapped_func)
            performance_data[func_name] = wrapped_func()

    return performance_data
```