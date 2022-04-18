class Servicio:
    def __init__(self, id_servicios = None, nombre_servicio = None, proceso = None, notas = None):
        self._id_servicios = id_servicios
        self._nombre_servicio = nombre_servicio
        self._proceso = proceso
        self._notas = notas

    def __str__(self):
        return f'\nServicio: {self._id_servicios}, {self._nombre_servicio}, {self._proceso}, {self._notas}\n'

    @property
    def id_servicios(self):
        return self._id_servicios

    @id_servicios.setter
    def id_servicios(self, id_servicios):
        self._id_servicios = id_servicios

    @property
    def nombre_servicio(self):
        return self._nombre_servicio

    @nombre_servicio.setter
    def nombre_servicio(self, nombre_servicio):
        self._nombre_servicio = nombre_servicio

    @property
    def proceso(self):
        return self._proceso

    @proceso.setter
    def proceso(self, proceso):
        self._proceso = proceso

    @property
    def notas(self):
        return self._notas

    @notas.setter
    def notas(self, notas):
        self._notas = notas