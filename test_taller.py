import unittest
from unittest.mock import MagicMock, Mock
from datetime import date

import every as every
import returns as returns

from Maquina import Maquina
from Taller import Taller

maq = Maquina("Toro", "RM 5410", 234, True)
taller = Taller()

class TestMaquina(unittest.TestCase):

    def test_Caracteristicas(self):
        self.assertTrue(maq.marca == "Toro")  # add assertion here
        self.assertTrue(maq.modelo == "RM 5410")
        self.assertTrue(maq.horas == 234)
        self.assertTrue(maq.operativa)

    def test_PonerAReparar(self):
        maq.ponerAReparar()
        self.assertFalse(maq.operativa)
        self.assertTrue(maq.fechaFueraDeServicio == date.today())

    def test_ConsultarUltimoCambioAceite(self):
        maq.horasUltimoCambioAceite = 134
        self.assertTrue(maq.horasUltimoCambioAceite == 134)

    def test_CambiarHoras(self):
        maq.modificarHoras(500)
        self.assertTrue(maq.horas == 500)
        maq.modificarHoras(234)  # este vuelve las hora para que no falle el primer test

    def test_TiempoFueraDeServicio(self):
        maq.fechaFueraDeServicio = date(2022, 1, 10)
        a = maq.tiempoFueraDeServicio()
        b = date.today() - maq.fechaFueraDeServicio
        self.assertTrue(a == b.days)

    def test_PonerOperativa(self):
        maq.operativa = False
        maq.ponerOperativa()

        self.assertTrue(maq.operativa)
        self.assertTrue(len(maq.registroDeReparacines) == 1)
        self.assertTrue(
            maq.registroDeReparacines[0] == str(date.today()) + " la maquina estuvo fuera de servicio: " + str(maq.tiempoFueraDeServicio))

class TestTaller(unittest.TestCase):

    def test_caracteristicas(self):
        taller.baldesDeAceiteEnMes = 5
        self.assertTrue(taller.baldesDeAceiteEnMes == 5)
        self.assertTrue(taller.maquinas == [])
        self.assertTrue(taller.maquinasEnReparacion == [])
        self.assertTrue(taller.repuestos == [])

    def test_ingresarMaquina(self):

        taller.ingresarMaquina()



if __name__ == '__main__':
    unittest.main()
