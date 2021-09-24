"""
Script for open, read and print the content of an CSV file

version 1

Autor

"""


"""
Lo primero que vamos a hacer es abrir el archivo despues al imprimir vamos a leer el contenido,
finalmente cerramos el archivo
"""

archivoCSV = open('prueba.dat','r')
print(archivoCSV.read())
archivoCSV.close()

