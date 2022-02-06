import unittest
from datetime import date

from Maquina import Maquina

maq = Maquina("Toro", "RM 5410", 234, True)


class TestTaller(unittest.TestCase):

    def test_Caracteristicas(self):
        # self.assertEqual(True, False)
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
        self.assertTrue(a == 26)

    def test_PonerOperativa(self):
        maq.operativa = False
        maq.ponerOperativa()

        self.assertTrue(maq.operativa)
        self.assertTrue(len(maq.registroDeReparacines) == 1)
        self.assertTrue(
            maq.registroDeReparacines.pop(0) == "2022-02-05" + " la maquina estuvo fuera de servicio: " + str(
                maq.tiempoFueraDeServicio))


if __name__ == '__main__':
    unittest.main()
