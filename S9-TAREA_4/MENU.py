import os
from listas import Lista
from pilas import Pila
from cola import Cola

class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elija opcion[1...{}]:".format(len(self.opciones)))
        return opc

opc =""
while opc !="4":
    os.system("cls")
    men = Menu("Menu Operaciones",["1) Listas","2) Pilas","3) Colas","4) Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 =""
        numeros = Lista()
        while opc1 !="7":
            os.system("cls")
            men1 = Menu("\033[3;36m"+"Menu Listas",["\033[0;33m"+"1) Push","2) Pop","3) Show","4) Eliminar","5) Insertar","6) Buscar","7) Salir"])
            opc1 = men1.menu()
            os.system("cls")

            if opc1 == "1":
                print("PUSH")
                dato = input("Ingrese un dato a la Lista: ")
                numeros.push(dato)
                print(numeros.lista)
                input("Presione una tecla para continuar...")

            elif opc1 == "2":
                print("POP")
                dato = numeros.pop()
                if dato: print("El dato eliminado es: {}".format(dato))
                else: print("La lista esta vacia")
                input("Presione una tecla para continuar...")

            elif opc1 == "3":
                print("SHOW")
                numeros.mostrar()
                input("Presione una tecla para continuar...")

            elif opc1 == "4":
                print("ELIMINAR")
                dato = int(input("Ingrese la posicion del valor ha eliminar: "))
                numeros.eliminarElemento(dato)
                print(numeros.lista)
                input("Presione una tecla para continuar...")

            elif opc1 == "5":
                print("INSERTAR")
                pos = int(input(("Ingrese la posicion en la que desea insertar el valor: ")))
                valor = int(input("Ingrese el dato a insertar en la Lista: "))
                numeros.insertarElemento(pos,valor)
                print(numeros.lista)
                input("Presione una tecla para continuar...")

            elif opc1 == "6":
                print("BUSCAR")
                dato = input("Ingrese el dato que desea buscar: ")
                print(numeros.buscar(dato))
                input("Presione una tecla para continuar...")

    elif opc =="2":
        opc2 =""
        pila1 = Pila()
        while opc2 !="6":
            os.system("cls")
            men2 = Menu("\033[3;36m"+"Menu Pilas",["\033[0;33m"+"1) Push","2) Pop","3) Show","4) Buscar","5) Longitud","6) Salir"])
            opc2 = men2.menu()
            os.system("cls")

            if opc2 == "1":
                print("PUSH")
                dato = input("Ingrese un dato a la Pila: ")
                pila1.push(dato)
                print(pila1.lista)
                input("Presione una tecla para continuar...")

            elif opc2 == "2":
                print("POP")
                dato = pila1.pop()
                if dato: print("El dato eliminado es: {}".format(dato))
                else: print("La pila esta vacia")
                input("Presione una tecla para continuar...")

            elif opc2 == "3":
                print("SHOW")
                print(pila1.show())
                input("Presione una tecla para continuar...")

            elif opc2 == "4":
                print("BUSCAR")
                buscar = input("Ingresar el valor a buscar: ")
                print(pila1.buscar(buscar))
                input("Presione una tecla para continuar...")

            elif opc2 == "5":
                print("LONGITUD")
                print(pila1.longitud())
                input("Presione una tecla para continuar...")

    elif opc == "3":
        opc3 =""
        cola1 = Cola()
        while opc3 !="6":
            os.system("cls")
            men3 = Menu("\033[3;36m"+"Menu Colas",["\033[0;33m"+"1) Push","2) Pop","3) Show","4) Buscar","5) Longitud","6) Salir"])
            opc3 = men3.menu()
            os.system("cls")

            if opc3 == "1":
                print("PUSH")
                dato = input("Ingrese el dato a encolar: ")
                cola1.push(dato)
                print(cola1.cola)
                input("Presione una tecla para continuar...")

            elif opc3 == "2":
                print("POP")
                dato = cola1.pop()
                if dato: print("El dato eliminado es: {}".format(dato))
                else: print("La cola esta vacia")
                input("Presione una tecla para continuar...")

            elif opc3 == "3":
                print("SHOW")
                cola1.show()
                input("Presione una tecla para continuar...")

            elif opc3 == "4":
                print("BUSCAR")
                buscar = input("Ingresar el valor a buscar: ")
                print(cola1.buscar(buscar))
                input("Presione una tecla para continuar...")

            elif opc3 == "5":
                print("LONGITUD")
                print(cola1.longitud())
                input("Presione una tecla para continuar...")

    elif opc == "4":
            print("Gracias por usar el sistema ")
    else:
            print("Opcion no valida")

print("Lo esperamos en una proxima ocasion")



