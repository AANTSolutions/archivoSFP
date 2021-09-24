"""
version 1

Lo que vamos a hacer es llenar de forma iterativa un archivo CSV.


"""

"""
Lo primero que vamos a hacer es abrir el archivo CSV en modo escritura
"""

archiCSV = open('prueba.dat','w')

"""
Ahora vamos a escribir algo en el archivo, que no esta vacio, para despues cerrarlo
"""

archiCSV.write("Esta frase fue escrita por Python una segunda vez\n")
archiCSV.write("Este es ...")
archiCSV.close()
