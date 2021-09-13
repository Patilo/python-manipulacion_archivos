try:
    archivo = open('CreacionArchivo.txt' ,'w', encoding='utf8')
    archivo.write('aqui estamos agregando informacion\n')
    archivo.write('Saliendo')

except Exception as e:
    print(e)
finally:
    archivo.close()
    print('fin del archivo')
