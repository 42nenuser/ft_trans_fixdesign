def square(x: int | float) -> int | float:
    """
    Returns the square of a number.
    """
    return x * x

def pow(x: int | float) -> int | float:
    """
    Returns the number raised to the power of itself (x^x).
    """
    return x ** x

def outer(x: int | float, function) -> object:
    """
    Takes a number and a function as arguments and returns an object
    that computes the result of the function on subsequent calls.
    """
    count = 0  # Keeps track of how many times the inner function is called

    def inner() -> float:
        nonlocal count
        count += 1
        # Apply the function repeatedly
        result = function(x)
        for _ in range(count - 1):
            result = function(result)
        return result

    return inner
