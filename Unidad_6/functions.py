
def longitud_palabras(lista_inicial: list) -> list:
    """ 
    Calcula cantidad de caracteres para cada 
    elemento de una lista de palabras
    y lo guarda en un diccionario
    """
    # Diccionario de palabras
    dict_palabras = {}

    for  palabra in lista_inicial:
        dict_palabras.update({palabra:len(palabra)})

    return dict_palabras
    
