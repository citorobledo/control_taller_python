from Maquina import Maquina


class Taller:
    def __init__(self,
                 baldesDeAceiteEnMes=0
                 ):
        maquinas = []
        maquinasEnReparacion = []
        repuestos = []
        self.maquinas = maquinas
        self.maquinasEnReparacion = maquinasEnReparacion
        self.baldesDeAceiteEnMes = baldesDeAceiteEnMes
        self.repuestos = repuestos

    def ingresarMaquina(self):
        marca, modelo, horas, horasAceite = input("ingrese marca"), input("ingrese modelo"), input("ingrese horas"), input("horas ultimo cambio de aceite")
        self.maquinas.append(Maquina(marca, modelo, horas, horasUltimoCambioAceite = horasAceite))
