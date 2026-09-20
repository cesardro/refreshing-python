# Call has_docstring() on the load_and_plot_data() function
def load_and_plot_data():
    """Load and plot data."""
    pass


def has_docstring(func):
    """Check to see if the function 

    `func` has a docstring.

    Args:

      func (callable): A function.

    Returns:

      bool
    """
    return func.__doc__ is not None


ok = has_docstring(load_and_plot_data)

if not ok:
    print("load_and_plot_data() doesn't have a docstring!")
else:
    print("load_and_plot_data() looks ok")

########################################


def create_math_function(func_name):
    if func_name == 'add':
        def add(a, b):
            return a + b
        return add
    elif func_name == 'subtract':
        # Define the subtract() function
        def subtract(a, b):
            return a-b
        return subtract
    else:
        print("I don't know that one")


add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))
