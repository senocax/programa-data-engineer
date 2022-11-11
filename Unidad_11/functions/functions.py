# Funciones.
def add(a: float, b: float) -> float:
    """Add operation.

    :param a: first argument value
    :type a: float
    :param b: second argument value
    :type b: float
    :return: add operation
    :rtype: float
    """
    operation= a + b
    return operation


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

def get_add(a, b) -> float:
    """ Get result add operation.

    :param a: first argument value
    :type a: float
    :param b: second argument value
    :type b: float
    :return: result add
    :rtype: float
    """
    result = add(a, b) 
    return result

def get_subtract(a, b) -> float:
    """Get result subtract operation.

    :param a: first argument value
    :type a: float
    :param b: second argument value
    :type b: float
    :return: result subtract
    :rtype: float
    """
    result = subtract(a, b) 
    return result

def get_multiply(a, b) -> float:
    """Get result multiply operation.

    :param a: first argument value
    :type a: float
    :param b: second argument value
    :type b: float
    :return: result multiply
    :rtype: float
    """
    result = multiply(a, b) 
    return result

def get_divide(a, b) -> float:
    """Get result divide operation.

    :param a: first argument value
    :type a: float
    :param b: second argument value
    :type b: float
    :return: result divide
    :rtype: float
    """
    result = divide(a, b) 
    return result
