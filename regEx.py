"""
version 1

Vamos a generar es renglones de un archivo CSV de forma iterativa con Expresiones Regulares

"""

"""
Lo primero es generar imprimir una pequeña cadena de caracteres que termine con el caracter especial ','
"""

import re

encabezado=['A','B','C','D','E','F','G','H','I']
print(encabezado)
renglon1=list(range(9))
print(renglon1)
renglon2 = list(range(10,19))
print(renglon2)
renglon3 = list(range(20,29))
print(renglon3)

"""
Ahora vamos a abrir el archivo en modo escritura para escribir los renglones

NOTA: aquí deberia estar una llamada al script escribirCSVfile.py mandando los renglones 
incluyendo el encabezado como parametros para el script

Si tenemos la siguiente lista (mejor desde aqui usamos Diccionario? para guardar cada renglon)

paragraph= ['encabezado]
"""

archivoDAT = open('prueba.dat','w')

archivoDAT.write(str(encabezado))
archivoDAT.write("\n")
archivoDAT.write(str(renglon1))

"""
Despues de la llamada al script para escribir en un archivo, ahora vamos a modificar lo 
escrito en dicho archivo para que cumpla con la sintaxis y estructura de los archivos CSV
"""

textoArchivo= open('prueba.dat','r')
texto= "['A','B','C','D','E','F','G','H','I']\n[0,1,2,3,4,5,6,7,8]\n[10,11,12,13,14,15,16,17,18]\n[20,21,22,23,24,25,26,27,28]"

print(re.sub(r'^\[','',texto))
"""


print(re.sub(r'^\[' | r'^\[\'','',texto,0,re.M))

"""