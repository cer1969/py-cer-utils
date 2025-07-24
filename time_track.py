# © Cristian Echeverría Rabí

import time

#--------------------------------------------------------------------------------------------------

def time_track(info):
    """
    Decorator function that tracks the execution time of a given function.

    Parameters:
        info (str): A string describing the purpose or context of the function being tracked.

    Returns:
        function: A decorated function that measures the execution time and prints the result.

    Example:
        @time_track("Calculation")
        def add_numbers(a, b):
            return a + b

        result = add_numbers(3, 5)
        # Output: Calculation demoró: 0.000123 segundos.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"{info} demoró: {end - start} segundos")
            print("-----------------------------------------------")
            return result
        return wrapper
    return decorator

