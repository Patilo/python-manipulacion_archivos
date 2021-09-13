#USAREMOS METODOS ENTER Y EXIT

class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('entrando al archivo o recurso'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='uft8')
        return self.nombre

    def __exit__(self, tipo_excepcion, valor_exception, traza_error):
        print('cerramos el archivo o recurso'.center(50, '-'))
        if self.nombre:
            self.nombre.close()