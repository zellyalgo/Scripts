claves = open("clave") # Este es el archivo donde tengo las claves para hacer la codificacion los que estan en la primera columna quiero que se codifiquen en mi archivo file en 1 los de la segunda en 2 y los de la tercera en 3.
clave_lineas = list()


def parse_to_number(genomas, keys):
    contador = 0
    number_list = list()
    for genoma in genomas:
        try:
            number_list.append((genoma, keys[contador].index(genoma) + 1))
        except ValueError:
            number_list.append((genoma, '0'))
        contador += 1
    return number_list


for clave in claves:
    clave_lineas.append(clave.strip().split("\t")) # aqui me transformo la clave que tengo en un array donde pueda seleccionar la casilla que me interesa

content = open("genotiposanocolumna").readlines()
file = map(lambda x: x.strip(), content) # la funcion map recorre una lista ejecutando una f(x).

final_genoma = list()
genoma_row = list()
contador = 1
for genoma in file:
    genoma_row.append(genoma)
    if contador % 192 == 0:
        final_genoma.append(genoma_row)
        genoma_row = list()
    contador+=1
final_result = list(map(lambda x: parse_to_number(x, clave_lineas), final_genoma))
print(final_genoma)
print(final_result)


archivo = open("rs2.txt", "w") # este es el archivo de salida | SI abres un fichero en modo escritura, siempre cierralo
for genoma_result in final_result:
    for genoma, value in genoma_result:
        archivo.write('%s\t%s\t' % (genoma, value))
    archivo.write('\n')
archivo.close()
