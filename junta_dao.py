from cursor_pool import CursorPool
from logger_base import log
from juntas import Juntas

class JuntasDAO:
    _SELECCIONAR    = 'SELECT * FROM juntas ORDER BY id_junta;'
    _INSERTAR       = 'INSERT INTO juntas(junta, fecha_junta) VALUES(%s, %s);'
    _ACTUALIZAR     = 'UPDATE juntas SET junta=%s, fecha_junta=%s WHERE id_junta=%s;'
    _ELIMINAR       = 'DELETE FROM juntas WHERE id_junta=%s;'
    _BUSCAR         = "SELECT * FROM juntas WHERE junta LIKE"

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            log.debug('Seleccionando juntas...')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            return registros

    @classmethod
    def insertar(cls, junta):
        with CursorPool() as cursor:
            log.debug(f'Junta a insertar: {junta}')
            valores = (junta.junta, junta.fecha_junta)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, junta):
        with CursorPool() as cursor:
            log.debug(f'Junta a actualizar: {junta}')
            valores = (junta.junta, junta.fecha_junta, junta.id_junta)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, junta):
        with CursorPool() as cursor:
            log.debug(f'Junta a cancelar: {junta}')
            valores = (junta.id_junta,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount

    @classmethod
    def buscar(cls, junta):
        with CursorPool() as cursor:
            log.debug(f'Buscando: {junta}')
            valores = (junta.junta)
            cursor.execute(cls._BUSCAR + f"'%{valores}%'")
            registros = cursor.fetchall()
            return registros


if __name__ == '__main__':
    juntas = JuntasDAO.seleccionar()
    for junta in juntas:
        print(junta)
    junta = Juntas(junta='Auditoria')
    juntas = JuntasDAO.buscar(junta)
    for junta in juntas:
        print(junta)
        print(type(junta))
        print(type(junta[2]))
        junta = str(junta[2])
        print(type(junta))
        print(junta)
