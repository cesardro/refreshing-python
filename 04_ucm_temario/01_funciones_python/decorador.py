import time
import signal
from functools import wraps


def print_before_and_after(func):
    def wrapper(*args):
        print('Before {}'.format(func.__name__))
        # Call the function being decorated with *args
        func(*args)
        print('After {}'.format(func.__name__))
    # Return the nested function
    return wrapper


@print_before_and_after
def multiply(a, b):
    print(a * b)


multiply(5, 10)

print('##############################################')


def print_return_type(func):
    # Define wrapper(), the decorated function
    def wrapper(*args, **kwargs):
        # Call the function being decorated
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(
            func.__name__, type(result)
        ))
        return result
    # Return the decorated function
    return wrapper


@print_return_type
def foo(value):
    return value


print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))


print('##############################################')


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return wrapper.count
    # Set count to 0 to initialize call count for each new decorated function
    wrapper.count = 0
    # Return the new decorated function
    return wrapper

# Decorate foo2() with the counter() decorator


@counter
def foo2():
    print('calling foo2()')


foo2()
foo2()

print('foo2() was called {} times.'.format(foo2.count))


print('##############################################')

# It prints the docstring of the wrapper function, not the decorated function.


def add_hello(func):
    # Add a docstring to wrapper
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)
    return wrapper


@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)


print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

print('##############################################')

# To fix example above and print the docstring of the decorated function, we can use functools.wraps().
# And decorate the wrapper function with functools.wraps() and pass in the decorated function as an argument.


def add_hello(func):
    # Decorate wrapper() so that it keeps func()'s metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)
    return wrapper


@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)


print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)

print('##############################################')

# functools.wraps() also adds the __wrapped__ attribute to wrapper(), which points to the original function.
# Calling it runs the original function directly, skipping the extra behavior added by the decorator.

# Decorated: prints 'Hello' and then the sum
print_sum(10, 20)

# Original: only prints the sum (no 'Hello')
print_sum.__wrapped__(10, 20)

# False: wrapper() and the original are different objects
print(print_sum.__wrapped__ is print_sum)
print(print_sum.__wrapped__.__name__)  # print_sum

print('##############################################')

# This is a decorator factory, which is a function that returns a decorator.
# The decorator returned by run_n_times() will call the decorated function n times.


def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

# Make print_sum() run 10 times with the run_n_times() decorator


@run_n_times(3)
def print_sum(a, b):
    print(a + b)


print_sum(15, 20)


# Use run_n_times() to create the run_five_times() decorator
run_five_times = run_n_times(2)


@run_five_times
def print_sum(a, b):
    print(a + b)


print_sum(4, 100)

# Modify the print() function to always run 3 times
#print = run_n_times(3)(print)

"""
Es equivalente a decorar print_sum de otra forma:

def print_sum(a, b):
    print(a + b)
print_sum = run_n_times(3)(print_sum)

Solo que en este caso, estamos literalmente decorando la función print() de Python, 
así que cada vez que llamemos a print(), se ejecutará 3 veces.
"""

print('What is happening?!?!')


print('##############################################')


def tag(*tags):
    # Define a new decorator, named "decorator", to return
    def decorator(func):
        # Ensure the decorated function keeps its metadata
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Call the function being decorated and return the result
            return func(*args, **kwargs)
        wrapper.tags = tags
        return wrapper
    # Return the new decorator
    return decorator


@tag('test', 'this is a tag')
def foo():
    pass


print(foo.tags)


print('##############################################')

def raise_timeout(*args, **kwargs):
    raise TimeoutError()

signal.signal(signalnum=signal.SIGALRM, handler=raise_timeout)

def timeout(n_seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Activates an alarm in n secods.
            signal.alarm(n_seconds)
            try:
                # Calls the decorated functions
                return func(*args, **kwargs)
            finally:
                # Deactivates the alarm
                signal.alarm(0)
        return wrapper
    return decorator


@timeout(5)
def foo():
    time.sleep(10)
    print('foo() finished')


@timeout(20)
def bar():
    time.sleep(10)
    print('bar() finished')

foo()
bar()
