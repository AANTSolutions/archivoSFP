"""
This is a script that have some functions about work with files

"""

def abrir_leer(archivo:str):
    archivoAbierto = open(archivo,'r')
    print(archivoAbierto.read())
    archivoAbierto.close()


def escribir_archivo(archivo:str,frase:str):
    archivoAbierto= open(archivo,'w')
    archivoAbierto.write(frase)
    archivoAbierto.write('\n')
    archivoAbierto.close()


def crea_dict(path_archivo:str):
    """

    The next thing that we'll do is the Dictionary; where the table heads were the Dictionary's indexes and the data
    in each register is the value in each Dictionary. therefore we will have a lot of
    Dictionaries the number of registers in the table.

    There is many modes of define a Dictionary to this kind of problem the easiest is using the dict ¿¿method??

    d = dict(zip(['pera','tomate','manzana'],[1.2, 3.5, 4.2]))



    :param path_archivo:
    :return:
    """
    with open(path_archivo,"r") as p:
        # data_csv = csv.DictReader(p)
        # for linea in data_csv.fieldnames:
        #    print(linea)
        encabezado = p.readline()
        encabezadov = encabezado.strip()
        lineas = p.readlines()
        print(p.tell())
        encabezadoF = encabezadov.split(',')

    dict_rows = []
    for linea in lineas:
        lineav = linea.strip()
        reg = lineav.split(',')
        if len(reg) != len(encabezadoF):
            raise Exception("invalid CSV")
        d = dict(zip(encabezadoF,reg))
        dict_rows.append(d)

    return dict_rows,reg

def crea_lista(path_archivo:str):
    with open(path_archivo,"r") as p:
        # data_csv = csv.DictReader(p)
        # for linea in data_csv.fieldnames:
        #    print(linea)
        encabezado = p.readline()
        encabezadov = encabezado.strip()
        lineas = p.readlines()
        # print(p.tell())
        encabezadoF = encabezadov.split(',')

    dict_rows = []
    for linea in lineas:
        lineav = linea.strip()
        reg = lineav.split(',')
        # if len(reg) != len(encabezadoF):
        #     raise Exception("invalid CSV")
        # d = dict(zip(encabezadoF,reg))
        # dict_rows.append(d)

    return reg

