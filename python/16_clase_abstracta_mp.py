from abc import ABC, abstractmethod


class ServicioAeropuerto(ABC):
    @abstractmethod
    def informar(self):
        pass


class MostradorCheckIn(ServicioAeropuerto):
    def informar(self):
        return "El mostrador de check-in esta abierto"


class ControlSeguridad(ServicioAeropuerto):
    def informar(self):
        return "El control de seguridad esta atendiendo pasajeros"


servicios = [MostradorCheckIn(), ControlSeguridad()]
for servicio in servicios:
    print(servicio.informar())
