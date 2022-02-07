# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import main
from Taller import *
from Maquina import *

taller = Taller()
a = int
maquina = Maquina()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'hola, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def opciones():
    print(
        "1 para ingresar maquina\n"
        "2 para seleccionar maquina\n"
        "3 para saber caracteristicas\n"
        "0 para salir\n"
    )


def listarMaquinas():
    for i in range(len(taller.maquinas)):
        a =taller.maquinas[i]
        print(f"{i+1}: " + a.modelo )
    print("")


def opcionesResponden(numero):

    if numero == 0:
        main.a = 0
    elif numero == 1:
        return taller.ingresarMaquina()
    elif numero == 2:
        listarMaquinas()
        a = int(input("seleccionar maquina: "))
        main.maquina = taller.maquinas[a-1]
        print(f"seleccionaste: {main.maquina.modelo}\n")
    elif numero == 3:
        print("\n" + main.maquina.infoMaquina())


if __name__ == '__main__':

    while main.a != 0:
        opciones()
        opcionesResponden(int(input("ingrese opcion: ")))

# input()  # para que no se cierre la ventana agrego un input() y antes se le puede poner un "presione enter para terminar"
