import functools
from datetime import datetime


def timer(func):
    @functools.wraps(func)
    def wrapper_time(*args, **kwargs):
        start_time = datetime.now()
        value = func(*args, **kwargs)
        end_time = datetime.now()
        run_time = end_time - start_time
        print(f'Finished {func.__name__} in {run_time}')
        return value

    return wrapper_time
