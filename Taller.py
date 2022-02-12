from Maquina import Maquina


class Taller:
    def __init__(self,
                 baldesDeAceiteTotales=0,
                 maquinas=[],
                 maquinasEnReparacion=[],
                 repuestos=[]
                 ):
        self.maquinas = maquinas
        self.maquinasEnReparacion = maquinasEnReparacion
        self.baldesDeAceiteTotales = baldesDeAceiteTotales
        self.repuestos = repuestos

    def agregarBaldesAceite(self, cantidad):
        self.baldesDeAceiteTotales += cantidad

    def ingresarMaquina(self):
        marca, modelo, horas, horasAceite = input("ingrese marca: "), input("ingrese modelo: "), \
                                            input("ingrese horas: "), input("horas ultimo cambio de aceite: ")
        print("\n")
        self.maquinas.append(Maquina(marca, modelo, horas, horasUltimoCambioAceite=horasAceite))
