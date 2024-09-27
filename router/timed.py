from time import perf_counter


def timed(func):
    def timed_function(*args):
        t0 = perf_counter()
        result = func(*args)
        elapsed = perf_counter() - t0
        name = func.__name__
        print(f"\nFunction [{name}] executed in {elapsed: 0.2f} seconds")
        return result

    return timed_function
