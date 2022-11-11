
def open_file(file_name):
    """ Open file"""
    file = open(file_name,'r')
    return file

def line_count(file):
    """count lines"""
   
    number_list = {}
    lines = len(file.readlines())
    number_list.update({file.name:lines}) 
    return number_list

def word_count(file):
    """count numbers of word for line"""
   
    count_list = {}
    for count, line in enumerate(file):
        word = line.split(" ")
        numero = len(word)
        count_list.update({count:numero})
    return count_list          

    