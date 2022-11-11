MEANS_TRANSPORT = [
    'auto',
    'avión',
    'barco',
    'bicicleta',
    'ómnibus']


def get_transport(msg: str) -> str:
    """This function user enters index number of list and print the text.

    :param msg: message value
    :type msg: str
    :return: index value
    :rtype: str
    """
    try:
        print(msg)
        index = int(input('Enter a positive index number:'))
    except ValueError:
        return get_transport("Invalid value error. Try again")
    else:
        try:
            return MEANS_TRANSPORT[index]
        except IndexError:
            return get_transport("Error index does not exist. Try again")
