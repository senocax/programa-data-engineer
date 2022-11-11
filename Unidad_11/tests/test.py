import os, sys
import datetime
sys.path.append('../')
import unittest
from functions.functions import get_divide, get_multiply, get_subtract, get_add

# Imports para configurar docs_from_tests

from pathlib import Path
from docs_from_tests.instrument_call_hierarchy import (
    instrument_and_import_package,
    initialise_call_hierarchy,
    finalise_call_hierarchy
)

instrument_and_import_package(os.path.join(Path(__file__).parent.absolute(), '..', 'functions'), 'functions')

class TestCalc(unittest.TestCase):

    def test_operations(self):
        """Test add, subtract, multiply, divide operations."""
        initialise_call_hierarchy('start')
        self.assertEqual(get_add(1, 5), 6)
        self.assertEqual(get_add(-1, 1), 0)
        self.assertEqual(get_add(-3, -1), -4)
        #test subtract
        self.assertEqual(get_subtract(1, 5),-4)
        self.assertEqual(get_subtract(-1, 1), -2)
        self.assertEqual(get_subtract(-2, -2), 0)
        #test multiply
        self.assertEqual(get_multiply(10, 9), 90)
        self.assertEqual(get_multiply(-2, 2), -4)
        self.assertEqual(get_multiply(-1, -1), 1)
        #test divide
        self.assertEqual(get_divide(15, 5), 3)
        self.assertEqual(get_divide(-2, 1), -2)
        self.assertEqual(get_divide(5, 2), 2.5)

        with self.assertRaises(ZeroDivisionError):
            get_divide(25, 0)

        # Finalizamos la secuencia
        root_call = finalise_call_hierarchy()
        # Retornamos el diagrama de secuencia
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )

        # Escribimos el archivo de la secuencia en formato markdown   
        sequence_diagram_filename = os.path.join(os.path.dirname(__file__), '..', 'doc', 'diagrama de secuencia.md')
        Path(sequence_diagram_filename).write_text(sequence_diagram)
   
def insert_header(f):
    f.write('\n')
    f.write('******************TESTING**************************')
    f.write('\n')
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    f.write(date_time)
    f.write('\n')
    return f

def main(out = sys.stderr, verbosity = 2):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)
        
if __name__ == '__main__':
    with open('testing.txt', 'a') as f:
        f = insert_header(f)
        main(f)
