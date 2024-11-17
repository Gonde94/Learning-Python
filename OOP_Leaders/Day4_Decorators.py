"""
Decorators allow you to extend and modify the behaviour of a callable (functions, 
classes, methods), without permanently modifying the callable itself.

Focusing on functions for now. The function's behaviour is changed when decorated.
"""

import time

# Example 1: This decorator converts input text to upper case
def shout(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@shout
def greet():
    return "Hello there!"


"""
If you didn't use the wrapper function, you'd be replacing the original function
entirely with the decorator. The wrapper function adds behaviour _around_ the original function.
"""

# Example 2: a logging decorator.
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@logging_decorator
def add(a, b):
    return a + b


# Example 3: a timing decorator - measure how long a function takes to execute.
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    return "Finished."


# Examples above add behaviour before or after the original function.
# They ensure the original function's behaviour remains intact while extending its capabilities.


if __name__ == "__main__":

    print("Example 1: ", greet())
    print("Example 2: ", add(2,4))
    print("Example 3: ", slow_function())
