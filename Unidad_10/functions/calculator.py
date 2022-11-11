def add(a: float, b: float) -> float:
    """Add operation.

    :param a: first argument value
    :type a: float
    :param b: second argument value
    :type b: float
    :return: add operation
    :rtype: float
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract operation.

    :param a: first argument value
    :type a: float
    :param b: second argument value
    :type b: float
    :return: substract operation
    :rtype: float
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply operation.

    :param a: first argument value
    :type a: float
    :param b: second argument value
    :type b: float
    :return: multiply operation
    :rtype: float
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide operation.

    :param a: first argument value
    :type a: float
    :param b: second argument value
    :type b: float
    :raises ZeroDivisionError: _description_
    :return: divide operation
    :rtype: float
    """
    if b == 0:
        raise ZeroDivisionError('Error divide by zero!')
    return a / b