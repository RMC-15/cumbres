from logger_base import log
from conexion import Conexion

class CursorPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio el método del with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Se ejecuta el método __exit__')
        if exc_val:
            self._conexion.rollback()
            log.error('Ocurrió un error, se hizo rollback')
        else:
            self._conexion.commit()
            log.debug('Commit de transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug('Dentro del bloque With')
        cursor.execute('SELECT * FROM usuarios')
        log.debug(cursor.fetchall())