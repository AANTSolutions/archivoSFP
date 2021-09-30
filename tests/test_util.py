"""
Version 3
This version is write in a meeting work with Oscar Liguori's team.

This scrip makes Dictionaries using CSV text files that the user give inside the system

This scrip process the lines in the CSV file more than his version 1.

"""
import pytest


class TestUtil:
    def test_crea_dict_exito(self):
        from archivoSFP.lib.util import crea_dict
        expected_result = [{'A':'a1','B':'b1'}]

        example_path = "test_examples/prueba_01.csv"
        result = crea_dict(example_path)
        assert expected_result == result

    def test_crea_dict_error(self):
        from archivoSFP.lib.util import crea_dict
        # expected_result = [{'A':'a1','B':'b1','C':''},{'A':'a2','B':'b2','C':'c2'}]

        example_path = "test_examples/prueba_02.csv"
        with pytest.raises(Exception):
            result = crea_dict(example_path)





# encabezado = "A,B,C,D,E,F,G,H,I"
# lineas = ['0,1,2,3,4,5,6,7,8','10,11,12,13,14,15,16,17,18','20,21,22,23,24,25,26,27,28']
#
# texto = encabezado + '\n' + '\n'.join(lineas)
# tratadorArchivo.escribir_archivo('prueba.dat',texto)
#
#
#
# # import csv
#
# tratadorArchivo.crea_dict("prueba.dat")
