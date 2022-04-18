class Juntas:
    def __init__(self, id_junta=None, junta=None, fecha_junta=None):
        self._id_junta = id_junta
        self._junta = junta
        self._fecha_junta = fecha_junta

    def __str__(self):
        return f'\nJunta numero: {self._id_junta}, {self._junta} el día {self._fecha_junta}\n'

    @property
    def id_junta(self):
        return self._id_junta

    @id_junta.setter
    def id_usuario(self, id_junta):
        self._id_junta = id_junta

    @property
    def junta(self):
        return self._junta

    @junta.setter
    def junta(self, junta):
        self._junta = junta

    @property
    def fecha_junta(self):
        return self._fecha_junta

    @fecha_junta.setter
    def password(self, fecha_junta):
        self._fecha_junta = fecha_junta