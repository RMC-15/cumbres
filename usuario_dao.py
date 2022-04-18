from cursor_pool import CursorPool
from logger_base import log
from usuario import Usuario

class UsuarioDAO:
    _SELECCIONAR    = 'SELECT * FROM usuarios ORDER BY id_user;'
    _INSERTAR       = 'INSERT INTO usuarios(username, password) VALUES(%s, %s);'
    _ACTUALIZAR     = 'UPDATE usuarios SET username=%s, password=%s WHERE id_user=%s;'
    _ELIMINAR       = 'DELETE FROM usuarios WHERE id_user=%s;'
    _BUSCAR         = "SELECT * FROM usuarios WHERE username LIKE"
    _LOGIN          = 'SELECT * FROM usuarios WHERE username = %s'


    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            log.debug('Seleccionando usuarios...')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount

    @classmethod
    def buscar(cls, usuario):
        with CursorPool() as cursor:
            log.debug(f'Buscando: {usuario}')
            valores = (usuario.username)
            cursor.execute(cls._BUSCAR + f"'%{valores}%'")
            registros = cursor.fetchall()
            #usuarios = []
            #for registro in registros:
            #    usuario = Usuario(registro[0], registro[1], registro[2])
            #    usuarios.append(usuario)
            return registros

    @classmethod
    def login(cls, usuario):
        with CursorPool() as cursor:
            log.debug(f'Buscando: {usuario}')
            valores = (usuario.username,)
            cursor.execute(cls._LOGIN, valores)
            registros = cursor.fetchall()
            # usuarios = []
            # for registro in registros:
            #    usuario = Usuario(registro[0], registro[1], registro[2])
            #    usuarios.append(usuario)
            return registros

if __name__ == '__main__':
    usuario = Usuario(username='rmora')
    usuarios = UsuarioDAO.login(usuario)
    for usuario in usuarios:
        print(usuario)
        print(type(usuario))
