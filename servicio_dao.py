from cursor_pool import CursorPool
from servicio import Servicio

class ServicioDAO:
    _SELECCIONAR    = 'SELECT * FROM servicios ORDER BY id_servicios;'
    _INSERTAR       = 'INSERT INTO servicios(nombre_servicio, proceso, notas) VALUES(%s, %s, %s);'
    _ACTUALIZAR     = 'UPDATE servicios SET nombre_servicio=%s, proceso=%s, notas=%s WHERE id_servicios=%s;'
    _ELIMINAR       = 'DELETE FROM servicios WHERE id_servicios=%s;'
    _BUSCAR         = "SELECT * FROM servicios WHERE nombre_servicio LIKE"

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            servicios = []
            for registro in registros:
                servicio = Servicio(registro[0], registro[1], registro[2], registro[3])
                servicios.append(servicio)
            return servicios

    @classmethod
    def insertar(cls, servicio):
        with CursorPool() as cursor:
            valores = (servicio.nombre_servicio, servicio.proceso, servicio.notas)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, servicio):
        with CursorPool() as cursor:
            valores = (servicio.nombre_servicio, servicio.proceso, servicio.notas, servicio.id_servicios)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, servicio):
        with CursorPool() as cursor:
            valores = (servicio.id_servicios,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount

    @classmethod
    def buscar(cls, servicio):
        with CursorPool() as cursor:
            valores = (servicio.nombre_servicio)
            cursor.execute(cls._BUSCAR + f"'%{valores}%'")
            registros = cursor.fetchall()
            return registros

if __name__ == '__main__':
    usuarios = ServicioDAO.seleccionar()
    for usuario in usuarios:
        print(usuario)

    servicio = Servicio(nombre_servicio='Agua')
    servicios = ServicioDAO.buscar(servicio)
    for i in servicios:
        print(i)

    id = 4
    servicio = Servicio(id_servicios=id)
    servicios_eliminados = ServicioDAO.eliminar(servicio)
    print('Servicios eliminados', f'Se han eliminado {servicios_eliminados} servicio')