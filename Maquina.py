from datetime import date


class Maquina:
    def __init__(self,
                 marca="",
                 modelo="",
                 horas=int,
                 operativa=bool,
                 horasUltimoCambioAceite=int ):
        self.registroDeReparacines = list
        self.fechaFueraDeServicio = date
        self.marca = marca
        self.modelo = modelo
        self.horas = horas
        self.operativa = operativa
        self.horasUltimoCambioAceite = horasUltimoCambioAceite


    def ponerAReparar(self):
        operativa = False
        fechaFueraDeServicio = date.today()  # importa el dia del sistema

    def ultimoCambioAceite(self):
        return self.horasUltimoCambioAceite

    def modificarHoras(self, nuevasHoras): self.horas = nuevasHoras

    def tiempoFueraDeServicio(self):
        meses = self.fechaFueraDeServicio.until(date.today()).toTotalMonths()
        dias = self.fechaFueraDeServicio.until(date.today()).days
        return f"{meses} meses y {dias} dias"

    def ponerOperativa(self):
        operativa = True
        self.registroDeReparacines.append( str( date.today() ) + " la maquina estuvo fuera de servicio: " + self.tiempoFueraDeServicio )
