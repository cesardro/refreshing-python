"""
Los formatos docstring más comunes son:
- Google style
- Numpydoc
- reStructuredText (reST)
- Epytext
"""

import inspect


def count_letter(content, letter):
    """Count the number of times `letter` appears in `content`.

    Args:
      content (str): The string to search.
      letter (str): The letter to search for.

    Returns:
      int

    # Add a section detailing what errors might be raised
    Raises:
      ValueError: If `letter` is not a one-character string.
    """
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` must be a single character string.')
    return len([char for char in content if char == letter])


##################################


# Inspect the count_letter() function to get its docstring
docstring = inspect.getdoc(count_letter)

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

##################################


def build_tooltip(function):
    """Create a tooltip for any function that shows the
    function's docstring.

    Args:
      function (callable): The function we want a tooltip for.

    Returns:
      str
    """
    # Get the docstring for the "function" argument by using inspect
    docstring = inspect.getdoc(function)
    border = '#' * 28
    return '{}\n{}\n{}'.format(border, docstring, border)


print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))


##################################

# En caso de que alguien haya modificado los nombres de las funciones podemos hacer lo suguiente para ver su docstring y ver realmente que estamos usando.

import numpy

# fywdkxa = es histogram, por ejemplo.
print(numpy.fywdkxa.__doc__)