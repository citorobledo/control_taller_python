import dill
import Main
from Taller import *
from Maquina import *

maq = Maquina()
taller = Taller()


def opciones():
    print(
        "1 para ingresar maquina\n"
        "2 para seleccionar maquina\n"
        "3 para saber caracteristicas\n"
        "0 para salir\n"
    )


def listarMaquinas():
    for i in range(len(taller.maquinas)):
        maqui = taller.maquinas[i]
        print(f"{i + 1}: " + maqui.modelo)
    print("")


def guardarMaquinas():
    with open('maquinas_dill.pkl', 'wb') as file:
        for i in range(len(taller.maquinas)):
            dill.dump(taller.maquinas[i], file)


def cargarMaquinas():
    with open('maquinas_dill.pkl', 'rb') as file:
        while file.peek():
            taller.maquinas.append(dill.load(file))


def opcionesResponden(numero):
    if numero == 0:
        guardarMaquinas()
        return 0
    elif numero == 1:
        return taller.ingresarMaquina()
    elif numero == 2:
        listarMaquinas()
        num = int(input("seleccionar maquina: "))
        Main.maq = taller.maquinas[num - 1]
        print(f"seleccionaste: {Main.maq.modelo}\n")
        return
    elif numero == 3:
        print("\n" + Main.maq.infoMaquina())


if __name__ == '__main__':
    opcion = int
    cargarMaquinas()
    while opcion != 0:
        opciones()
        opcion = int(input("ingrese opcion: "))
        opcionesResponden(opcion)

# input()  # para que no se cierre la ventana agrego un input() y antes se le puede poner un "presione enter para terminar"
