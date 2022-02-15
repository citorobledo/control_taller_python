from datetime import date


class Maquina:
    def __init__(self,
                 marca="",
                 modelo="",
                 horas=0,
                 horasUltimoCambioAceite=0,
                 operativa=True,
                 cambiosDeAceite=list(),
                 registroDeReparacines = list()
                 ):
        self.cambiosDeAceite = cambiosDeAceite
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
        return self.cambiosDeAceite[-1]

    def hacerCambioDeAceite(self, horasMauina: int):
        self.horas = horasMauina
        self.cambiosDeAceite.append(f"a las {horasMauina} horas, el {date.today()}")

    def modificarHoras(self, nuevasHoras):
        self.horas = nuevasHoras

    def tiempoFueraDeServicio(self):
        a = date.today() - self.fechaFueraDeServicio
        return a.days

    def ponerOperativa(self):
        self.operativa = True
        self.registroDeReparacines.append(str(date.today()) + " la maquina estuvo fuera de servicio: " + str(self.tiempoFueraDeServicio()) + " dias")

    def infoMaquina(self):
        if self.operativa:
            a = "SI"
        else:
            a = "NO"
        return str(
            "Marca: " + self.marca + "\n" +
            "Modelo: " + self.modelo + "\n" +
            "Esta operativa: " + a + "\n" +
            "Horas: " + str(self.horas) + "\n" +
            "Ultimo cambio de aceite: " + str(self.ultimoCambioAceite()) + "\n")
