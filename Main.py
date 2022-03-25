import dill
import Main
import json
from Taller import *
from Maquina import *

maq = Maquina()
taller = Taller()


def opciones():
    print(
        "1 para ingresar maquina\n"
        "2 para seleccionar maquina\n"
        "3 para saber caracteristicas\n"
        "4 poner a reparar maquina\n"
        "5 poner maquina operativa\n"
        "6 hacer cambio de aceite\n"
        "7 eliminar maquina\n"
        "8 historial de reparaciones\n"
        "9 registrar reparaión\n"
        "0 para salir\n"
    )
    guardarMaquinas()

def listarMaquinas():
    for i in range(len(taller.maquinas)):
        maqui = taller.maquinas[i]
        print(f"{i + 1}: " + maqui.modelo)
    print("")


def guardarMaquinas():
    with open('maquinas_dill.pkl', 'wb') as file:
        for i in range(len(taller.maquinas)):
            dill.dump(taller.maquinas[i], file)

    #with open("registro.json", "w") as fileJson:
    #    for i in range(len(taller.maquinas)):
    #        json.dump(taller.maquinas[i], fileJson)


def cargarMaquinas():
    with open('maquinas_dill.pkl', 'rb') as fileMaquina:
        while fileMaquina.peek():
            taller.maquinas.append(dill.load(fileMaquina))

    #with open('registro.json', 'r') as fileMaquina:
    #    while fileMaquina.peek():
    #        taller.maquinas.append(dill.load(fileMaquina))


def opcionesResponden(numero):
    if numero == 0:
        guardarMaquinas()
    elif numero == 1:
        taller.ingresarMaquina()
        print("ingresaste correctamente la mauina:\n")

    elif numero == 2:
        listarMaquinas()
        num = int(input("seleccionar maquina: "))
        Main.maq = taller.maquinas[num - 1]
        print(f"- seleccionaste: {Main.maq.modelo} -\n")
    elif numero == 3:
        print("--------- INFO DE LA MAQUINA -----------")
        print("\n" + Main.maq.infoMaquina())
        print("----------------------------------------")
    elif numero == 4:
        Main.maq.ponerAReparar()
        print(f"- Maquina {Main.maq.modelo} en reparacion -\n")
    elif numero == 5:
        Main.maq.ponerOperativa()
        print(f"- la maquina {Main.maq.modelo} ahora esta operativa -\n")
    elif numero == 6:
        Main.maq.hacerCambioDeAceite(int(input("¿cuantas horas tiene la mauina?: \n")))
        print("se registro el cambio de aceite\n")
    elif numero == 7:
        a = input(f"¿estas seguro que vas a eliminar {Main.maq.modelo}?\n 1: para Si\n 2: para No\n")
        if a == "1":
            taller.eliminarMaquina(Main.maq)
            print(f"eliminaste {Main.maq.modelo}: \n")
    elif numero == 8:
        print("----- REGISTRO DE REPARACIONES ----- \n")
        for i in range(len(Main.maq.registroDeReparacines)):
            print(Main.maq.registroDeReparacines[i])
        print("\n------------------------------------")
    elif numero == 9:
        Main.maq.registrarReparacion()
        print("La reparación fué registrada\n")

if __name__ == '__main__':
    opcion = int
    cargarMaquinas()
    while opcion != 0:
        opciones()
        opcion = int(input("ingrese opcion: "))
        opcionesResponden(opcion)

# input()  # para que no se cierre la ventana agrego un input() y antes se le puede poner un "presione enter para terminar"
