from datetime import date


class Maquina:
    def __init__(self,
                 marca="",
                 modelo="",
                 horas=0,
                 operativa=bool,
                 horasUltimoCambioAceite=0,
                 ):
        registroDeReparacines = []
        self.registroDeReparacines = registroDeReparacines
        self.fechaFueraDeServicio = None
        self.marca = marca
        self.modelo = modelo
        self.horas = horas
        self.operativa = operativa
        self.horasUltimoCambioAceite = horasUltimoCambioAceite

    def ponerAReparar(self):
        self.operativa = False
        self.fechaFueraDeServicio = date.today()  # importa el dia del sistema

    def ultimoCambioAceite(self):
        return self.horasUltimoCambioAceite

    def modificarHoras(self, nuevasHoras): self.horas = nuevasHoras

    def tiempoFueraDeServicio(self):
        a = date.today() - self.fechaFueraDeServicio
        return a.days

    def ponerOperativa(self):
        self.operativa = True
        self.registroDeReparacines.append(
            str(date.today()) + " la maquina estuvo fuera de servicio: " + str(self.tiempoFueraDeServicio))
