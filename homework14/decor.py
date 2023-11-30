from functools import wraps


# Task 1
def logger(func):
    """This decorator prints the name of function and its arguments"""
    def func_wrap(*args):
        print(f"{func.__name__}() called with ", *args)
        res = func(*args)
        return res
    return func_wrap


# Task 2
def stop_words(words: list):
    """Delete words from result (must be str)"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            for w in words:
                if w in res:
                    res = res.replace(w, '*')
            return res
        return wrapper
    return decorator


# Task 3
class ArgRules:
    """This decorator checks length and presence of mandatory characters in the argument"""
    def __init__(self, type_: type, max_length=4096, contains=None):
        self.type = type_
        self.maxlen = max_length
        self.contains = contains if contains is not None else []

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args):
            for arg in args:
                if isinstance(arg, str):
                    len_check = len(arg) <= self.maxlen
                    contain_check = all([c in arg for c in self.contains])
                    if not contain_check:
                        print(f"Argument '{arg}' does not contain all mandatory symbols")
                        return False
                    elif not len_check:
                        print(f"Length of argument '{arg}' more than max length")
                        return False
                else:
                    print(f'Type of argument {arg} is not string')
                    return False
            return func(*args)
        return wrapper
