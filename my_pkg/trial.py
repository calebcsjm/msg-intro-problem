"""Sample code for illustrating python package setup and test-driven development."""

# First code written for python package test.
def square(x):
    """Finds the square of the input.
    
    Args:
        x (float): The number to be squared.
    Returns:
        x2 (float): The squared number.
    """

    return x**2

def factorial(n):
    """Factorial calculates the factorial of the provided integer
    
    Ags: 
        n (int): the value that the factorial will be computed from
    Returns:
        fact (int): the factorial of n.
    Raises:
        ValueError: if n is not an integer.
    """
    
