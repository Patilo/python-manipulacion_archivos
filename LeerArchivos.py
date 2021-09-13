archivo = open ('CreacionArchivo.txt', 'r', encoding='utf8')
#print(archivo.read())  #aqui lee todo pero hay q especificar si queremos leer mas

# print(archivo.read(5))  #lee los primeros 5 0-4
# print(archivo.readline()) #lee la primera linea

#recorrer el archivo
# for linea in archivo:
#     print(linea)

#leer todas las lineas y acceder a una linea
# print(archivo.readlines()[0]) #primera linea

#leer y copiar un archivo nuevo
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo2.close()
archivo.close()
