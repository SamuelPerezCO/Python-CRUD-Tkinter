'''
from Cities import Countries

paises = Countries()

menu = "==========================
* MENU paises *
==========================
*                        *
* i) Insertar Registros  *
* e) Eliminar Registros  *
* m) Modificar Registros *
* p) Imprimir la tabla   *
* x) Salir               *
*                        *
=========================="

def main():
    opcion = '0'
    while opcion != 'X':
        print(menu)
        opcion = input("¿Que opcion deseas? : ").upper()
        if opcion == 'I':
            print("Insertar paises")
            ISO3 = input("Introduce la clave ISO3 del Nuevo Pais: ")
            CountryName = input("Introduce el nombre del nuevo pais: ")
            Capital = input("Introduce la Capital de nuevo Pais: ")
            CurrencyCode = input("Introduce el currency code del nuevo pais: ")
            r = paises.inserta_pais(ISO3 , CountryName ,Capital, CurrencyCode )
            if(r == 0):
                print("-> Error al insertar")
            else:
                print("-> Se inserto correctamente")
        elif opcion == 'E':
            print("Eliminar paises")
            Id = int(input("Introduce el Id del pais que desea Eliminar: "))
            r = paises.elimina_pais(Id)
            if(r == 0):
                print("El Pais no existe")
            else:
                print("-> el pais se elimino Correctamente")
        elif opcion == 'M':
            print("Modificar paises")
            Id = int(input("Introduce el Id del pais que quieres modificar: "))
            pais = paises.buscar_pais(Id)
            if pais == None:
                print("-> EL pais no existe")
            else:
                print("Pais a modificar: ")
                print(pais)
                ISO3 = input("Introduce la nueva clave ISO3 del pais a modificar: ")
                CountryName = input("Introduce el nuevo nombre del pais a modificar: ")
                Capital = input("Introduce la Capital del pais a modificar: ")
                CurrencyCode = input("Introduce el currency code del pais a modificar: ")
                r = paises.modifica_pais(Id , ISO3 , CountryName , Capital , CurrencyCode)
                if r == 0:
                    print("Modificacion no completada")
                else:
                    print("Se Modifico Correctamente")
        elif opcion == 'P':
            print("Imprimir paises")
            print(paises)
        elif opcion == 'X':
            print("-> Saliendo del sistema")
        else:
            print("Opcion no valida")

    pass

'''
from tkinter import *
from ventana import *
from ventana import Ventana

def main():
    root = Tk()
    root.wm_title("Crud Python MySql")
    app = Ventana(root)
    app.mainloop()

if __name__ == "__main__":
    main() 
